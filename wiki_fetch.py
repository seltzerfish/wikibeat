import lxml
import bs4
import urllib


def fetch_page_content(url):
    data = urllib.request.urlopen(url)
    content = data.read()
    parsed_content = bs4.BeautifulSoup(content, "lxml")
    paragraphs = parsed_content.find_all("p")
    article_text = ""
    for p in paragraphs:
        article_text += p.text
    return article_text.replace("\n", " ")
