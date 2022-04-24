#display art
# from replit import clear
from art import logo,vs
print(logo)
import random
from game_data import data
score=0

#format the account data into printable format
def format_data(account):
  '''Takes the account data and returns into printable format'''
  account_name=account["name"]
  account_descrp=account["description"]
  account_country=account["country"]
  return f"{account_name},a {account_descrp}, from {account_country}"


def check_answer(guess,a_followers,b_followers):
  '''Take the user guess and follower counts and returns if they got it right'''
  if a_followers>b_followers:
    return guess=="a"
  else:
    return guess=="b"  

game_should_continue=True
account_b =random.choice(data)
while game_should_continue:
  
  #generate a random account from the game data
  account_a =account_b
  account_b=random.choice(data)
  
  while account_a == account_b:
    account_b=random.choice(data)
  
  
  print(f"compare A:{format_data(account_a)}")
  print(vs)
  print(f"Against B:{format_data(account_b)}")
  #ask user for a guess
  
  guess= input("Who has more followers? Type 'A' or 'B' ").lower()
  
  
  # check if user is correct
  
  
  
  #get follower count of each account
  a_follower_count=account_a["follower_count"]
  b_follower_count=account_b["follower_count"]
  
  is_correct=check_answer(guess,a_follower_count,b_follower_count)
  
  #clear the screen 
  #clear()
  
  
  #give user feedback on their guess
  #score keeping
  if is_correct:
    score+=1
    print(f"you right,your currect score is {score}")
  else:
    #make game repeatable
    game_should_continue=False
    print(f"sorry that's wrong ,your final score is {score}")

  







