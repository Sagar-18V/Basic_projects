import random
words=['python','java','ruby','virat']
word = random.choice(words)
guesses=''
count=4

while count>0:
     fail=0
     for char in word:
         if char in guesses:
             print(char,end=" ")
         else:
             print("_")
             print(char,end=" ")
             fail+=1
     if fail==0:
        print("you won")
        break
     print()
     guess = input()
     guesses += guess
     if guess not in word:
         count-=1
         print("wrong")
         if count==0:
             print("loss")
        
