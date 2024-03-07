# def sum_of_dividers(num):
#   dividers = []
#   for i in range(1, (num // 2) + 1):
#     if num % i == 0:
#       dividers.append(i)
#   return sum(dividers)


# for i in range(1, 9000):
#   count = 0
#   if sum_of_dividers(i) == i:
#     count += 1

# print("Ilosc liczb perfekcyjnych: ", count)


def sum_of_dividers(num):
  dividers = []
  for div in range(1, (num // 2) + 1):
    if (num % div) == 0:
      dividers.append(div)
  return sum(dividers)
 
def is_perfect(num):
  return sum_of_dividers(num) == num
 
count = 0
for i in range(1, 1000):
  count += 1 if is_perfect(i) else 0

print(count)