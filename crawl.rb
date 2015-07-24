require 'rubygems'
require 'google-search'

search = ["minorities summer programs"]

search_query = []
search_query_one = []

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

states.each do |state|
	search_query.push(search[0] + " " + state)
end

search_query.each do |query|
	categories.each do |category|
		search_query_one.push(category + " " + query)
	end
end

f = File.new("results.txt", "w+")

# puts search_query_one[320]

search_query_one.each do |term|
	sleep(rand(10..20))
	Google::Search::Web.new(query: term).each do |link|
		puts link.uri
		puts term
		f.puts(link.uri)
	end
end

# Google::Search::Web.new(query: search_query_one[320]).each do |link|
# 	f.puts(link.uri)
# end
# puts example
#sleep(rand(9..20))