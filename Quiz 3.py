# import requests
# import json
# import sqlite3

# payload = "head"
# URL = f"https://mugenmonkey.com/api/v0/ds3_builds?{payload}"
# ans = requests.get(URL)
# ans2 = ans.json()
# print(ans.text)
# print(ans.status_code)
# print(ans.headers)
#
# with open("file.json", "w") as file:
#     json.dump(ans2, file, indent=4)

# print(ans2["ds3_builds"][])

# for each in ans2["ds3_builds"]:
#     print(ans2["ds3_builds"][each]["covenant"] + ", " + ans2["ds3_builds"][each]["id"])

# con = sqlite3.connect("DarkSouls.sqlite")
# c = con.cursor()

# c.execute('''CREATE TABLE IF NOT EXISTS game
#                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 covenant VARCHAR(70),
#                 title VARCHAR(70),
#                 starting_class VARCHAR(70))
# ''')

# information = []

# for x in ans2["ds3_builds"]:
#     covenant = ans2["ds3_builds"][x]["covenant"]
#     title = ans2["ds3_builds"][x]["title"]
#     starting_class = ans2["ds3_builds"][x]["starting_class"]
#     info = [covenant, title, starting_class]
#     information.append(info)

# c.executemany('''INSERT INTO game (covenant, title, starting_class)
#                       VALUES (?,?,?)''', information)

# con.commit()
# con.close()
