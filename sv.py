import requests

# Function to get data from the API using NID and DOB
def get_nid_data(nid, dob):
    # Base API URL
    url = 'https://rnf.nsmodz.top/server.php'

    # API key (assumed from the URL you provided)
    api_key = 'rafiz'

    # Parameters to be sent in the API request
    params = {
        'key': api_key,
        'nid': nid,
        'dob': dob
    }

    # Send GET request to the API
    response = requests.get(url, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        # Print the API response
        print("Response Data:")
        print(response.json())
    else:
        # Print the error message
        print(f"Failed to fetch data. Status code: {response.status_code}")

# Main function to get input from the user
if __name__ == '__main__':
    nid = input("Enter NID: ")
    dob = input("Enter DOB (YYYY-MM-DD): ")

    # Call the function to fetch and display data
    get_nid_data(nid, dob)