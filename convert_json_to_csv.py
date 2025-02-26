import pandas as pd
import json

def json_to_csv(json_file, csv_file):
    # Load JSON data
    with open(json_file, 'r') as file:
        data = json.load(file)
    
    # Extract the records list
    records = data.get("records", [])  # Safely get the list, default to empty list if missing
    # Convert JSON to DataFrame
    df = pd.DataFrame(records)
    
    # Save DataFrame to CSV
    df.to_csv(csv_file, index=False)
    print(f"Successfully converted {json_file} to {csv_file}")

# Example usage
json_to_csv('planit-output.json', 'planit-output.csv')
