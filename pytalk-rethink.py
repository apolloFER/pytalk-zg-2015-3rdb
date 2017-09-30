__author__ = 'darko.ronic'

# connect to rethinkdb

import rethinkdb as r
print r.connect(host="192.168.59.103", port=28015).repl()

# create a table

print r.db("test").table_create("authors").run()

# insert data

print r.table("authors").insert([
    {"name": "William Adama", "tv_show": "Battlestar Galactica",
     "posts": [{"title": "Decommissioning speech", "content": "The Cylon War is long over..."},
               {"title": "We are at war", "content": "Moments ago, this ship received..."},
               {"title": "The new Earth", "content": "The discoveries of the past few days..."}]
    },
    {"name": "Laura Roslin", "tv_show": "Battlestar Galactica",
     "posts": [{"title": "The oath of office", "content": "I, Laura Roslin, ..."},
               {"title": "They look like us", "content": "The Cylons have the ability..."}]
    },
    {"name": "Jean-Luc Picard", "tv_show": "Star Trek TNG",
     "posts": [{"title": "Civil rights", "content": "There are some words I've known since..."}]
    }
]).run()

# run a query

cursor = r.table("authors").filter(r.row["posts"].count() > 2).run()
for document in cursor:
    print document["name"]

# update data

print r.table("authors").update({"type": "fictional"}).run()
print r.table("authors").filter(r.row['name'] == "William Adama").update({"rank": "Admiral"}).run()

# delete data

print r.table("authors").filter(r.row["posts"].count() < 3).delete().run()