import requests
import json

key = "AIzaSyCF2NpnG7EJ0L1nedriD92ZnVaOtz5Ankw"


with open('keywords.txt', 'r') as f:
	with open('output_locations.txt', 'w') as output_file:
		for word in f:
			keyword = word
			#for y in range()
			url = "https://maps.googleapis.com/maps/api/place/radarsearch/json?location=40.7211,-73.9823&radius=50000&keyword=" +  keyword + "&"  +"key=" + key

			print url
			response = requests.get(url).text
			output = json.loads(response)

	
			for result in output['results']:
				output_file.write(str(result['geometry']['location']['lat']) + " , " + str(result['geometry']['location']['lng']) + "\n")
