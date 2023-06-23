import sqlite3, os, json

# read JSON file which is in the next parent folder
# file = os.path.abspath('/home/dem/Downloads/HEjson') + "/nutrient_names.json"
# file = os.path.abspath('/home/dem/Downloads/HEjson') + "/cooking_conditions_names.json"
file = os.path.abspath('/home/dem/Downloads/HEjson') + "/products.json"
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
# for i, item in enumerate(json_obj):
#     print(i, item, json_obj[item])
#     if i == 2:
#         break

    # cursor.execute(f"INSERT OR IGNORE INTO healthapp_cookingcondition (id, title) VALUES (?, ?)", (item,	json_obj[item]))
    # res = cursor.execute(f"SELECT * FROM healthapp_cookingcondition WHERE id = {item}")
    # df = res.fetchone()
    # print(df)


# fill productcategory
# category_set = set()
# ind = 1
# for i, item in enumerate(json_obj):
    # print(i, item, json_obj[item])
    # if i == 2:
    #     break
    # category_set.add(json_obj[item]['Категория'])

# for category in category_set:
    # cursor.execute(f"INSERT OR IGNORE INTO healthapp_productcategory (id, title) VALUES (?, ?)", (ind,	category))

#     res = cursor.execute(f"SELECT * FROM healthapp_productcategory WHERE id = {ind}")
#     df = res.fetchone()
#     print(df)
#     ind += 1
# print(category_set)

# fill source
# source_set = set()
# ind = 1
# for i, item in enumerate(json_obj):
#     # print(i, item, json_obj[item])
#     # if i == 2:
#     #     break
#     source_set.add(json_obj[item]['Источник'])
#
# for source in source_set:
#     # cursor.execute(f"INSERT OR IGNORE INTO healthapp_source (id, title) VALUES (?, ?)", (ind,	source))
#
#     res = cursor.execute(f"SELECT * FROM healthapp_source WHERE id = {ind}")
#     df = res.fetchone()
#     print(df)
#     ind += 1
# print(source_set)

# fill product
for i, item in enumerate(json_obj):
#     print(i, item, json_obj[item])
    # if i == 2:
    #     break
    category_id = cursor.execute(f"SELECT id FROM healthapp_productcategory WHERE title = (?)", (json_obj[item]['Категория'],))
    ci = category_id.fetchone()
    source_id = cursor.execute(f"SELECT id FROM healthapp_source WHERE title = (?)", (json_obj[item]['Источник'],))
    si = source_id.fetchone()
    cursor.execute(f"INSERT INTO healthapp_product (id, title, product_category_id, source_id) VALUES (?, ?, ?, ?)", (item,	json_obj[item]["Название"], ci[0], si[0]))

    # res = cursor.execute(f"SELECT * FROM healthapp_product WHERE id = {item}")
    # df = res.fetchone()
    # print(df[0])




# cursor.execute(f"DELETE FROM healthapp_product")
con.commit()
con.close()