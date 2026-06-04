# aim is to show 1. show balance
#                2. Deposit
#                3. withdraw

def show_balance(balance):
    print(f"your balance is ${balance: .2f}")
    

def deposit():
    amount = float(input("Enter an amount to deposite: "))
    
    if amount <0:
        print("That's is not valid amount")
        return 0
    else:
        return amount

def withdraw():
    amount = float(input("enter a amount to withdraw: "))
    
    if amount > balance:
        print("Insufficient amount")
        return 0
    elif amount <=0 :
        print("money should be deposite")
    else: 
        return amount



def main():
    balance =0
    is_running = True

    while is_running:
      print("Banking program")
      print("1.Show the balance")
      print("2.deposite")
      print("3.withdraw")
      print("4.exit")
    
      choice = input("enter the choice(1-4): ")
    
      if choice == '1':
        show_balance(balance)
      elif choice == '2':
        balance += deposit()
      elif choice == '3':
        balance -= deposit()
      elif choice == '4':
        is_running = False
      else:
        print("That is not valid choice ")
    
    print("Thank you have a nice day")
    
if __name__ == '__main__':
    main()