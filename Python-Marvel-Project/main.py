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
story = marvel.stories
events = marvel.events


if __name__ == '__main__':
    print(comics.all())