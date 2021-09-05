import requests
import json
from bs4 import BeautifulSoup


class formulaEvent:
    def __init__(self, date, name, time):
        self.date = date
        self.name = name
        self.time = time

    def printEvent(self):
        print("{} - {} - {}".format(self.date, self.name, self.time))


def getTimeLine(link):
    if("TBC" in link):
        return print("No Race")
    URL = "https://www.formula1.com{}/Timetable.html".format(
        link.replace(".html", ""))
    print(URL)
    page = requests.get(URL)
    if page.status_code != 200:
        print()
        page = requests.get("https://www.formula1.com{}".format(link))
        soup = BeautifulSoup(page.content, "html.parser")
        h1 = soup.find("h1")
        print(h1.text)
        print()
        print("No official data yet")
        print()
        return

    soup = BeautifulSoup(page.content, "html.parser")
    location = soup.find("h1")
    print(location.text)
    f1 = soup.find_all("td")

    for i in range(0, len(f1)):
        if "thursday" in f1[i].text.lower():
            print()
            date = f1[i].text
            print(f1[i].text)
            print()
        if "friday" in f1[i].text.lower():
            print()
            date = f1[i].text
            print(f1[i].text)
            print()
        if "saturday" in f1[i].text.lower():
            print()
            date = f1[i].text
            print(f1[i].text)
            print()
        if "sunday" in f1[i].text.lower():
            print()
            date = f1[i].text
            print(f1[i].text)
            print()

        if "Formula 1" in f1[i].text:
            if "Practice" in f1[(i+1)].text:
                name = f1[i+1].text
                time = f1[i+2].text
                print(f1[i].text+" " +
                      f1[i+1].text.replace("\n", "")+" "+f1[i+2].text)
                event = formulaEvent(date, name, time)
                event.printEvent()
            if "Qualifying" in f1[(i+1)].text:
                name = f1[i+1].text
                time = f1[i+2].text
                print(f1[i].text+" " +
                      f1[i+1].text.replace("\n", "")+" "+f1[i+2].text)
                event = formulaEvent(date, name, time)
                event.printEvent()
            if "Grand Prix" in f1[(i+1)].text:
                name = f1[i+1].text
                time = f1[i+2].text
                print(f1[i].text+" " +
                      f1[i+1].text.replace("\n", "")+" "+f1[i+2].text)
                event = formulaEvent(date, name, time)
                event.printEvent()


URL = "https://www.formula1.com/en/racing/2021.html"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
h1 = soup.find("h1")
print(h1.text)

races = soup.find_all("a", class_="event-item-wrapper event-item-link")
for i in races:
    getTimeLine(i["href"])
