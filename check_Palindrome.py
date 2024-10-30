def is_palindrome(s):
    return s == s[::-1]

def main():
    while True:
        try:
            print("Press the number corresponding to the option to select it")
            print("0. Exit")
            print("1. Check for Palindrome")
            choice = int(input("Your choice: "))

            if choice == 1:
                string = input("Enter the string you want to check: ").lower()

                if is_palindrome(string):
                    print(f"\n{string} is a palindrome!\n")
                else:
                    reversed_string = string[::-1]
                    print(f"\n{string} is not a palindrome as it spells {reversed_string} when reversed.\n")

            elif choice == 0:
                print("\n#################### Thank you for using my program ####################\n")
                break

            else:
                print("\nInvalid input. Please enter 0 or 1.\n")

        except ValueError:
            print("\nEnter an integer value corresponding to your choice!\n")

if __name__ == "__main__":
    main()
