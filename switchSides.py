import urllib.request, json

def sideWithWinners():

    #run through json and count peace vs revolution
    url = "https://mygeoangelfirespace.city/db/votes.json"

    response = urllib.request.urlopen(url)

    data = json.loads(response.read())

    #Search through JSON to get zanussbot streetcred

    votes = data['votes']

    lengthofdata = len(votes)

    peace = 0

    rev = 0

    #print(lengthofdata)

    #print(votes['1'])

    for i in range(1,lengthofdata+1):
        vote = (votes[f'{i}']['vote'])
        print(vote)
        if(vote == 'peace'):
            peace = peace +1
        if(vote == 'revolution'):
            rev = rev +1

    

    print("Peace: "+ str(peace))

    print("Revolution: "+ str(rev))

    if(rev > peace):
        majority = "revolution"
        
    
    if(peace > rev):
        majority = "peace"


    if(peace == rev):
        majority = "revolution"

    return majority