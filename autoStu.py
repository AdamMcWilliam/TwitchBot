import os
import requests
import requests.auth

client_id = os.environ['REDDIT_CLIENT_ID']
client_secret = os.environ['REDDIT_CLIENT_SECRET']
username = os.environ['REDDIT_BOT_USER']
password = os.environ['REDDIT_BOT_PASS']

def keeboftheday():
    client_auth = requests.auth.HTTPBasicAuth(client_id, client_secret)

    post_data = {"grant_type": "password",
    "username": f"{username}",
    "password": f"{password}"}

    headers = {"User-Agent": "ChangeMeClient/0.1 by zanussbot"}
    response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)
    result = response.json()
    ##print(result)

    token = result['access_token']

    headers = {"Authorization": f"bearer {token}", "User-Agent": "ChangeMeClient/0.1 by zanussbot"}
    response = requests.get("https://oauth.reddit.com/r/MechanicalKeyboards/hot/.json?limit=3", headers=headers)
    ##print(response.json())
    response = response.json()

    #need to go in data -> children -> find image
    url = response['data']['children'][2]['data']['preview']['images'][0]['source']['url']

    #fix URL
    url = url.replace("&amp;", "&")
    print(url)
    #https://preview.redd.it/w0d9rgn55ut51.jpg?width=960&crop=smart&auto=webp&s=3d2d98b948e803fc80f5da16c7c310b7e62d9c3a
    return url