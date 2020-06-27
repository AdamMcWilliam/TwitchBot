import urllib.request, json


def getBotStreet():
    #search through https://mygeoangelfirespace.city/db/users.json

    url = "https://mygeoangelfirespace.city/db/users.json"

    response = urllib.request.urlopen(url)

    data = json.loads(response.read())

    #Search through JSON to get zanussbot streetcred

    data = data['users']['663']['street_cred']
    
    return json.dumps(data, indent = 4)


