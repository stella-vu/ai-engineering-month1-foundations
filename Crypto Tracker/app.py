import requests
import streamlit as st
from streamlit_autorefresh import st_autorefresh
import pandas as pd
import os
import plotly.express as px
import dotenv

# --------------------------------------
# Load API key from environment variable
# --------------------------------------
dotenv.load_dotenv()
api_key = os.getenv("COINGECKO_API_KEY")

if not api_key:
    st.error("Missing CoinGecko API Key")
    st.stop()

st.set_page_config(page_title="Crypto Dashboard", layout="wide")

st.title("🚀 Live Crypto Dashboard")
st.caption("Real-time cryptocurrency dashboard powered by CoinGecko API")

st_autorefresh(interval=30000, key="crypto_refresh")



class CoinGeckoClient:
   
    BASE_URL = "https://api.coingecko.com/api/v3/"
    
    def __init__(self, api_key):
        self.session = requests.Session()
        self.session.headers.update({"x-cg-demo-api-key": api_key})


    def fetch_data(self, endpoint, params=None):
        url = self.BASE_URL + endpoint
        try:
            response = self.session.get(url, params=params, timeout=5)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"API request failed: {e}")

    @st.cache_data(ttl=30)
    def get_coin_prices(_self, coin_ids, vs_currency):
        params = {
            "ids": ",".join(coin_ids),
            "vs_currencies": vs_currency,
            "include_24hr_change": "true"
        }
        return _self.fetch_data("simple/price", params)
    
    @st.cache_data(ttl=300)
    def get_market_chart(_self, coin_id, days=7, vs_currency="usd"):
        params = {
            "vs_currency": vs_currency,
            "days": str(days)
        }

        data = _self.fetch_data(f"coins/{coin_id}/market_chart", params)
        df = pd.DataFrame(data["prices"], columns=["timestamp", "price"])
        df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
        df["formatted_time"] = df["timestamp"].dt.strftime("%b %d %Y %H:%M:%S")
        return df


COINS = {
    "Bitcoin": "bitcoin",
    "Ethereum": "ethereum",
    "Dogecoin": "dogecoin",
    "TRON": "tron"
}

CURRENCIES = {
    "USD": "usd",
    "EUR": "eur",
    "AUD": "aud",
    "VND": "vnd",
    "GBP": "gbp",
    "CNY": "cny",
    "JPY": "jpy"
}

CURRENCY_SYMBOLS = {
    "USD": "$",
    "EUR": "€",
    "AUD": "A$",
    "VND": "₫",
    "GBP": "£",
    "CNY": "¥",
    "JPY": "¥"
}

# -----------------------------------
# SIDEBAR
# -----------------------------------

st.sidebar.title("⚙️ Settings")

selected_label = st.sidebar.selectbox("Select Coin", list(COINS.keys()))
selected_coin = COINS[selected_label]

selected_currency = st.sidebar.selectbox("Select Currency", list(CURRENCIES.keys()))
selected_currency_code = CURRENCIES[selected_currency]
selected_currency_symbol = CURRENCY_SYMBOLS[selected_currency]
selected_days = st.sidebar.slider("Select Time Range (days)",
    min_value=1,
    max_value=30,
    value=7
)

# -----------------------------------
# Live Price Metrics
# -----------------------------------
api = CoinGeckoClient(api_key)

try:
    coin_prices = api.get_coin_prices(list(COINS.values()), selected_currency_code)
    cols = st.columns(len(COINS))
    for col, (label, coin_id) in zip(cols, COINS.items()):
        coin_data = coin_prices[coin_id]
        price = coin_data[selected_currency_code]
        change = coin_data[f"{selected_currency_code}_24h_change"]
        with col:
            st.metric(label=f"**{label}**", value=f"{selected_currency_symbol}{price:,.2f}", delta=f"{change:.2f}%")

except Exception as e:
    st.error(f"Error fetching coin prices: {e}")

# -----------------------------------
# Chart
# -----------------------------------

st.subheader(f"📈 {selected_label} Price Chart (Last {selected_days} days)")

try:
    chart_data = api.get_market_chart(
        selected_coin,
        selected_days,
        selected_currency_code
    )

    min_price = chart_data["price"].min()
    max_price = chart_data["price"].max()

    padding = (max_price - min_price) * 0.1

    y_min = min_price - padding
    y_max = max_price + padding

    selected_change = coin_prices[selected_coin][f"{selected_currency_code}_24h_change"]
    line_color = "green" if selected_change >= 0 else "red"
    
    fig = px.line(
        chart_data,
        x="timestamp",
        y="price",
        title=f"{selected_label} Price ({selected_currency})"
    )

    fig.update_yaxes(
        range=[y_min, y_max]
    )

    fig.update_traces(
        hovertemplate=
        "<b>Time:</b> %{customdata}<br>" +
        f"<b>Price:</b> {selected_currency_symbol}%{{y:,.2f}}<extra></extra>",
        customdata=chart_data["formatted_time"],
        line=dict(color=line_color)
    )

    fig.update_layout(
        xaxis_title="Time",
        yaxis_title=f"Price ({selected_currency})",
        hovermode="x unified"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

except Exception as e:
    st.error(f"Error fetching market chart: {e}")

