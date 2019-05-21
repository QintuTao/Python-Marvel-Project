# User will be able to checkout any characters, events and comics by using this programm

from marvel import Marvel

# Get both keys from my personal account ---- Roederor
PUBLIC_KEY = "75f9ed43f23271b39b0257e422c150b3"
PRIVATE_KEY = "068e03d27a588b3a806e9201f539ca81a92d31c5"

# Fetch Data from Marvel Database
marvel = Marvel(PUBLIC_KEY,PRIVATE_KEY)

# Get specific data from the request results
characters = marvel.characters
comics = marvel.comics
series = marvel.series
creator = marvel.creators
stories = marvel.stories
events = marvel.events

# Get the total number of each types of request
total = [
    characters.all()['data']['total'],
    events.all()['data']['total'],
    stories.all()['data']['total'],
    series.all()['data']['total'],
]

# The introduction fuction
def printIntro():
    print(f"Hello, Dear User,\n"
          f"    Welcome to the Simple Python Marvel Software.\n"
          f"    You can look up anything in the {total[3]}, including {total[2]} stories with {total[1]} events and {total[0]} characters!\n")
    print('''
------------------------------------------------------------------------------------------------------
Please Enter The Hero You Are Looking for. If you need help, please enter "help" (without quotation marks)
    ''')

# the questioning function
def ask(ask_num:int):
    user_input = []
    for i in range(ask_num):
        user_input.append(input().lower())
    return user_input

if __name__ == '__main__':
    #Introduction
    printIntro()



