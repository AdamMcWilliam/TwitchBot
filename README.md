# TwitchBot
Python Twitch bot created with twitchio for use in BeginWorld @ https://twitch.tv/beginbot

Resources Used:

Base setup following this tutorial: https://dev.to/ninjabunny9000/let-s-make-a-twitch-bot-with-python-2nd8 

Using Python 3.7: https://www.python.org/downloads/release/python-370/

Google Spreadsheets API: https://developers.google.com/sheets/api/quickstart/python

You need to download and add credentials.json file from google and add to the working directory.


Commands: 

! is what the bot expects for a command, I use an addtional ! in my custom commands to avoid bot confusion resulting in most commands being !!COMMANDS. I designed it this way as there is one command my bot watches for that is by another bot using only one !.

!!manifestozanussbot
 - Outputs description of bot.

!!botcss
 - Updates the css of the bot with link hardcoded.

!!propsme
 - Outputs !props and the user who entered the command.

!!csstemplate
 - Links a helpful css template for other users in BeginWorld.

!!donateme
 - Outputs !donate and the user who entered the command.

!!propsall
 - Outputs !props and the user who entered the command and the total streetcred that the bot currently has.

!!buyall
 - The bot buys everything it can with !buy random and the total streetcred that the bot currently has.

!la_libre
 - When anyone runs this command the bot will find the winning side and vote for it.

!cubed
 - If beginbotbot uses this command the time is captured along with the timestamp of the message and is sent to be stored in a google spreadsheet.

!!act
 - Pulls data from a specific cell in the google spreadsheet

!!dact
 - Searches spreadsheet for all results of cube times on current day and calculates an average.

!!grovel
 - gives a use a point after 2 attempts, attempts logged in a created json file.


The live google spreadsheet in question: https://docs.google.com/spreadsheets/d/1fR7O9sgzjfrYCJN2ITZzFYjHiSQUUf_DkuxsfbutZms/edit?usp=sharing






