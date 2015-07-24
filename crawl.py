#import pygoogle
#import urllib2
#from fake_useragent import UserAgent
from xgoogle.search import GoogleSearch, SearchError
import time
import random

search_query = []
search_query_one = []

search = ["minorities summer programs"]
                        # "girl summer camp high school",
                        # "native american summer camp high school",
                        # "high school summer day camp"]

states = ["alabama",
                  "alaska",
                  "arizona",
                  "arkansas",
                  "california",
                  "colorado",
                  "connecticut",
                  "delaware",
                  "florida",
                  "georgia",
                  "hawaii",
                  "idaho",
                  "illinois",
                  "indiana",
                  "iowa",
                  "kansas",
                  "kentucky",
                  "louisiana",
                  "maine",
                  "maryland",
                  "massachusetts",
                  "michigan",
                  "minnesota",
                  "mississippi",
                  "missouri",
                  "montana",
                  "nebraska",
                  "nevada",
                  "new hampshire",
                  "new jersey",
                  "new mexico",
                  "new york",
                  "north carolina",
                  "north dakota",
                  "ohio",
                  "oklahoma",
                  "oregon",
                  "pennsylvania",
                  "rhode island",
                  "south carolina",
                  "south dakota",
                  "tennessee",
                  "texas",
                  "utah",
                  "vermont",
                  "virginia",
                  "washington",
                  "west virginia",
                  "wisconsin",
                  "wyoming",
                  "washington dc",
                  "guam",
                  "puerto rico"]

categories = ["architecture",
                      "business",
                      "computer science",
                      "creative writing",
                      "criminal justice",
                      "debate",
                      "engineering",
                      "international",
                      "journalism",
                      "law",
                      "leadership",
                      "math",
                      "medicine",
                      "music",
                      "outdoor",
                      "science",
                      "visual and performing arts"]

for i in range(len(states)):
	search_query.append(search[0] + " " + states[i])

for i in range(len(search_query)):
	for j in range(len(categories)):
		search_query_one.append(categories[j] + " " + search_query[i])

# print search_query_one

# ua = UserAgent()

# query = urllib2.Request('https://www.google.com/#q=p' + search_query_one[0])
# query.add_header[('User-agent', ua.random)]
# print query

# result = urllib2.urlopen(query)

# print result.geturl()

link = open('search_query_one_links.txt', 'w')

for query in range(len(search_query_one)):
	try:
		search = GoogleSearch(search_query_one[query])
		search.results_per_page = 90
		results = search.get_results()
		for res in results:
			print res.url.encode("utf8")
			link.write(res.url.encode("utf8") + '\n')
	except SearchError, e:
		print "Search failed: %s" % e
	time.sleep(random.randint(10,25))




# print states
# print categories
# print search_query_one