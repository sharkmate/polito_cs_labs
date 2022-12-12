"""
The administrative manager of a hotel records sales in a text file.
Each line contains the following 4 information, separated by semicolon characters (';'):
I. the client's name;
II. the service sold;
III. the amount paid;
IV. the date of the event.
The services sold may be, for example, a dinner, a conference, or lodging.
The proper format for this file is for it to contain 4 fields per line,
and for the amount paid to contain values of type float.
Write a program that reads this text file, and displays the total amount for each type of service,
reporting an error if the file does not exist or if its format is incorrect.

"""


def main():
    try:
        with open("hotel.txt") as records:
            lines = records.read().replace("\n", ";").split(";")
    except FileNotFoundError:
        print("the records aren't available on the device")
        exit(0)

    dinner_pay = 0
    lodging_pay = 0

    for index, element in enumerate(lines):
        if lines[index-1] == "Dinner":
            dinner_pay += float(element)
        if lines[index-1] == "Lodging":
            lodging_pay += float(element)

    print(f"the total amount paid for the dining service is {dinner_pay} "
          f"and the total amount paid for the lodging service is {lodging_pay}")


if __name__ == '__main__':
    main()