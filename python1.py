import urllib

urls=["https://www.gsaadvantage.gov/advantage/main/start_page.do","https://www.gsaadvantage.gov/advantage/s/search.do?db=0&q=0%3A2S-133R&searchType=0&s=8"]

i=0

while i<len(urls):
	htmlfile=urllib.urlopen(urls[i])
	htmltext=htmlfile.read()
	print htmltext
	i+=1