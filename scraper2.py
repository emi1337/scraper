from bs4 import BeautifulSoup
from urllib2 import urlopen

base_url = "http://www.chicagoreader.com"

def get_category_links(section_url):
	html = urlopen(section_url).read()
	soup = BeautifulSoup(html, "lxml")
	boccat = soup.find("dl", "boccat")
	category_links = [BASE_URL + dd.a["href"] for dd in boccat.findAll("dd")]
	return category_links

def get_category_links(section_url):
	html = urlopen(section_url).read()
	soup = BeautifulSoup(html, "lxml")
	category = soup.find("h1", "headline").string
	winner = [h2.string for h2 in soup.findAll("h2", "boc1")]
	runners_up = [h2.string for h2 in soup.findAll("h2", "boc2")]
	return {"category": category,
			"category_url": category_url,
			"winner": winner,
			"runners_up": runners_up}

def make_soup(url):
	html = urlopen(url).read()
	return BeautifulSoup(html, "lxml")

soup = make_soup(url) # url we're passing into OG function



# ("/chicago/food-and-drink/Section?oid=846971")


