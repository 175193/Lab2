arr = [1, 'jeden', 2, 'dwa', 3, 'trzy', 4, 'cztery', 5, 'pięć', 1, 2, 3, 4, 5]

count_dict = {}
for element in arr:
  if element in count_dict:
    count_dict[element] += 1
  else:
    count_dict[element] = 1

numeric_dict = {}
for key, value in count_dict.items():
  if isinstance(key, int):
    numeric_dict[key] = value

print(numeric_dict)