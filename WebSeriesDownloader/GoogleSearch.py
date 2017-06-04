from bs4 import BeautifulSoup as bs
import urllib2
import Hobby_codes.logger.logger as log
import re

class google:
	def __init__(self):
		self.season_no = None		#no of seasons to download
		self.series_name = None		#name of series to download
		self.no_of_episodes = None	#no episode to download
		self.soup = None
		self.urlutils = None
		self.hrefs = []
		self.dl_list = []
		self.log = log.log(r'C:\Results\webcrawler')

	def search(self,series_name):
		'''
		gives the search page of google
		:param series_name:
		:return:
		'''
		self.series_name = series_name
		search_query = 'index+of+'+self.series_name+'&ie=utf-8&oe=utf-8&client=firefox-b-ab'
		google_search_url = 'http://www.google.co.in/search?q='
		full_search_url = google_search_url+search_query
		# print full_search_url
		return self.send_search_request(full_search_url)

	def send_search_request(self,link):
		hdr = {'User-Agent': 'Mozilla/53.0.03'}
		req = urllib2.Request(link,headers=hdr)
		webobj = urllib2.urlopen(req)
		self.soup = bs(webobj,'lxml')
		#self.log.Info(self.soup)
		return self.get_dls()

	def get_dls(self):
		'''
		1. parse the page for hrefs
		2. get all the links which are dls
		note : links with dls are condsidered to be download links as of now(assumption)
		:return:
		'''
		httpurl = []
		localurl = []
		alla = self.soup.find_all('a')
		#self.print_links(alla)
		for linkattributes in alla:
			self.hrefs.append(linkattributes.get('href'))
		for http in self.hrefs:
			urls = re.findall("(?P<url>http?://[^\s]+)", http)
			if len(urls)>0:
				httpurl.append(urls[0])

		for links in httpurl:
			if '/dl' in links:
				#print links
				self.dl_list.append(links)
		print self.dl_list
		for i in self.dl_list:
			#print 'local url'
			print re.split(self.series_name, i, flags=re.IGNORECASE)[0]+self.series_name+'/'
		print localurl
		return self.dl_list

 	def Crawler(self,Parent_link):
		'''
		method suppose to give sitemap from the patent link
		:param Parent_link:
		:return:Not decided yet
		'''
		print 'in crawler'
		self.send_search_request(Parent_link)

	def print_links(self,link_list):
		'''
		prints all the links
		:param link_list:
		:return:
		'''
		print 'Printing list :'

		for link in link_list:
			print link

