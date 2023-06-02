from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
page = response.text

soup = BeautifulSoup(page, "html.parser")
articles = soup.find_all(name="span", class_="titleline")
article_links = []
article_texts = []
for tag in articles:
    articletext = tag.getText()
    article_texts.append(articletext)
    article_link = tag.find("a").get("href")
    article_links.append(article_link)

article_upvotes = soup.find_all(name="span", class_="score")

article_votes = [int(score.getText().split()[0]) for score in article_upvotes]

highest = article_votes.index(max(article_votes))
print(article_texts[highest])
print(article_links[highest])
print(article_votes[highest])