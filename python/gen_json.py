import json
import IUCAASports as iu
from manage import badminton

data ={"events":badminton.GetDict()}

# JSONPATH = r"C:\Users\ranit\OneDrive\My Drive\7 GitHub\Organisations\ranit-web\IUCAA-Sports\data.json"
JSONPATH = r"/home/ranit/MyDrive/IUCAA-Sports/data.json"
with open(JSONPATH,"w") as json_file:
    json.dump(data, json_file, indent=4)

