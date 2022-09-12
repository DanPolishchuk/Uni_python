from bs4 import BeautifulSoup as BS
import requests
import re
main_url = "https://meteo.gov.ua/ua/"
req = requests.get(url=main_url, verify=False)
soup = BS(req.text, "html.parser")


#######################################################################################################################
print("Hi!Now you have possibility to look at weather in Kyiv")
user_choice = int(input("Please choose which weather you want to check\n1 - currently weather\n2 - weather for the "
                        "next 5 followings days\nType your answer here: "))
def forecast_now():
    city = soup.find("div", class_="hdr_fr_bl1_sity").get_text()
    date = soup.find("div", class_="hdr_fr_bl1_date").get_text()
    currently_weather = soup.find("div", style="position:relative; height:20px; text-align:left; padding-left:0px; "
                                                "margin-top:13px; font-size:19px; color:#4abbeb;").get_text()
    currently_temperature = soup.find("div", style="position:relative; height:24px; text-align:center; "
                                                   "padding-left:0px; top:-5px;  font-size:32px; color:#00a0e4"
                                                   ";").get_text()
    currently_wind = soup.find("div", style="position:relative; float:left; width:140px; margin-top:8px;").get_text()
    currently_humidity = soup.find("div", style="position:relative; float:left; width:140px;")
    currently_pressure = currently_humidity.find_next("div", style="position:relative; float:left;width:140px;").\
        get_text()
    weather_now = [city, date, currently_weather + currently_temperature, currently_wind, currently_humidity.get_text(),
                   currently_pressure]
    for i in range(len(weather_now)):
        match = re.sub(r"[\\n\s]+", " ", weather_now[i])
        print(match)

def forecast_5_days():
    day1 = soup.find("td", style="text-align:center; border-bottom:1px solid #dbdddf; border-right:1px solid #dbdddf; "
                                    "background-color:#f6fbfe;")

    day2 = soup.find("td", style="text-align:center; border-bottom:1px solid #dbdddf; border-right:1px solid #dbdddf; ")

    day3 = day2.find_next("td", style="text-align:center; border-bottom:1px solid #dbdddf; border-right:1px solid "
                                      "#dbdddf; background-color:#f6fbfe;")

    day4 = day3.find_next("td", style="text-align:center; border-bottom:1px solid #dbdddf; border-right:1px solid "
                                      "#dbdddf; ")

    day5 = day4.find_next("td", style="text-align:center; border-bottom:1px solid #dbdddf; border-right:1px solid "
                                      "#dbdddf; background-color:#f6fbfe;")

    weather1 = soup.find("td", style="border-bottom:1px solid #dbdddf; border-right:1px solid #dbdddf; "
                                     "background-color:#f6fbfe; color:#c4540a; font-size:15px;")

    weather2 = soup.find("td", style="border-bottom:1px solid #dbdddf; border-right:1px solid #dbdddf;  color:#c4540a; "
                                     "font-size:15px;")

    weather3 = weather2.find_next("td", style="border-bottom:1px solid #dbdddf; border-right:1px solid #dbdddf; "
                                              "background-color:#f6fbfe; color:#c4540a; font-size:15px;")

    weather4 = weather3.find_next("td", style="border-bottom:1px solid #dbdddf; border-right:1px solid #dbdddf;  "
                                              "color:#c4540a; font-size:15px;")

    weather5 = weather4.find_next("td", style="border-bottom:1px solid #dbdddf; border-right:1px solid #dbdddf; "
                                              "background-color:#f6fbfe; color:#c4540a; font-size:15px;")

    precipitation1 = soup.find("td", style="border-bottom:1px solid #dbdddf; border-right:1px solid #dbdddf; "
                                           "background-color:#f6fbfe; ").find("img", width="36px").find_next(
                                           "img", width="36px")
    precipitation2 = soup.find("td", style="border-bottom:1px solid #dbdddf; border-right:"
                                           "1px solid #dbdddf;  ").find("img", width="36px").find_next(
                                           "img", width="36px")
    precipitation3 = precipitation2.find_next("td", style="border-bottom:1px solid #dbdddf; border-right:1px solid "
                                                          "#dbdddf; background-color:#f6fbfe; "
                                                          "").find("img", width="36px").find_next("img", width="36px")
    precipitation4 = precipitation3.find_next("td", style="border-bottom:1px solid #dbdddf; border-right:"
                                           "1px solid #dbdddf;  ").find("img", width="36px").find_next(
                                           "img", width="36px")

    precipitation5 = precipitation4.find_next("td", style="border-bottom:1px solid #dbdddf; border-right:1px solid "
                                                          "#dbdddf; background-color:#f6fbfe; "
                                                          "").find("img", width="36px").find_next("img", width="36px")

    #------------------------------------------------------------------------------------------------------------------

    my_forecast = [day1.get_text() + ", Погода вдень:" + weather1.get_text() + ", Опади вдень:" +
                   precipitation1.get("title"), day2.get_text() + ", Погода вдень:" + weather2.get_text() +
                   ", Опади вдень:" + precipitation2.get("title"), day3.get_text() + ", Погода вдень:"
                   + weather3.get_text() + ", Опади вдень:" + precipitation3.get("title"), day4.get_text() +
                   ", Погода вдень:" + weather4.get_text() + ", Опади вдень:" + precipitation4.get("title"),
                   day5.get_text() + ", Погода вдень:" + weather5.get_text() + ", Опади вдень:" +
                   precipitation5.get("title")]

    for i in range(len(my_forecast)):
        match = re.sub(r"[\\n\s]+", " ", my_forecast[i])
        print(match)

if user_choice == 1:
    forecast_now()
elif user_choice == 2:
    forecast_5_days()
else:
    print("Please, choose one of two suggested variants")

