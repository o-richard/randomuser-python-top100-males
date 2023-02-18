import requests
from tabulate import tabulate

# Randomuser.me URL
URL = "https://randomuser.me/api/"

# Specify parameters
params = {
    "results": 100,
    "gender": "male",
    "inc": "name,location,email,dob,phone,cell,nat",
}

response = requests.get(URL, params=params)

print(
    """
  ____ _____  _    ____ _____ 
 / ___|_   _|/ \  |  _ \_   _|
 \___ \ | | / _ \ | |_) || |  
  ___) || |/ ___ \|  _ < | |  
 |____/ |_/_/   \_\_| \_\|_|  
                              
    """
)

# Succesful request
if response.status_code == 200:
    data = response.json()
    results = data["results"]
    table_data = []

    for r in results:
        flattened_results = [
            r["name"]["title"],
            r["name"]["first"],
            r["name"]["last"],
            r["location"]["country"],
            r["email"],
            r["dob"]["age"],
            r["phone"],
            r["cell"],
            r["nat"],
        ]
        table_data.append(flattened_results)

    # Convert the dictionary to a list of tuples

    # Display the data in a table
    headers = [
        "Title",
        "First Name",
        "Last Name",
        "Country",
        "Email",
        "Age",
        "Phone",
        "Cell",
        "Nationality",
    ]
    print(tabulate(table_data, headers=headers, tablefmt="grid"))

# Unsucessful request
else:
    print("Error: Failed to get data from API.")

print(
    """
  _____ _   _ ____  
 | ____| \ | |  _ \ 
 |  _| |  \| | | | |
 | |___| |\  | |_| |
 |_____|_| \_|____/ 
                      
    """
)
