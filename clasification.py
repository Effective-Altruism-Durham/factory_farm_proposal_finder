import ollama
import pandas as pd


df = pd.read_csv("planit-output.csv")

# Define a function to check if the description indicates a factory farm
def is_factory_farm(description):
    if pd.isna(description):  # Handle NaN values
        return False
    message = [{"role": "user", "content": 'Answer with either 0 or 1! Does this seem related to a factory farm?  """'+description+'"""'}]
    response = ollama.chat(model="gemma:2b-instruct-q4_0", messages=message)
    print(response["message"], "👾", message)
    result = None
    if "1" in response["message"]["content"] or "yes" in response["message"]["content"].lower():
        result = True
    elif "0" in response["message"]["content"] or "no" in response["message"]["content"].lower():
        result = False
    else:
        print("Invalid response received")
        result = None
    return result

# Create a new column 'Factory farm' with boolean values
df["Factory farm"] = df["description"].apply(is_factory_farm)

# Save the modified DataFrame if needed
df.to_csv("updated_file.csv", index=False)

# Print the first few rows for verification
print(df.head())
