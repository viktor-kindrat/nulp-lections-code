balance = 1000
account_valid = True
withdrawl = 100

if account_valid and withdrawl <= balance:
    print("ok")
else:
    if not account_valid:
        print("account invalid")
    else:
        print("withdrawl is more than balance")
