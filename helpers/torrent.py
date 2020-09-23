import requests

def torrent_search(torrent_name):
    base_url = "https://kickasstorrents.to/usearch/"
    request = requests.get(base_url)
    if (request.status_code == 200):
        response = request.json()
        return response
    return None
