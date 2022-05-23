import navigator
import os

BINARYEDGE_API_KEY = os.getenv('BINARYEDGE_API_KEY')
URL_API = 'https://api.binaryedge.io/v2/query/domains/subdomain/{0}'
DOMAINS_LIST = []


def returnDomains(domain):
    req = navigator.Navigator()
    json = req.downloadResponse(URL_API.format(domain), 'JSON', 'GET', header={'X-Key': BINARYEDGE_API_KEY})
    try:
        for _ in json['events']:
            DOMAINS_LIST.append(_)
        req.ModuleLoaded('binaryedge.io', DOMAINS_LIST)
        return DOMAINS_LIST
    except:
        return []
