# Bank Management System
Bank_DB = {}

def acc_create(acc_num, acc_holder, pin, initial_amount):
    if acc_num in Bank_DB:
        print("Aleardy has account!")
        return False
    Bank_DB{
        "name" : acc_holder,
        "pin" : pin,
        "balance" : initial_amount 
    }