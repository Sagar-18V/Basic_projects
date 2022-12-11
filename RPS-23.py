import random
user=input()
computer=random.choice(['r','p','s'])
def play():
 
    if user==computer:
        return "Tie MC"
    if(user=='r' and computer=='s') or(user=='p' and computer=='r') or(user=='s' and computer=='p'):
        return "Its ur luck BC"
    return "Looser"
print(computer)
print(play())
