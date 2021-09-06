import requests
import json
from bs4 import BeautifulSoup


# class for f1 raceweek
class formulaRaceWeek:
    def __init__(self, name):
        self.name = name
        self.events = []

    def addEvent(self, event):
        self.events.append(event)

    def printRaceWeek(self):
        print(str(self.name))
        for event in self.events:
            event.printEvent()

# class for f1 events


class formulaEvent:
    def __init__(self, date, name, time):
        self.date = date
        self.name = name
        self.time = time

    def printEvent(self):
        print("{} - {} - {}".format(self.date, self.name, self.time))

# get the schedules from the formula1 page


def getTimeLine(link):
    # if there is no official schedule then:
    if("TBC" in link):
        return

    page = requests.get("https://www.formula1.com{}".format(link))
    soup = BeautifulSoup(page.content, "html.parser")
    location = soup.find("h2", class_="f1--s")
    raceName = location.text
    race = formulaRaceWeek(raceName)
    URL = "https://www.formula1.com{}/Timetable.html".format(
        link.replace(".html", ""))
    page = requests.get(URL)

    if page.status_code != 200:
        page = requests.get("https://www.formula1.com{}".format(link))
        soup = BeautifulSoup(page.content, "html.parser")
        h1 = soup.find("h1")
        print(type(h1.text))
        print()
        print("No official data yet")
        print()
        return
    soup = BeautifulSoup(page.content, "html.parser")
    f1 = soup.find_all("td")

    for i in range(0, len(f1)):
        if "thursday" in f1[i].text.lower():
            date = f1[i].text.strip("\n")
        if "friday" in f1[i].text.lower():
            date = f1[i].text.strip("\n")
        if "saturday" in f1[i].text.lower():
            date = f1[i].text.strip("\n")
        if "sunday" in f1[i].text.lower():
            date = f1[i].text.strip("\n")

        if "Formula 1" in f1[i].text:
            if "Practice" in f1[(i+1)].text:
                name = f1[i+1].text.strip("\n")
                time = f1[i+2].text.strip("\n")
                event = formulaEvent(date, name, time)
                race.addEvent(event)
            if "Qualifying" in f1[(i+1)].text:
                name = f1[i+1].text.strip("\n")
                time = f1[i+2].text.strip("\n")
                event = formulaEvent(date, name, time)
                race.addEvent(event)
            if "Grand Prix" in f1[(i+1)].text:
                name = f1[i+1].text.strip("\n")
                time = f1[i+2].text.strip("\n")
                event = formulaEvent(date, name, time)
                race.addEvent(event)

    race.printRaceWeek()
    print()


URL = "https://www.formula1.com/en/racing/2021.html"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
h1 = soup.find("h1")
print(h1.text)

races = soup.find_all("a", class_="event-item-wrapper event-item-link")
for i in races:
    getTimeLine(i["href"])
