def whosSalty(message):

    #get tagged user from message
    user = message.split('!!salt')
    user = user[1]
    return user