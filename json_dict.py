import re
import requests
import json

def jsonsResponse():
    '''
    Python project to read public data returned from URL, and parsing JSON to a
    dictionary object
    '''
    return requests.get('https://api.openalex.org/authors')


def toJson():
    '''
    parsing JSON to a dictionary object
    '''
    rr = requests.get('https://api.openalex.org/authors')
    data = json.loads(rr.text)
    return [{"open_alex_id": i['id'], 
                "display_name": i['display_name'], 
                "orcid_id": i['orcid'], "works_count": i['works_count'],
                 "cited_by_count": i['cited_by_count'],
                  "institution_id": i['last_known_institution']['id'], 
                  "institution_name": i['last_known_institution']['display_name'],
                   "country_code": i['last_known_institution']['country_code'],
                    "institution_type": i['last_known_institution']['type']} for i in data['results']]

    #json.dump(lst,out_file,indent=2, sort_keys=True)
    

print(jsonsResponse())