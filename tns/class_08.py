b_d = {}

def create_acc(acc_num, cs_name, acc_pin, o_b = 0.0):
    if acc_num in b_d:
        print(f"Error: Account {acc_num} already exist".)
        return False

    b_d[acc_num] = {
        "Customer Name" : cs_name,
        "Account Pin" : acc_pin,
        "Account Balance" : o_b
    }

    print(f"Success: Account created for {cs_name}.")
    print(f"Starting Balance: ${opening_balance}")
    return True


def dep_money(acc_num, d_a):
    if acc_num not in b_d:
        print(f"Error: Account {acc_num} not found!")
        return False

    if d_a <= 0:
        print("Error: Deposit amount must be greater then zero.")
        return False

    b_d[acc_num]["Account Balance"] += d_a

    print(f"Success: Deposited ${d_a}. New Balance: ${b_d[acc_num]['Account Balance']}")
    return True

def with_money(acc_num, pin, w_a):

    if acc_num not in b_d:
        print(f"Error: Account {acc_num} not found.")
        return False

    acc_details = b_d[acc_num]

    if acc_details["Account Pin"] != pin:
        return False

    acc_details = b_d[acc_num]

    



    

