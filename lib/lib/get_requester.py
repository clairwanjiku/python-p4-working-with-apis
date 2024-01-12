import requests

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.text
        else:
            # Handle errors here if needed
            response.raise_for_status()

    def load_json(self):
        response_body = self.get_response_body()
        try:
            json_data = response_body.json()  # Assuming the response contains JSON data
            return json_data
        except ValueError as e:
            # Handle JSON decoding error here
            print(f"Error decoding JSON: {e}")
            return None

# Example usage:
url = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"
requester = GetRequester(url)

# Get the response body
response_body = requester.get_response_body()
print("Response Body:")
print(response_body)

# Load JSON data
json_data = requester.load_json()
print("\nJSON Data:")
print(json_data)
