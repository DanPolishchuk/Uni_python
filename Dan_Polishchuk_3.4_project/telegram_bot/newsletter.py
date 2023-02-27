from main import bot, cur
from bs4 import BeautifulSoup as bs
from requests import get
from time import sleep

def sending_news():
    while True:
        cur.execute("""SELECT chat_id FROM Users_data""")
        chat_ids = cur.fetchall()
        cur.execute("""SELECT chat_ids FROM Stop_list""")
        stop_list = cur.fetchall()
        for id in chat_ids:
            if id not in stop_list:
                cur.execute(f"""SELECT news_type FROM Users_data
                                WHERE chat_id="{id[0]}" """)
                type_news = cur.fetchall()
                if type_news[0][0] == "1":
                    sport_news(id[0])
                elif type_news[0][0] == "2":
                    crypto_news(id[0])
                elif type_news[0][0] == "3":
                    politics_news(id[0])
                elif type_news[0][0] == "4":
                    sport_news(id[0])
                    crypto_news(id[0])
                elif type_news[0][0] == "5":
                    sport_news(id[0])
                    politics_news(id[0])
                elif type_news[0][0] == "6":
                    crypto_news(id[0])
                    politics_news(id[0])
                elif type_news[0][0] == "7":
                    sport_news(id[0])
                    crypto_news(id[0])
                    politics_news(id[0])
        sleep(14400.0)


def sport_news(id):
    url = "https://www.nba.com/news"
    req = get(url)
    soup = bs(req.text, "html.parser")
    news = soup.find("div", class_="NewsView_dazn__ZF2K2").find_all("div", class_="ArticleTile_tileMainContent__c_bU1", limit=3)
    for i in news:
        bot.send_message(id, text=(i.find("h3", class_="Text_text__I2GnQ ArticleTile_tileTitle__aA8g7").get_text()+ "\n"+
            i.find("p", class_="Text_text__I2GnQ ArticleTile_tileSub__kiMA0").get_text()+ 
            "\nLink = https://www.nba.com"+i.find("a").get("href"), "\n"))

def crypto_news(id):
    url = "https://cryptonews.com/news/"
    req = get(url)
    soup = bs(req.text, "html.parser")
    news = soup.find("section", class_="category_contents_details").find_all("article", class_="mb-15 mb-sm-30 article-item", limit=3)
    for i in news:
        bot.send_message(id, text=(i.find("a", class_="article__title article__title--lg article__title--featured mb-20").get_text()+ "\n"+
            i.find("div", class_="mb-25 d-none d-md-block").get_text()+
            "\nLink = https://cryptonews.com"+i.find("a").get("href")+ "\n"))


def politics_news(id):
    url = "https://www.cnbc.com/politics/"
    req = get(url)
    soup = bs(req.text, "html.parser")
    news = soup.find("div", class_="SectionWrapper-content").find_all("a", class_="Card-title", limit=3)
    for i in news:
        bot.send_message(id, text=(i.get_text()+ "\nLink = "+i.get("href")+ "\n"))



if __name__ == "__main__":
    
    try:
        sending_news()
    
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)
    except IndexError as e:
        print(e)
    except ConnectionError as e:
        print(e)