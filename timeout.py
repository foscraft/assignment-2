import requests
import json


def time_out_response():
    '''
    Python program to send a timed request to a web page
    ''' 
    k = list(range(1,2))
    for j in k:
        rr = requests.get(f'https://api.openalex.org/authors?per-page=100&page={j}',timeout=0.05)
        return json.loads(rr.content)
        #return json.loads(rr.text)

#invoke function
print(time_out_response())