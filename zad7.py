nums = []

while len(nums) < 10:
  num = int(input("Podaj liczbę: "))
  nums.append(num)

evens = []
for i in nums:
  if i % 2 == 0:
    evens.append(i)


print(evens)

