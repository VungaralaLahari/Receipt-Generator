total = 0

while True:
    user = input("Enter item price or Q to exit: ").strip()

    if user.upper() == "Q":
        print("Thanks for visiting!")
        print(f"Final Bill Amount: {total}")
        break

    if user.isdigit():
        total += int(user)
        print(f"Current Total: {total}")
    else:
        print("Please enter a valid number or Q to exit")
