import requests
import pandas as pd
import os



# Fetch data from an API
api_url = "https://jsonplaceholder.typicode.com/posts"  # Replace with actual API URL
response = requests.get(api_url)

if response.status_code == 200:
    data = response.json()
    # Convert the JSON data into a DataFrame
    df = pd.DataFrame(data)
    
    # Save DataFrame to Excel
    df.to_excel(output_file, index=False)
    print(f"Excel file created: {output_file}")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")

# if __name__ == "__main__":
# input_file = "input_file.txt"
# output_file = "output_data.xlsx"

