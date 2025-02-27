import requests
import feedparser

# Define the URL of the Armadale Library RSS feed (if available)
rss_url = "https://library.armadale.wa.gov.au/rss.xml"  # Replace with the actual RSS feed URL if available

# Fetch the RSS feed
response = requests.get(rss_url)

if response.status_code == 200:
    feed = feedparser.parse(response.content)

    # Print feed title
    print(f"Feed Title: {feed.feed.title}")

    # Loop through the first 5 entries
    for entry in feed.entries[:5]:
        print(f"\nTitle: {entry.title}")
        print(f"Link: {entry.link}")
        print(f"Published: {entry.published}")
else:
    print(f"Failed to fetch RSS feed. Status Code: {response.status_code}")

