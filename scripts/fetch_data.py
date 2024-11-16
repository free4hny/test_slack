import requests
import pandas as pd

def fetch_and_save_to_excel(api_url, output_file):
    # Fetch data from the API
    response = requests.get(api_url)
    
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()  # Convert the response to JSON
        
        # Convert the JSON data into a Pandas DataFrame
        df = pd.DataFrame(data)
        
        # Save the DataFrame to an Excel file
        df.to_excel(output_file, index=False)
        print(f"Data successfully written to {output_file}")
    else:
        print(f"Failed to fetch data. HTTP Status code: {response.status_code}")
        print(f"Data successfully written to this path: {!pwd}")

if __name__ == "__main__":
    # Define the API URL and the output Excel file
    api_url = "https://jsonplaceholder.typicode.com/posts"
    output_file = "posts_data.xlsx"
    
    # Fetch the data and save it to an Excel file
    fetch_and_save_to_excel(api_url, output_file)
