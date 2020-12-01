def main():
    x = 0

    # while loop
    while (x<10):
        print(x)
        x = x+1

    # for loop
    print("For loop starting ----------")
    for x in range(1, 5):
        print(x)

    # looping over list
    print("-----Days of Week-----")
    days=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for d in days:
        print(d)

    # break and continue statements
    print("-----break & continue-----")
    for x in range(1, 5):
        if (x==3): break
        print(x)

    # break and continue statements
    print("-----break & continue-----")
    for x in range(1, 5):
        if (x % 2) == 0: continue
        print(x)

if __name__ == "__main__":
    main()    