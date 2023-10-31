import os
from art import logo

print(logo)
other_bid="yes"
dic={}
while(other_bid=="yes"):
    name=input("Welcome to the secret auction program.\nWhat is your name?: ")
    bid=input("What's your bid?: $")
    dic[name]=bid
    other_bid=input("Are there any other bidders? Type 'yes' or 'no'.")
winner=max(dic, key=dic.get)
os.system('cls')
print(f"The winner is {winner} with a bid of ${dic[winner]}")