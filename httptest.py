import json

import requests




# funcs
def get_data() -> (int | requests.Response | str):
    link = input("Provide a url: ")
    if link.find("https://") < 0:
        print("'htts://' prefix was NOT found... restarting.")
        return get_data()

    return requests.get(link, auth=("user", "pass"))

def write_file(data: str):
    with open("result.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

# FRONTEND
result = get_data()
if type(result) == requests.Response:
    write_file(result.json())
    print("url saved to file.")
