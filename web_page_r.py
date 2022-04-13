import requests
import json
'''
Python program to send a request to a web page, and print the response text
and content
'''

def ids_open_dict():
    '''
    This function returns a list of all authorships and orcid ids in OpenAlex.
    ''' 
    k = list(range(1,2))
    for j in k:
        rr = requests.get(f'https://api.openalex.org/authors?per-page=100&page={j}')
        return json.loads(rr.content)
        #return json.loads(rr.text)

#invoke function
print(ids_open_dict())
