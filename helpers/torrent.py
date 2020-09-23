import requests

def torrent_search(torrent_name):
    base_url =f"https://1337x.to/usearch={torrent_name}"
    request = requests.get(base_url)
    if (request.s



