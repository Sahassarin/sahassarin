# Complete this program to classify people by age
age = int(input("Enter age: "))

# Add your if-elif-else statements here
# 0-12: Child
# 13-19: Teenager  
# 20-59: Adult
# 60+: Senior

# Your code here:
age = int(input("Enter age: "))

if age <= 12:
  print ("Child")
elif age <=19:
  print ("Teenager")
elif age <=59:
  print ("Adult")
elif age >=60:
  print ("Senior")


# Complete this ATM simulation
balance = 1000
pin = "1234"

entered_pin = input("Enter PIN: ")
if entered_pin == pin:
    print("PIN accepted")
    while True:
        print("\n1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit") 
        print("4. Exit")
        
        choice = input("Choose option: ")
        
        # Complete the menu logic here
        # Your code here:
        if choice == "4":
            break
        elif choice == "1":
           print ("Balance: ", balance, "บาท")
        elif choice == "2":
           amount = float(input("ถอนเท่าไหร่???"))
           balance = balance - amount
        elif choice == "3":
           amount = float(input("ฝากจำนวนเท่าไหร่"))
           balance = balance + amount
else:
    print("Invalid PIN")
