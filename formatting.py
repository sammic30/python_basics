from datetime import datetime

def main():

    now = datetime.now()
    print(now.strftime("The current year is: %Y"))
    print(now.strftime("%a, %d %B, %Y"))
    print(now.strftime("The current time is: %I:%M:%S %p"))


if __name__ == "__main__":
    main()