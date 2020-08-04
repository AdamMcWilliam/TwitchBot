import urllib.request, json


def insureBot():
    #search through https://mygeoangelfirespace.city/db/users.json

    url = "https://mygeoangelfirespace.city/db/users.json"

    response = urllib.request.urlopen(url)

    data = json.loads(response.read())

    #Search through JSON to get zanussbot streetcred

    #data = data['users']['663']
    # if("insured" in data):
    #     print("insured")
    #     return True
        
    # else:
    #     print("not insured")
    #     return False

    data = data['users']['663']['insured']
    
    if data == True:
        print("insured")
        return True
    else:
        print("not insured")
        return False
        