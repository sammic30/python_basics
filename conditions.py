def main():
    x, y = 1000, 200

    #conditional flow uses if, elif, else
    if (x < y):
        num = "x is less than y"
    elif (x == y):
        num = "x is the same as y"
    else:
        num = "x is greater than y"

    print (num)

if __name__ == "__main__":
    main()