from bs4 import BeautifulSoup
import requests
import sys
import itertools

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

def get_lyrics(link):
	response = requests.get(link)

	soup = BeautifulSoup(response.text)
	lyrics = soup.find('div',class_='lyrics').text.strip()

	return lyrics	

if __name__ == '__main__':
	artists = ['drake','kanye','lil+wayne','kendrick+lamar','jay+z','2+chainz','sage+the+gemini']
	lyrics =''	
	links =[]
	
	for artist in artists:
		links.append(get_links(artist))

	links = list(itertools.chain(*links))

	#store lyrics in a string
	for link in links:
		lyrics+=str(get_lyrics(link).encode('utf-8'))
		
	with open('lyrics.txt','a') as the_file:
		the_file.write(lyrics)
