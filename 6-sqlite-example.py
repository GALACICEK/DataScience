import sqlite3
import random

def random_int():
    return(random.randint(1, 100))

def get_acolor(cursor,list_eleman):
    cursor.execute("CREATE TABLE IF NOT EXISTS translates (en_color text, tr_color text)")
    # For a row
    cursor.execute("INSERT INTO translates VALUES (?,?)", list_eleman)
    cursor.execute("SELECT * FROM translates WHERE en_color=:c", {"c": list_eleman[0]})
    #Getting execution list
    translate_search = cursor.fetchall()  
    #print(translate_search)

    cursor.execute("SELECT * FROM fruits WHERE color=:c", {"c": list_eleman[0]})
    color_search = cursor.fetchall()

    # manipulate database 
    qs=[]
    for data in color_search:
        qs.append([translate_search[0][1] if value==translate_search[0][0] else value for value in data])

    return qs

def get_translate_colors(cursor, tr_list):
    cursor.execute("CREATE TABLE IF NOT EXISTS translates (en_color text, tr_color text)")
    cursor.executemany("INSERT INTO translates VALUES (?,?)", tr_list) 

    cursor.execute("""SELECT fruits.*, translates.tr_color
                          FROM fruits
                          INNER JOIN translates ON fruits.color = translates.en_color""")
    
    translate_search = cursor.fetchall()
 
    
    qs=[]
    for row in translate_search:
        qs.append(row)

    return qs


##---------------------------------------------------------------------------------------------------------------------------

my_list = [
    (random_int(), "apple", "red"),
    (random_int(), "banana", "yellow"),
    (random_int(), "cherry", "red"),
    (random_int(), "date", "brown"),
    (random_int(), "grape", "purple"),
    (random_int(), "kiwi", "brown"),
    (random_int(), "lemon", "yellow"),
    (random_int(), "orange", "orange"),
    (random_int(), "pear", "green"),
    (random_int(), "watermelon", "green")
]

# create connection
connection = sqlite3.connect("fruits.db")

# create cursor object
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS fruits  (amount interger, fruit text, color text)")

# insert data to table
cursor.executemany("INSERT INTO fruits VALUES (?,?,?)", my_list)

# print database rows
for row in cursor.execute("SELECT * FROM fruits"):
    print(row)

print("\n")

# print spesific rows
cursor.execute("SELECT * FROM fruits WHERE color=:c", {"c": "green"})
color_search = cursor.fetchall()
print(color_search)
print("\n")

# new table
translate_list =[
    ("red", "kırmızı"),
    ("yellow", "sarı"),
    ("brown", "kahverengi"),
    ("purple", "mor"),
    ("orange", "turuncu"),
    ("green", "yeşil")
]

translate_search = get_acolor(cursor,translate_list[-1])
print("\n")
print(translate_search)



colors_translate_list= get_translate_colors(cursor, translate_list)
print("\n")
print(colors_translate_list)


connection.commit()

connection.close()
