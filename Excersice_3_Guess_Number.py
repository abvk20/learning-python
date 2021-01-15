winning_number = 90
while True:
    guess = int(input("Please enter a number"))
    if guess>winning_number:
        print("Enter a smaller number")
    elif guess<winning_number:
        print("Enter a larger number")
    else:
        print("U WON!")
        break