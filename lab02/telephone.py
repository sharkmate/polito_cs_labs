"""
The following pseudocode describes how to transform a string
containing a ten-digit telephone number (such as "4155551212") into a more easily readable string,
formatted in the U.S. style, such as "(415) 555–1212":
I. Take the string consisting of the first three characters and surround it with round brackets
(this is the prefix, called "area code");
II. Concatenating the prefix with the string containing the next three characters, a hyphen, and
the string consisting of the last four characters results in the number in the required format.
Translate this pseudocode into a Python program that stores a 10-digit phone number in a string,
and then display it in the format just described.
"""

def main():
    phone = (input("insert your 10 digits phone number "))
    print(f'your american phone number is  ({phone[:3]}) {phone[3:6]}-{phone[6:]}')

if __name__ == '__main__':
    main()
