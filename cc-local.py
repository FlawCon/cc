import json
import requests

room = "Room 1" # Room Name
#frab = "https://timetable.flawcon.xyz/2019/schedule/export/schedule.json" # Timetable/Schedule URL

# read file
with open('schedule.json', 'r') as myfile:
    data=myfile.read()

sched = json.loads(data)["schedule"]["conference"]["days"][0]["rooms"]
#sched = requests.get(frab).json()["schedule"]["conference"]["days"][0]["rooms"]

z = ""

for i in sched[room]:
    if i["do_not_record"] == False:
        print("From-until	" + i["title"])

        if len(i["persons"]) == 1:
            for y in i["persons"]:
                z = z + y["name"]
        elif len(i["persons"]) > 1:
            for y in i["persons"][:-1]:
               z = z + y["name"] + ", "
            z = z + i["persons"][len(i["persons"])-1]["name"]
        else:
            print("Error")

        print("From-until	- " + z)
        z = ""