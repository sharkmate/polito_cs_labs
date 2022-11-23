"""
When you use an automated teller machine (ATM) with your bank card,
 you need to use a personal identification number (PIN)
 to access your account.
If a user fails more than three times when entering the PIN, the machine will block the card.
Assume that the user’s PIN is “1234” and write a program that asks the user for the PIN no more than three times,
and does the following:

If the user enters the right number, print a message saying,
 “Your PIN is correct”, and end the program.
If the user enters a wrong number, print a message saying,
“Your PIN is incorrect” and, if you have asked for the PIN less than three times, ask for it again.
If the user enters a wrong number three times,
print a message saying “Your bank card is blocked” and end the program.

"""
PIN = 1234


def main():
    count = 1
    while count <= 3:
        pin = (input("insert your PIN code"))
        pin = int(pin)
        if pin == PIN:
            print("your PIN is correct")
            break
        else:
            if count == 3:
                print("your bank card is now blocked")
            else:
                print(f"your PIN is incorrect, try again")
            count += 1


if __name__ == "__main__":
    main()
