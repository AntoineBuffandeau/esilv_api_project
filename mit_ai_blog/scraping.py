import requests
from bs4 import BeautifulSoup

def scrape_mit_news():
    try:
        url = "https://news.mit.edu/topic/artificial-intelligence2"
        response = requests.get(url)
        response.raise_for_status()  # Gérer les erreurs HTTP
        soup = BeautifulSoup(response.content, "html.parser")
        articles = []
        article_tags = soup.find_all("div", class_="term-page--news-article--item--descr")
        number = 0
        for article_tag in article_tags[:5]:
            number += 1
            title = article_tag.find("h3", class_="term-page--news-article--item--title").text.strip()
            link = "https://news.mit.edu" + article_tag.find("a", class_="term-page--news-article--item--title--link")["href"]
            date = article_tag.find("time").text.strip()
            articles.append({"Article number" : number, "title": title, "date": date, "link": link})
        return articles
    except Exception as e:
        print("Error fetching data from MIT News:", e)
        return []

def scrape_article_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Gérer les erreurs HTTP
        soup = BeautifulSoup(response.content, "html.parser")
        article_content = soup.find("div", class_="paragraph--type--content-block-text")
        if article_content:
            paragraphs = article_content.find_all("p")
            formatted_content = "\n".join(paragraph.get_text(strip=True) for paragraph in paragraphs)
            return formatted_content
        else:
            return None
    except Exception as e:
        print("Error fetching article content:", e)
        return None
