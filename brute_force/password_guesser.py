import string 
import itertools
import time
import csv

while True: 
  #User selects target password + error handling for blank input 
  while True:
    target_password = list(input("Enter a target password..."))
    if str("".join(target_password)).strip() == "":
      print("You can't leave this field blank!")
      continue 
    else:
      break

  password_length = len(target_password)
  count = 0
  
  #User selects whether they want to see the guesses or just the result
  while True:
    view_attempts = input("Would you like to see the guesses in real time?(y/n) ")
    if view_attempts == 'y' or 'n':
      break
    else:
      print("Please enter a valid input!")
      continue

  #Define an empty charset before conditions
  charset = ""

  #This improves efficiency by only including characters in the password
  if any(char in string.ascii_lowercase for char in target_password):
    charset += string.ascii_lowercase
  if any(char in string.ascii_uppercase for char in target_password):
    charset += string.ascii_uppercase
  if any(char in string.punctuation for char in target_password):
    charset += string.punctuation
  if any(char in string.digits for char in target_password):
    charset += string.digits
  if not charset:
    charset += string.ascii_letters + string.punctuation + string.digits

  #Define a function that guesses every permutation for our selected character set 
  
  #The brute force function that displays guesses
  def brute_force_view():  
    for x in itertools.product(charset, repeat=password_length):
      guess = ''.join(x)
      print(f"Trying: {guess}")
      global count
      count += 1

      if guess == ''.join(target_password):
        print(f"Password found: {guess} (in {count:,} attempts)")
        break
  
  #The brute force function that does NOT display guesses but displays guesses so far
  def brute_force_no_view():
    total_guesses = len(charset) ** password_length
    print(f"Guessing password... Estimated total guesses: {total_guesses:,}")

    update_frequency = max(1000, total_guesses // 100)  # Adaptive progress updates

    for count, x in enumerate(itertools.product(charset, repeat=password_length), 1):
        guess = ''.join(x)

        if count % update_frequency == 0:
            print(f"{count:,} attempts so far...")

        if guess == ''.join(target_password):
            print(f"Password found: {guess} (in {count:,} attempts)")
            break

  #Starts the timer that will give us our time for execution in our program
  start_time = time.time()

  #We start by checking really common passwords, stored on a csv file that has common passwords or passwords from a data breach
  with open("common_passwords.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
   
    found = False
    for row in reader:
      if row[0] == ''.join(target_password):
        print(f"Password found: {''.join(target_password)} ... Your password is very common!")
        found = True
        break

  #If the password isn't in csv file, we start brute forcing
    if found == False and view_attempts == 'y':
       brute_force_view()
    elif found== False and view_attempts == 'n':
       brute_force_no_view()
    else:
       pass
      
  #Ends our timer and tells us how much time it took to guess
  end_time = time.time()
  time_taken = end_time - start_time
  print(f"Time taken: {time_taken:.4g} seconds")

  try_again = input("Would you like to try another password?(y/n) ")

  if try_again == "y":
    continue
  else:
    print("Thanks for playing!")
    break
