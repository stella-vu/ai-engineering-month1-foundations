# 🚀 Live Crypto Dashboard

A professional real-time cryptocurrency dashboard built with Python, Streamlit, and the CoinGecko API.

This project provides live crypto market tracking with interactive charts, dynamic currency conversion, caching optimization, and responsive dashboard components.

---

# ✨ Features

- 📈 Real-time cryptocurrency price tracking
- 🌍 Multiple fiat currency support
- 🎨 Dynamic chart color based on 24h market performance
- ⚡ Auto-refreshing live dashboard
- 📊 Interactive Plotly charts
- 🕒 Custom hover timestamps
- 🚀 Optimized API requests with caching
- 🔄 Persistent HTTP sessions using `requests.Session()`
- 🛡️ Error handling for API/network failures
- 📱 Responsive wide-layout dashboard

---

# 🖼️ Dashboard Preview

![Dashboard Screenshot](assets/dashboard.gif)

---

# 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Interactive web dashboard |
| Plotly | Interactive chart visualization |
| Pandas | Data manipulation |
| Requests | API communication |
| CoinGecko API | Cryptocurrency market data |

---

# 🧠 Engineering Concepts Demonstrated

- REST API integration
- Object-oriented programming (OOP)
- HTTP session management
- API response caching
- Dynamic UI rendering
- Data visualization
- Error handling
- Config-driven architecture
- Interactive frontend engineering

---

# 📂 Project Structure

```text
crypto-dashboard/
│
├── app.py                 # Main Streamlit application
├── requirements.txt       # Project dependencies
├── README.md              # Project documentation
├── .gitignore             # Ignore unnecessary files for Git
├── .env                   # Environment variables (API keys)
│
├── assets/
│   └── dashboard.gif     # Dashboard screenshot
