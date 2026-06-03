# With module (Writing a json file)

import json

data = {'Name': 'Nibras', 'Age': 18}
data["Grade"] = "A"

with open("Sample.json", "w") as file:
  
    json.dump(data, file, indent=4) # Dump is to add the data into the json file


# Reading a json file

with open("Sample.json", "r") as file:
    data = json.load(file)
    print(data)


