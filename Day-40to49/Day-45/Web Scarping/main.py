from bs4 import BeautifulSoup
import requests

URL ="https://news.ycombinator.com"

response = requests.get(url=URL ,timeout=None)
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page,"html.parser")


article_tag = soup.select(selector=".titleline a")

article_texts = []
article_links = []

for article in article_tag:
    text = article.get_text()
    article_texts.append(text)
    link = article.get("href")
    article_links.append(link)

    
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span",class_="score")]

print(article_texts)
print(article_links)
print(article_upvotes)

# max = 0
# for news_upcotes in article_upvotes:
#     if news_upcotes > max :
#         max = news_upcotes

largest_no = max(article_upvotes)
print(largest_no)
index = article_upvotes.index(largest_no)

print(article_texts[index])
print(article_links[index])

























# # import lxml #for parsing instead of html.parser



# with open(file="Day-40to49/Day-45/Web Scarping/website.html",
#           encoding="utf_8") as website_html :
#     contents = website_html.read()

# soup = BeautifulSoup(contents,"html.parser")

# # print(soup.title)
# # print(soup.title.string)
# # print(soup.prettify())
# # print(soup.a)

# all_anchor_tag = soup.find_all(name="a")
# # print(all_anchor_tag)

# # for tag in all_anchor_tag:
# #     # print(tag.getText())
# #     print(tag.get("href"))

# heading = soup.find(name="h1",id="name")
# # print(heading)

# section_heading = soup.find_all(name="h3",class_="heading")
# print(section_heading)

# name = soup.select_one(selector="#name")
# print(name)

# headings= soup.select(".heading")
# print(headings)
