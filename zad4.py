number = int(input("Podaj liczbę: "))

is_prime = True

if number <= 1:
  print("Liczba nie jest pierwsza")
  exit()
elif number > 1:
  for i in range(2, number):
    if number % i == 0:
      is_prime = False
      break

print("Liczba jest pierwsza" if is_prime else "Liczba nie jest pierwsza")
