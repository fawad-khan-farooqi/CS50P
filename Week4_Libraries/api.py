# Sending an HTTP GET request to a REST API and processing its JSON response.
import requests

def main():
    try:
        # Send a GET request to the Art Institute of Chicago API.
        # Search for artworks related to the keyword "Monet".
        response = requests.get(
            "https://api.artic.edu/api/v1/artworks/search",
            {"q": "Monet"}
        )

        # Raise an HTTPError if the server returns an error
        # (e.g., 404 Not Found, 500 Internal Server Error).
        response.raise_for_status()

    except requests.HTTPError:
        print("Couldn't complete the request.")
        return

    # Convert the JSON response into a Python dictionary.
    content = response.json()

    # The API stores the search results under the "data" key.
    # Iterate through each artwork and print its title.
    for artwork in content["data"]:
        print(artwork["title"])


main()

# Common HTTP Status Codes:
# 200 -> OK (Request successful)
# 400 -> Bad Request (Invalid request from the client)
# 403 -> Forbidden (Permission denied)
# 404 -> Not Found (Resource does not exist)
# 500 -> Internal Server Error (Problem on the server)
