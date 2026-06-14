# Data Cleaning Process

## Overview

This document describes the data cleaning pipeline used to transform raw transaction data into a clean, production-ready dataset suitable for PostgreSQL database import.

## Raw Data

**Source File:** `data/budgetwise_synthetic_dirty.csv`

**Size:** Contains synthetic transaction records with various data quality issues.

## Data Quality Issues Identified

1. **Duplicate Rows** - Identical transaction records appearing multiple times
2. **Missing Values** - Null or empty values in critical fields
3. **Inconsistent Date Formats** - Dates in mixed formats
4. **Categorical Inconsistencies** - Varying case and naming conventions
5. **Invalid Values** - Out-of-range or nonsensical values

## Cleaning Pipeline Steps

### Step 1: Load Data

```python
import pandas as pd
df = pd.read_csv('data/budgetwise_synthetic_dirty.csv')
df.shape  # Check dimensions
```

**Output:** Initial dataset size and structure

---

### Step 2: Check for Missing Values

```python
df.isnull().sum()
```

Identifies which columns have missing data and how many missing values.

**Action:** 
- Drop rows with critical missing values
- Fill non-critical missing values with appropriate defaults

---

### Step 3: Remove Duplicate Rows

```python
# Check for duplicates
print("Rows before:", len(df))
df = df.drop_duplicates()
print("Rows after:", len(df))
```

**Result:** Removes identical transaction records

---

### Step 4: Standardize Date Format

```python
df['date'] = pd.to_datetime(
    df['date'],
    format='mixed', 
    errors='coerce'
)
```

**Actions:**
- Parse mixed date formats
- Coerce invalid dates to NaT (Not a Time)
- Convert to standard ISO format (YYYY-MM-DD)

---

### Step 5: Validate Transaction Types

```python
df['transaction_type'].unique()
```

**Expected Values:** 
- `income` - Money received
- `expense` - Money spent

**Action:** Standardize to lowercase, remove invalid values

---

### Step 6: Clean and Map Categories

```python
df['category'].unique()
df['category'].value_counts()
```

**Common Issues:**
- Inconsistent capitalization (e.g., "FOOD" vs "Food")
- Typos and misspellings ('Salray', 'Other Incmoe', 'Oher Income', 'Entertainmet', 'Healh')
- Too many granular categories

**Solution:** 
- Step 1: Use rapidfuzz to find similar categories and create a new column with cleaned categories. 
- Step 2: Create a manual mapping to standardize categories:

```python
category_mapping = {
    'eRnt': 'Rent',
    'Retn': 'Rent',
    'Rnet': 'Rent',
    'oFod': 'Food',
    'Fodo': 'Food'
    # ... additional mappings
}

df['category'] = df['category'].map(category_mapping)
```

**Final Categories:**
- Bonus
- Education
- Entertainment
- Food
- Health
- Other Income
- Others
- Rent
- Salary
- Savings
- Travel
- Utilities


---

### Step 7: Clean Amount Field

```python
# Convert to numeric, handle errors
df['amount'] = pd.to_numeric(df['amount'], errors='coerce')

# Remove negative amounts
df = df[df['amount'] > 0]
```

---

### Step 8: Standardize Text Fields

Clean fields like location, notes, payment_mode:

```python
df['payment_mode'] = df['payment_mode'].str.lower().str.strip()
df['location'] = df['location'].str.strip()
```

---

### Step 9: Remove Invalid Records

```python
# Keep only records with valid dates
df = df[df['date'].notna()]

# Keep only records with valid transaction types
valid_types = ['income', 'expense']
df = df[df['transaction_type'].isin(valid_types)]

# Keep only records with valid amounts
df = df[df['amount'].notna()]
```

---

### Step 10: Handle Outliers (Optional)

```python
# Identify outliers using IQR method
Q1 = df['amount'].quantile(0.25)
Q3 = df['amount'].quantile(0.75)
IQR = Q3 - Q1

outliers = df[(df['amount'] < Q1 - 1.5*IQR) | (df['amount'] > Q3 + 1.5*IQR)]

# Review outliers - decide whether to keep or remove
# df = df[~((df['amount'] < Q1 - 1.5*IQR) | (df['amount'] > Q3 + 1.5*IQR))]
```

---

## Duplicate Transaction Resolution

The dataset contained duplicate transaction_ids.

To resolve conflicting duplicates:

1. Calculated completeness_score using count of non-null values.
2. Selected the most complete record.
3. Flagged ties for manual review.
4. Removed exact duplicate rows.

---

## Cleaned Data

**Output File:** `data/budgetwise_synthetic_cleaned.csv`

**Data Quality Metrics:**
- No duplicate rows
- No critical missing values
- Standardized formats
- Validated categories
- Consistent column names

## Data Validation

### Before & After Comparison

| Metric | Before | After |
|--------|--------|-------|
| Total Records | 15,836 | 14,698 |
| Duplicate Records | 804 | 0 |
| Bad Amount Format | 5265 | 0 |
| Records with Missing Amount | 178 | 0 |
| Valid Date Format | 35% | 100% |
| Unique Categories | 213 | 12 |
