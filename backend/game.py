import requests
'''
takes in a word 
'''
def validate(word):
    if len(word) < 5:
        return False

def getWords():
    url = "https://random-word-api.herokuapp.com/word?length=5&number=50" 
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        raise Exception(f'API Request Failed With Status{response.status_code}')

    