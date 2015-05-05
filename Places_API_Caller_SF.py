import requests
import json

key = "AIzaSyCF2NpnG7EJ0L1nedriD92ZnVaOtz5Ankw"


with open('keywords.txt', 'r') as f:
	with open('output_locations.txt', 'w') as output_file:
		for word in f:
			keyword = word
			#for y in range()
			url = "https://maps.googleapis.com/maps/api/place/textsearch/json?location=37.757632, -122.447385&radius=10000&query=" +  keyword + "&"  +"key=" + key

			print keyword
			response = requests.get(url).text
			output = json.loads(response)


			for result in output['results']:
				output_file.write(str(result['geometry']['location']['lat']) + " , " + str(result['geometry']['location']['lng']) + "\n")
