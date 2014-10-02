from bs4 import BeautifulSoup
import requests
import sys

def get_links(artist):
	#constructs url to scrape from
	search_url = 'http://genius.com/search?q=' + str(artist)

	#get html from page
	user_agent = {'User-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1944.0 Safari/537.36'}
	response = requests.get(search_url,headers = user_agent)

	#scrape out links from page
	links = []
	soup = BeautifulSoup(response.text)
	for link in soup.select('ul.search_results > li > a'):
		links.append(link['href'])	
	
	return links

if __name__ == '__main__':
	links = get_links(sys.argv[1])

	for link in links:
		print link
