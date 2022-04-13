import re
import requests
import json

def jsons_response(url):
    '''
    Python project to read public data returned from URL, and parsing JSON to a
    dictionary object
    '''
    return requests.get(url)


def to_json(data):
    '''
    parsing JSON to a dictionary object
    '''
    #rr = requests.get('https://api.openalex.org/authors')
    return json.loads(data.text)
    
json_store=jsons_response('https://api.openalex.org/authors')
print(to_json(json_store)['meta'])