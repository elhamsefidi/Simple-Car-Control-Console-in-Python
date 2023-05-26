secret_number=9
guess_counter=0
while guess_counter<3:
    guess_number=int(input(f"Guess{guess_counter} "))
    guess_counter += 1
    if secret_number == guess_number:
        print("you won")
        break
else:
    print("you failed")
print(f"Game is after {guess_counter}th time is done")
