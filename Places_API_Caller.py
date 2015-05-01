import requests
import json

key = "AIzaSyCF2NpnG7EJ0L1nedriD92ZnVaOtz5Ankw"


with open('keywords.txt', 'r') as f:
	with open('output_locations.txt', 'w') as output_file:	
		for word in f:
			keyword = word
			url = "https://maps.googleapis.com/maps/api/place/textsearch/json?query=" +  keyword + "&"  +"key=" + key
			print url
			response = requests.get(url).text
			output = json.loads(response)
			output_file.write(str(output))
			try:
				output_file.write(output['results'])
			except UnicodeEncodeError:
				print "boooooo unicodes suxxxxx"



