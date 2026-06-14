# Import CSV Data into PostgreSQL

To import data from a CSV file into a PostgreSQL database, you must first create a target table that matches the structure of the CSV file. Once the table is created, you can use the `\copy` command to load the data.

## Step 1: Create the `transactions` table

Run the `ddl_transactions.sql` script to create the `transactions` table.

## Step 2 - Connect to your database using: 

Use the following command to connect to PostgreSQL:

```bash
psql -U <username> -d <database_name>
```

For this project:

```bash
psql -U postgres -d expense_tracker
```

## Step 3 - Execute the file import

```bash
\copy transactions FROM '/path/to/your/file.csv' DELIMITER ',' CSV HEADER;
```

E.g budgetwise_synthetic_cleaned.csv to transactions table

```bash
\copy transactions FROM 'data/budgetwise_synthetic_cleaned.csv' DELIMITER ',' CSV HEADER;
```
Successfully return `COPY 14858` message