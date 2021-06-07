import requests

refresh_token = "AQDkMuj2pjh-mDCCoRszp7lj8BadzF3h9Y74sAJ09aIy387bC5BG89bT8p3XHS7Dpffp5MKBUWiJbtkq74lATYdeq3kM0TxpEmoEzKEBUC2gliUNap3TUC5FqbFJDSWrr98"
base_64_encoded_client_creds = "YmFmYjBhOTIzYjc2NDhlOWJkNWMyMTQzYzhkYzQzZjI6MmVlYTk1OGM4MjE4NDU0NWI5OThlMTk3NDExNGRjYjE="

def refresh_code():
    query = "https://accounts.spotify.com/api/token"
    response = requests.post(
        query,
        data = {
                "grant_type": "refresh_token",
                "refresh_token": refresh_token
        },
        
        headers = {
                "Authorization": "Basic " + base_64_encoded_client_creds
        }
    )

    response_json = response.json()
    return response_json["access_token"]
