from bs4 import BeautifulSoup
import requests
import json

#r = requests.get(r"https://smiletutor-carlos.appspot.com/public/v2/tuition_assignments/0")
#r_json = r.json()
#
#with open("temp.json", "w") as f:
#    json.dump(r_json, f)

with open("smiletutor.json") as f:
    r_json = json.load(f)

site_listings = r_json["data"]



