import pandas as pd
import random
from datetime import date

# Load the cleaned dataset
df = pd.read_csv('data/budgetwise_synthetic_cleaned.csv')

# Get unique user IDs
user_ids = sorted(df['user_id'].dropna().unique())

df['date'] = pd.to_datetime(df['date'])

# Get the earliest transaction date for each user to use as their registration date
user_registration_dates = (
    df.groupby('user_id')['date']
    .min()
    .to_dict()
)

# create a list of synthetic users with realistic names, emails, and dates of birth
first_names = [
    'Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Heidi',
    'Ivan', 'Judy', 'Karl', 'Leo', 'Mallory', 'Nina', 'Oscar', 'Peggy', 
    'Quentin', 'Rita', 'Sam', 'Trudy', 'Uma', 'Victor', 'Wendy', 'Xavier',
    'Yvonne', 'Zach', 'Anna', 'Brian', 'Catherine', 'Daniel', 'Emily', 'Fred', 'Gina',
    'Hank', 'Isabel', 'Jack', 'Karen', 'Liam', 'Mia', 'Nathan', 'Olivia', 'Paul', 'Queen', 'Ryan',
    'Sara', 'Tom', 'Ursula', 'Vince', 'Will', 'Xena', 'Yuri', 'Zoe',
    'Aaron', 'Beth', 'Caleb', 'Diana', 'Ethan', 'Fiona', 'George', 'Hannah',
    'Ian', 'Jessica', 'Kevin', 'Laura', 'Mark', 'Nora', 'Owen', 'Penny', 'Quinn', 'Rachel', 'Steve', 'Tina',
    'Uri', 'Vanessa', 'Walter', 'Ximena', 'Yosef', 'Zara'
]

last_names = [
    'Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis',
    'Rodriguez', 'Martinez', 'Hernandez', 'Lopez', 'Gonzalez', 'Wilson', 'Anderson',
    'Thomas', 'Taylor', 'Moore', 'Jackson', 'Martin', 'Lee', 'Perez', 'Thompson', 'White', 'Harris', 'Sanchez',
    'Clark', 'Ramirez', 'Lewis', 'Robinson', 'Walker', 'Young', 'Allen', 'King', 'Wright', 'Scott', 'Torres', 'Nguyen',
    'Hill', 'Flores', 'Green', 'Adams', 'Nelson', 'Baker', 'Hall', 'Rivera', 'Campbell', 'Mitchell', 'Carter', 
    'Roberts', 'Gomez', 'Phillips', 'Evans', 'Turner', 'Diaz', 'Parker', 'Cruz', 'Edwards', 'Collins', 
    'Reyes', 'Stewart', 'Morris', 'Morales', 'Murphy', 'Cook', 'Rogers', 'Gutierrez', 'Ortiz', 'Morgan', 
    'Cooper', 'Peterson', 'Bailey', 'Reed', 'Kelly', 'Howard', 'Ramos', 'Kim', 'Cox', 'Ward', 'Richardson', 'Watson', 'Brooks', 'Chavez', 'Wood'
]  

# Generate synthetic user data
users = []
used_emails = set()

for user_id in user_ids:
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    
    # Assign registration date based on the earliest transaction date for the user
    registration_date = user_registration_dates.get(user_id)
    
    # Generate date of birth such that the user is at least 18 years old at the time of registration
    first_transaction_year = registration_date.year
    max_birth_year = first_transaction_year - 18  # Assuming users are at least 18 years old at registration
    birth_year = random.randint(1960, max_birth_year)
    birth_month = random.randint(1, 12)
    birth_day = random.randint(1, 28)  # To avoid issues with February
    
    dob = date(birth_year, birth_month, birth_day)

    # Ensure unique email addresses
    email = f"{first_name.lower()}.{last_name.lower()}{birth_year}@example.com"
    while email in used_emails:
        email = f"{first_name.lower()}.{last_name.lower()}{birth_year}{random.randint(10, 99)}@example.com"
    
    used_emails.add(email)
    
    users.append({
        'user_id': user_id,
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'dob': dob,
        'registration_date': registration_date.date()  # Convert to date format
    })

users_df = pd.DataFrame(users)
users_df.to_csv('data/synthetic_users.csv', index=False)

print(f'Generated {len(user_ids)} users. Saved to synthetic_users.csv')

# Check for duplicates in user_id and email
print("Unique user_ids:", users_df["user_id"].nunique())
print("Unique emails:", users_df["email"].nunique())