def print_user(id, email, age, balance, account_status):
    display_status = "Enabled" if account_status else "Disabled"

    print("======User Information======")
    print(
        f"ID: {id}\nEmail: {email}\nAge: {age}\nBalance: {balance}\nAccount Status: {display_status}\n")


user_id = 1
user_email = "johndoe@gmail.com"
user_age = 25
user_balance = 524.32
user_account_status = False

print_user(user_id, user_email, user_age, user_balance, user_account_status)

# Accidentially mutate user ID
user_id = 7

# Intentionally mutate data
user_email = "johndoe@outlook.com"
user_age = 26
user_balance = 200
user_account_status = True

print_user(user_id, user_email, user_age, user_balance, user_account_status)
