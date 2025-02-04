import requests
from send_email import send_gmail

api_key = "cfad61882db14a25bf9d7859f085ebeb"
url = "https://newsapi.org/v2/everything?q=tesla" \
      "&from=2025-01-04&sortBy=publishedAt&apiKey=" \
      "cfad61882db14a25bf9d7859f085ebeb"

#Make request
request = requests.get(url)

#Get a dictionary with data
content = request.json()

#Access the article titles and description
body = ""
for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + article["description"] + 2*"\n"

body = body.encode("utf-8")
send_gmail(message=body)