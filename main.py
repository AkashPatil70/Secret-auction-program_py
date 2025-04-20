from art import logo
print(logo)
auction_info = {}

# there is a function called max which takes dict as a input and what to be printed as 2nd variable
#it checks for the max value so we need to have a field as value on which we want to calculate
def calculate_winner(auction_info):
    max_bid = 0
    max_bid_user ={"name" : "",
                   "bid_value" : 0
                   }
    #another way we can have a user_name with string variable instead of dict and for bid value we have max bid
    for person in auction_info :
        if max_bid < auction_info[person] :
            max_bid_user["name"] = person
            max_bid_user["bid_value"]= auction_info[person]
            max_bid =auction_info[person]

    print(f"{max_bid_user['name']} is the Winner with bid amount : {max_bid_user['bid_value']}")

next_person_available = True
while next_person_available :
    name = input("What is your name?: ")
    auction_info [name] = int(input("What's your bid?: $"))
    next_person = input("is anyone else available for Bid?  type yes if available otherwise no....").lower()
    if next_person == "yes" :
        next_person_available = True
        print("\n"*100)
    else:
        next_person_available = False
        calculate_winner(auction_info)