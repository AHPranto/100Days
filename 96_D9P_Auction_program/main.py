import os
from art import logo
print(logo)

bids = {}
bidding_finished = False

def find_higest_bidder(bidding_record):
    highest_bid = 0
    # bidding_record = {"pranto":123}
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of {highest_bid} tk")

while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: (tk)"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if should_continue == "no":
        bidding_finished = True
        find_higest_bidder(bids)
    elif should_continue == "yes":
        clear = lambda: os.system('cls')
        clear()