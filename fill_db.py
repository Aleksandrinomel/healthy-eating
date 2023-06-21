import sqlite3, os, json

# read JSON file which is in the next parent folder
# file = os.path.abspath('/home/dem/Downloads/HEjson') + "/nutrient_names.json"
file = os.path.abspath('/home/dem/Downloads/HEjson') + "/cooking_conditions_names.json"
json_data = open(file).read()
json_obj = json.loads(json_data)


# do validation and checks before insert
# def validate_string(val):
#    if val != None:
#         if type(val) is int:
#             #for x in val:
#             #   print(x)
#             return str(val).encode('utf-8')
#         else:
#             return val


# connect to MySQL
con = sqlite3.connect("db.sqlite3")
cursor = con.cursor()


# fill nutrientname
# for i, item in enumerate(json_obj):
#     # print(i, item, json_obj[item][0])
#     # if i == 2:
#     #     break
#
#     # cursor.execute(f"INSERT OR IGNORE INTO healthapp_nutrientname (id, title) VALUES (?, ?)", (item,	json_obj[item][0]))
#     res = cursor.execute(f"SELECT * FROM healthapp_nutrientname WHERE id = {item}")
#     df = res.fetchone()
#     print(df)


# fill cookingcondition
for i, item in enumerate(json_obj):
    # print(i, item, json_obj[item])
    # if i == 2:
    #     break

    # cursor.execute(f"INSERT OR IGNORE INTO healthapp_cookingcondition (id, title) VALUES (?, ?)", (item,	json_obj[item]))
    res = cursor.execute(f"SELECT * FROM healthapp_cookingcondition WHERE id = {item}")
    df = res.fetchone()
    print(df)


# cursor.execute(f"DELETE FROM healthapp_cookingcondition")
con.commit()
con.close()