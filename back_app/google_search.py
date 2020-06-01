import json
from urllib.parse import urlencode

import requests
import settings


def get_results(keyword):

    url = "https://google-search3.p.rapidapi.com/api/v1/search"

    querystring = {"country": "Nepal", "language": "lang_en", "max_results": "100",
                   "uule": "w%2BCAIQICIbSG91c3RvbixUZXhhcyxVbml0ZWQgU3RhdGVz", "hl": "us",
                   "q": keyword}

    headers = {
        'x-rapidapi-host': "google-search3.p.rapidapi.com",
        'x-rapidapi-key': settings.GOOGLE_API_KEY
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    results = json.loads(response.text)
    count = len(results)
    return count
