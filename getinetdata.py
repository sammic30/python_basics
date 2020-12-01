import urllib.request
import urllib3.request

def main():
    # Connect and reterieve data from internet
    webUrl = urllib.request.urlopen("https://www.google.com")
    print("result code: " + str(webUrl.getcode()))
    data = webUrl.read()
    print(data)

if __name__ == "__main__":
    main()