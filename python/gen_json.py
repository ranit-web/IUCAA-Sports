import json
import IUCAASports
from manage import events

events:list[IUCAASports.SportsEvent]
events = [ev.GetDict() for ev in events]
data ={"events":events}

JSONPATH = r"C:\Users\ranit\OneDrive\My Drive\7 GitHub\Organisations\ranit-web\IUCAA-Sports\data.json"
with open(JSONPATH,"w") as json_file:
    json.dump(data, json_file,indent=4)

