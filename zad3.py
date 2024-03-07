word = input("Podaj słowo: ")

start = 0
end = len(word) - 1

while start < end:
  if word[start] != word[end]:
    print("To nie jest palindrom")
    exit()
  start = start + 1
  end = end - 1

print("To jest palindrom")