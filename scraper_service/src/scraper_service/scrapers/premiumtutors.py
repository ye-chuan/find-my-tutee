import requests
import json

r = requests.get(r"https://admin.premiumtutors.sg/api/assignments")
r_json = r.json()

with open("premiumtutors.json", "w") as f:
    json.dump(r_json, f)
