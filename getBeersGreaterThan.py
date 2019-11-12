import json
import requests
import sys

url = 'https://api.punkapi.com/v2/beers'
file = '/tmp/brew-dog.json'
beer_dict = {}

if len(sys.argv) == 1:
	print "Missing argument!!!"
	print "Usage " + sys.argv[0] + " <value>"
	exit(1)

## Create a physical file of the json data
def get_data(file_path):
	request = requests.get(url)
	response = request.json()
	with open(file_path, 'w') as outfile:
            json.dump(response, outfile)

## You can hash out the function call once file has been generated, can easily paramatize this
## but skipping to avoid wasting time

get_data(file)

## Open newly generated json file
## Use built in json.load to convert to object
with open(file) as json_data:
	load = json.load(json_data)
	
## Original implementation to display name and abv, but the commented it out for sort
## Loop through JSON as it's an array of objects
## Convert sys.argv from string to int, or else the if condition won't work
## Setting keys to indivdual variables to avoid unicode formatting
	# for i in load:
	#     if i['abv'] > int(sys.argv[1]):	   
	#         name = i['name']
	#         abv = i['abv']
	#         print ("{},{}".format(name, abv))


## Just to show thought process, let's do the sorting bonus
## Looped through original json data, and appended to an empty array
## By doing this, I'm able to sort by value [1]
## We can use reverse=True to sort by descending
 	for i in load:
	    if i['abv'] > int(sys.argv[1]):
	    	name = i['name']
	        abv = i['abv']
	        beer_dict[name] = abv

for key,value in sorted(beer_dict.items(), key=lambda item: item[1]):
	print ("%s: %s" % (key, value))
