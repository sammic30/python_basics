import urllib.request
import json

def printresults(data):
    #Use this json module to load string data into a dictonary
    newJSON = json.loads(data)

    # Access the content of the JSON
    if "title" in newJSON["metadata"]:
        print(newJSON["metadata"]["title"])

    # output number of events, plus magnitude
    count = newJSON["metadata"]["count"]
    print (str(count) + " event recorded")

def main():
    urlData = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
    
    # Open URL and read the data
    webUrl = urllib.request.urlopen(urlData)
    print("result code: " + str(webUrl.getcode()))
    if (webUrl.getcode() == 200):
        data = webUrl.read()
        printresults(data)
    else:
        print("Received error, cannot parse results")



if __name__ == "__main__":
    main()