import os
from dotenv import load_dotenv

import googleapiclient.discovery

load_dotenv()

# Set API key and region code
API_KEY = os.getenv("YOUTUBE_API_KEY")
REGION_CODE = "US"  # KR JP

# Create the service object
youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=API_KEY)

# Define the request parameters
request = youtube.videoCategories().list(part="snippet", regionCode=REGION_CODE)

# Execute the request
response = request.execute()

# Print category information
print("List of Video Categories (ID : Title):")
for item in response["items"]:
    print(f"- {item['id']} : {item['snippet']['title']}")
    
# Make list and return
def get_videoCategory():
    vid_cayegory = {}
    for item in response["items"]:
        vid_cayegory[item['id']] = item['snippet']['title']
    return vid_cayegory

### Result
# List of Video Categories (ID : Title):
# - 1 : Film & Animation
# - 2 : Autos & Vehicles
# - 10 : Music
# - 15 : Pets & Animals
# - 17 : Sports
# - 18 : Short Movies
# - 19 : Travel & Events
# - 20 : Gaming
# - 21 : Videoblogging
# - 22 : People & Blogs
# - 23 : Comedy
# - 24 : Entertainment
# - 25 : News & Politics
# - 26 : Howto & Style
# - 27 : Education
# - 28 : Science & Technology
# - 29 : Nonprofits & Activism
# - 30 : Movies
# - 31 : Anime/Animation
# - 32 : Action/Adventure
# - 33 : Classics
# - 34 : Comedy
# - 35 : Documentary
# - 36 : Drama
# - 37 : Family
# - 38 : Foreign
# - 39 : Horror
# - 40 : Sci-Fi/Fantasy
# - 41 : Thriller
# - 42 : Shorts
# - 43 : Shows
# - 44 : Trailers

### Res sample
# {
#     "kind": "youtube#videoCategoryListResponse",
#     "etag": "fIIv2-q7-AkaOeJf0LPrlnu-0As",
#     "items": [
#         {
#             "kind": "youtube#videoCategory",
#             "etag": "grPOPYEUUZN3ltuDUGEWlrTR90U",
#             "id": "1",
#             "snippet": {
#                 "title": "Film & Animation",
#                 "assignable": true,
#                 "channelId": "UCBR8-60-B28hp2BmDPdntcQ"
#             }
#         },
#         {...}
#     ]
# }
