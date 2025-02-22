import random

def num_validator(message):
  while True:
    try:
      num = int(input(message))
      return num
    except:
      print("Please enter a valid number")

start = num_validator("Enter the range start: ")
end = num_validator("Enter the range end: ")
random_number = random.randint(start, end)
i = 0
while i < 10:
  guess = num_validator("Wanna guess?")
  if guess > random_number:
    print("Ops! that too high...")
    print("guess again")
    i += 1
  elif guess < random_number:
    print("Ops! that too low...")
    print("guess again")
    i += 1
  else:
    print("you won!")
    break