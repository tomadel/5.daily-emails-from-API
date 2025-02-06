import requests
from send_email import send_gmail

topic = "tesla"

api_key = "cfad61882db14a25bf9d7859f085ebeb"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&from=" \
      "2025-01-06&sortBy=publishedAt&api" \
      "Key=cfad61882db14a25bf9d7859f085ebeb&" \
      "language=en"

#Make request
request = requests.get(url)

#Get a dictionary with data
content = request.json()
print(content)
#Access the article titles and description
body = ""
for article in content["articles"][:20]:
    title = article["title"] if article["title"] is not None else "No title"
    description = article["description"] if article["description"] is not None else "No description"
    url = article["url"] if article["url"] is not None else "No URL"
    subject = "Subject: Today's news"

    body = subject + "\n" + body + title + "\n" + description + "\n" + url + 2 * "\n"

body = body.encode("utf-8")
send_gmail(message=body)