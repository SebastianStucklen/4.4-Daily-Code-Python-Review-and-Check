#Ask a user how much they can bench press. If they can only lift under 10lbs, tell them to keep practicing and they'll get more swol. If they can lift between 10 and 50lbs, tell them they are getting good. If they can lift more than 50lbs, tell them the are mega swol. 
pounds = int(input("How much can you bench press"))
if pounds < 10:
    print("Keep practicing and youll get more swol.")
elif pounds >= 10 and pounds <= 50:
    print("You're getting good!")
elif pounds > 50:
    print("you are mega swol!!!")


#Use a for loop to print out the numbers 20-50 counting by 2s.
count = 20
for i in range(16):
    print(count)
    count+=2


#Use a while loop to print out the word "ribbit!" until the user types in the word "frog". 
#Write another while loop that prints out the numbers 100 down to 50 counting by 5s (no for loops).
inputttt = "placeholder"
while inputttt != "frog":
    print("ribbit!")
    inputttt = input("")


number = 100
while number >= 50:
    print(number)
    number-=5
#Write a function named AvgTwoNums. Function AvgTwoNums takes two parameters x and y. It adds the two numbers together, divides them by 2, and then returns the result. Call the function inside a print statement, and pass it the numbers 8 and 4 as arguments. 

#In a separate program, write function GiveCompliment. Function GiveComplement takes a parameter named "name" and doesn't return anything. When called, it prints out, "__________, you look so nice today!", placing the name passed as a parameter into the blank spot. Outside of the function definition, create a game loop that runs forever. Inside the game loop, ask the user for their name, and then call the function, passing it the name collected from the user. You don't need to be able to quit the game loop. 
def AvgTwoNums(x,y):
    return (x+y)/2

print(AvgTwoNums(8,4))
def GiveCompliment(name):
    print(f"{name}, you look so nice today!")
while True:
    name1 = input("whats your name?")
    if name1 == "break":
        break
    else:
        GiveCompliment(name1)
print("test")


#Write a list named "marbles" and fill it with the numbers 4, 6, 2, and 9. 
#Print out the second element. 
#Then multiply each list element by 5. 
#Then print out the whole list. 
marbles = [4,6,2,9]
print(marbles[1])
#marbles*=5

l = 0
for i in range(4):
    marbles[l]*=5
    l+=1
print(marbles)