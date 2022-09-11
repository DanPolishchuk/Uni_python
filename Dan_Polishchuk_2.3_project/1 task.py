from bs4 import BeautifulSoup as BS
import requests

main_url = "https://en.wikipedia.org/wiki/Apple_Inc."
req = requests.get(main_url)
soup = BS(req.text, "html.parser")

#######################################################################################################################

title = soup.find("h1", class_="firstHeading mw-first-heading")
print("Tittle:\n\n",title.get_text())

mid_titles = [i.get_text() for i in soup.find_all("span", class_="mw-headline")]
print("\n\nMiddle titles:\n\n")
for i in range(len(mid_titles)):
    print(mid_titles[i])

side_bar = soup.find("div", id="mw-panel").find_all("ul", class_="vector-menu-content-list")
dict_links = {}
for num, block in enumerate(side_bar):
    dict_links[num] = [i.get("href") for i in block.find_all("a", href=True)]
print("\n\nLinks:\n\n")
for i in range(len(dict_links)):
    print(dict_links[i])