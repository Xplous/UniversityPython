dct = {1: 11, 2: 22, 3: 33, 4: 4, 5: 33, 6: 1}
set_key = set();
set_value = set();
for key, value in dct.items():
    set_key.add(key);
    set_value.add(value);
set_new = set_key.union(set_value)
print(set_new)
# Видно, что при объединении множеств, получилось одно множество с неповторяющимися данными.
