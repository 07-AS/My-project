import random

def play():
    user=input("what's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    comp=random.choice(['r','p','s'])

    if user==comp:
        return "it\'s a tie"
    #r>s, s>p, p>r
    if is_win(user,comp):
        return "you won!"
    
    return "you lost!"
def is_win(player,opponent):
    #return true if player wins
    #r>s, s>p, p>r
    if (player=='r' and opponent=='s') or (player=='s' and opponent=='p')\
         or (player=='p' and opponent=='r'):
        return True
print(play())
    
choice=0
while choice==0:
    print("Do you want to continue playing? (Y/N)")
    ch=input("enter you choice: ")
    if ch=='Y':
        print(play())
    else:
        print("Thank you for playing, Hope you had a good time")
        exit()
