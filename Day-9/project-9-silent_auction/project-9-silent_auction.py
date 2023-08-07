def clear():
    import os
    import sys
    # Linux
    if sys.platform.startswith('linux'):
        os.system('clear')
    # Windows
    elif sys.platform.startswith('win32'):
        os.system('cls')

def find_highest_bidder(bidding_record):
    highest_bid =0
    winner = ""
    for key in bidding_record:
        value = bidding_record[key]
        if highest_bid < value:
            highest_bid = value
            winner = key
    print(f"The winner is {winner} with a bid of {highest_bid}.")

end_bid = False
auction_log = {}

while not end_bid :
    from art import logo
    print(logo)
    bidder = input("What is your name?: ")
    bid_amount = int(input("What is your bid?: $"))
    auction_log[bidder] = bid_amount
    more_bidders = input("Are ther any other bidders? Type 'yes' or 'no.'\n")
    if more_bidders == 'no':
        end_bid = True
        find_highest_bidder(auction_log)
    elif more_bidders =='yes':
        clear()


# max_key = max(auction_log, key=auction_log.get)
# max_value = auction_log[max_key]
# print(f"The winner is {max_key} with a bid of {max_value}.") 




       
    

