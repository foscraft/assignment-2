import requests
import json


def webPage_response():
    '''
    Python program to send a request to a web page, and print the response text
    and content
    ''' 
    k = list(range(1,2))
    for j in k:
        rr = requests.get(f'https://api.openalex.org/authors?per-page=100&page={j}')
        return json.loads(rr.content)
        #return json.loads(rr.text)

#invoke function
print(webPage_response())
