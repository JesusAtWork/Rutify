import urllib.request
import json

def rutify(query):
    query = query.replace(" ","%20")
    url = 'https://api.rutify.cl/search?q='+query
    with urllib.request.urlopen(url) as response:
        return response.read()
