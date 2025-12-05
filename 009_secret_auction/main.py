def highest_bidder(bidding_dictionary):
    g_bidder = 0
    n_bidder = ""

    for k, v in bidding_dictionary.items():
        if v > g_bidder:
            g_bidder = v
            n_bidder = k


    print(f"{n_bidder} is the higest bidder with {g_bidder}")
    print(f"Congratulations {n_bidder}!")


print("Welcome to the secret auction program.")


bids = {

}


bidder_on = True

while bidder_on:

    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))

    bids[name] = bid

    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'").lower()

    if more_bidders == "no":
        bidder_on = False
        highest_bidder(bids)
    else:
        print("\n" * 20)



