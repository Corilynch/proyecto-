import urllib.request

import urllib.request
import json

def fetch_json_from_api(url):
  """Fetches JSON data from an API and returns a Python dictionary.

  Args:
      url: The URL of the API endpoint.

  Returns:
      A Python dictionary representing the parsed JSON data, 
      or None if there's an error.
  """

  try:
    response = urllib.request.urlopen(url)
    content = response.read().decode('utf-8')
    data = json.loads(content)
    return data
  except (urllib.error.URLError, json.JSONDecodeError) as e:
    print(f"Error fetching or parsing JSON data: {e}")
    return None

# Example usage
api_url = 'https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/users.json'
  # Replace with the actual API URL
json_data = fetch_json_from_api(api_url)

if json_data:
  print(json_data)  # Access data using dictionary keys
else:
  print("Failed to fetch JSON data.")
