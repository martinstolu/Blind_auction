logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

auction = True
bidders = {}
highest_bidder = 0
winner = ""
while auction:
    name = input("What is your name:\n")
    bid = int(input("What is your bid?:\n$"))
    bidders[name]=bid
    other_bidder = input("Are there any other bidders?:\n")

    if other_bidder == "no".lower():
        for key in bidders:
            bid_amount = bidders[key]
            if bid_amount > highest_bidder:
                highest_bidder = bid_amount
                winner = key


        print(f"The winner is {winner} with a bid of"
              f" ${highest_bidder}")
        auction = False

    elif other_bidder == "yes".lower():
        print(f"\n" * 10)


# ANOTHER VERSION BELOW
#
# print(logo)
# print("Welcome to the secret auction program.")
#
# def find_highest_bidder(bidding_dictionary):
#
#     highest_bid = 0
#     winner = "" #or max(bidders)
#
#     max(bidding_dictionary)
#
#     for key in bidding_dictionary:
#         if bidding_dictionary[key] > highest_bid:
#             highest_bid = bidding_dictionary[key]
#             winner = key
#
#     print(f"The winner is {winner}, "
#           f"with a bid of ${highest_bid} ")
#
# bidders = {}
# auction = False
# while not auction:
#     bidder_name = input("What is your name?\n").lower()
#     bid = int(input("What's your bid?\n$"))
#     bidders[bidder_name] = bid
#
#     other_bidder = input("Are there any other bidders? Type"
#                          " 'yes' or 'no'.\n")
#     if other_bidder == "yes".lower():
#         print("\n" *10)
#     elif other_bidder == "no".lower():
#         find_highest_bidder(bidders)
#         auction = True
