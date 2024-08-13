MAX_LINES=3
MAX_BET=10
MIN_BET=1
def deposit():
    while True:
        amount=input("What amount You want to Deposit? $")
        if amount.isdigit:
            amount=int(amount)
            if amount > 0:
                break
            else:
                print("Enter a number which is greather than 0.")
        else:
            print("Enter a number")

    return amount

def number_of_lines():
    while True:
        lines=input("Enter the number of lines to bet on (1-" +str(MAX_LINES) +")?")
        if lines.isdigit:
            lines=int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a Valid Number of Lines.")
        else:
            print("Enter a number")

    return lines

def getbet():
    while True:
        amount=input ("Enter the amount of bet you would like for each line $")
        if amount.isdigit:
            amount = int(amount)
            if MIN_BET <= amount <=MAX_BET:
                break    
            else:
                print(f"Enter an amount between ${MIN_BET} - ${MAX_BET}.") 
        else:
            print("Enter Valid Number")   
            
    return amount

def main():
    balance= deposit()
    line= number_of_lines()
    bet = getbet()
    total_bet =bet * line
    print (f"You are betting {bet} on {line} lines. and the total bet is = {total_bet}")

main()