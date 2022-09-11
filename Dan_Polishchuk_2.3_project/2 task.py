from bs4 import BeautifulSoup as BS
import requests
import re
main_url = "https://www.basketball-reference.com/players/m/mykhasv01.html"
req = requests.get(main_url)
soup = BS(req.text, "html.parser")

#######################################################################################################################
print("Sviatoslav 'Svi' Yuriyovych Mykhailiuk (Ukrainian: Святосла́в Ю́рійович Михайлю́к, born June 10, 1997) \nis a "
      "UKRAINIAN professional basketball player who is currently a free agent and last played for the Toronto Raptors\n"
      "of the National Basketball Association (NBA). He was selected with the 47th overall pick in the 2018 NBA\n"
      "draft by the Los Angeles Lakers.\n\nMy algorithm suggests looking at Svi`s stats in the NBA ")
print("Which season do you want to see the stats for?\n1 - 2018-19\n2 - 2019-20\n3 - 2020-21\n4 - 2021-22")
user_data = int(input("Type 1,2,3 or 4 : "))

def season1():
    stats = soup.find("div", id="div_per_game").find("thead")
    match1 = re.findall(r"[\w%-]+\s", stats.get_text())
    data = soup.find("tr", id="per_game.2019")
    match2 = re.findall(r"[\w.%-]+\s", data.get_text(" "))
    for i in range(len(match1)-1):
        match1[i] += ":"
        match1[i] += match2[i]
        print(*match1[i])

def season2():
    stats = soup.find("div", id="div_per_game").find("thead")
    match1 = re.findall(r"[\w%-]+\s", stats.get_text())
    data = soup.find("tr", id="per_game.2020")
    match2 = re.findall(r"[\w.%-]+\s", data.get_text(" "))
    for i in range(len(match1)-1):
        match1[i] += ":"
        match1[i] += match2[i]
        print(*match1[i])

def season3():
    stats = soup.find("div", id="div_per_game").find("thead")
    match1 = re.findall(r"[\w%-]+\s", stats.get_text())
    data = soup.find("tr", id="per_game.2021")
    match2 = re.findall(r"[\w.%-]+\s", data.get_text(" "))
    for i in range(len(match1)-1):
        match1[i] += ":"
        match1[i] += match2[i]
        print(*match1[i])

def season4():
    stats = soup.find("div", id="div_per_game").find("thead")
    match1 = re.findall(r"[\w%-]+\s", stats.get_text())
    data = soup.find("tr", id="per_game.2022")
    match2 = re.findall(r"[\w.%-]+\s", data.get_text(" "))
    for i in range(len(match1)-1):
        match1[i] += ":"
        match1[i] += match2[i]
        print(*match1[i])

if user_data == 1:
    season1()
elif user_data == 2:
    season2()
elif user_data == 3:
    season3()
elif user_data == 4:
    season4()
else:
    print("Please choose the right season")
