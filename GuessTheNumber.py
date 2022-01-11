import random

n = random.randint(1,100)
Number_of_Guesses = 1
print("**************Number of gessses is limited to only 5 times********")

while (Number_of_Guesses <= 5):
    Guess_number = int(input("Guess the number: "))
    if Guess_number < n:
        print("You entered less number, Please input geeter number")
    elif Guess_number > n:
        print("your entered greater number , please input smaller number")
    else:
        print("You Won !!!!Congratulion")
        print(Number_of_Guesses, "number of guesses you took to finish  ")
        break
    print(5-Number_of_Guesses,"number of guesses left")
    Number_of_Guesses = Number_of_Guesses + 1
if Number_of_Guesses > 5:
    print("Better luck next time ")
    print("Game Over!!")
    print(r"System's number was:" , n)
