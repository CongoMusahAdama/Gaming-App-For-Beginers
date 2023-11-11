secret_number=int("3")

print(secret_number)

print("you are to guess a secret number by three atempt!")


guess_count= 1
while guess_count <= 5:
 usernumber= int (input("what's your number:"))
 usernumber=int()
 print(usernumber)



if usernumber!= secret_number:
    print(" \n you got it right buddy")
   
elif usernumber < secret_number:
    print("\n your answer is too low, try again buddy")

elif usernumber> secret_number:
    print(" \n your answer is too high, try again buddy")

