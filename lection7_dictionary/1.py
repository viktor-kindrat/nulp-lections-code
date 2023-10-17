# hash table

dict_1 = {
    "key_1": "value",
}

dict_2 = dict()

# HOW TO PASS EXCEPTION
print(dict_1["key_1"])
print("key_0" in dict_1)  # => False

print(dict_1.get("key_1"))
print(dict_1.get("key_0") or "other")  # => "other"

# HOW TO ADD NEW KEY OR RE-DEFINE VALUE OF KEY
dict_2["new_key"] = "ok"
print(dict_2)

for key in dict_1:
    print(key, ":", dict_1[key])

# DICTIONARY METHOD DOCS

# dict.keys() => [key1, key2]
# dict.values() => [val1, val2]
# dict.items() => [(key, value)]

# HOW TO UPDATE DICT
dict_3 = {"first": "ok"}
dict_3.update(dict_3.fromkeys(["bgbgbd", 'gertggtrg']))  # => {'first': 'ok', 'bgbgbd': None, 'gertggtrg': None}

print(dict_3)
print("dict_3" in globals())  # => True
