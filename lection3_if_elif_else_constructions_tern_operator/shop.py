price = 150

if price > 100:
    volume = 50 # "vol" i bad name for variable
else:
    volume = 55

volume = 50 if price > 100 else 10 # тернарний оператор (val_true if expression else val_else)

print(volume)