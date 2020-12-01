def main():
    #open a file
    f = open("textfile.txt", "w+") #w+ is required if file is NOT existed

    for i in range(10):
        f.write("This is line " + str(i) + "\r\n")

    f.close()

if __name__ == "__main__":
    main() 