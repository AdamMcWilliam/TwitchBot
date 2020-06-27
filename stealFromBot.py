

def StealFromBot(message, theif):

    #opsecbot !steal cacheisking rigged2

    #if message starts with !steal
    if(message.startswith('!steal')):
        #split message into parts
        split = message.split(' ')
        
        command = split[2]

        stealmessage = theif + " " + command
        
        return stealmessage
    