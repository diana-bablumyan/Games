import random

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
shape = ['H', 'D', 'C', 'S']
cards_52 = []

for i in cards:
    for j in shape:
        cards_52.append(str(j)+str(i))

#print(cards_52)

def my_cards_2():

    my_card = []
    for i in range(2):
        
        my_card.append(random.choice(cards_52))

    return my_card

def dealer_cards_3():

    dealer_card = []
    for i in range(3):

        dealer_card.append(random.choice(cards_52))

    return dealer_card

def dealer_cards_1_1():

    dealer_card = dealer_cards_3()
    dealer_card.append(random.choice(cards_52))

    return dealer_card


answer1 = input("Do you want to play POKER? yes/no ")
if answer1 == 'yes':
    my_cards = my_cards_2()
    print(f"My cards: {my_cards}")
    answer2 = input("Do you want to continue? yes/no ")
    if answer2 == 'yes':
        dealer_cards = dealer_cards_3()
        print(f"Dealer cards: {dealer_cards}")
        answer3 = input("Do you want to continue? yes/no ")
        if answer3 == 'yes':
            dealer_cards.append(random.choice(cards_52))
            print(f"Dealer cards: {dealer_cards}")
            answer3 = input("Do you want to continue? yes/no ")
            if answer3 == 'yes':
                dealer_cards.append(random.choice(cards_52))
                print(f"Dealer cards: {dealer_cards}")

else:
    print("Okey.I will wait you!!!")
    # else:
    #     print("Okey.Let's try again!!!")
    #     else:
    #         print("Okey.Let's try again!!!")
    #         else:
    #             print("Okey.Let's try again!!!")



