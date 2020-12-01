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

    # for each event, print place
    for i in newJSON["features"]:
        print(i["properties"]["place"])
        print("--------------------")

    # events that have magnitude over 4
    for i in newJSON["features"]:
        if i["properties"]["mag"] >= 4.0:
            print("%2.1f" % i["properties"]["mag"], i["properties"]["place"])
            print("---------------------------------")

def main():
    urlData = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
    
    # Open URL and read the data
    webUrl = urllib.request.urlopen(urlData)
    print("result code: " + str(webUrl.getcode()))
    if (webUrl.getcode() == 200):
        data = webUrl.read().decode("utf-8")
        printresults(data)
    else:
        print("Received error, cannot parse results" + str(webUrl.getcode()))



if __name__ == "__main__":
    main()