from replit import clear
#HINT: You can call clear() to clear the output in the console.

from art import logo

print(logo)
print("\nWelcome to secret auction program.")
auction_finish = False
auction_bids = {}
def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder 
  print(f"The winner is {winner} with a bid of ${highest_bid}.")
while auction_finish == False:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    auction_bids[name] = price
    bidders = input("Are there any bidders? Types 'yes' or 'no'.\n").lower()
    if bidders == "no":
      clear()
      find_highest_bidder(auction_bids)
      auction_finish = True
    elif bidders == "yes":
      clear()
