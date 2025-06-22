import random
from art import logo, vs
from game_data import data

print(logo)
score = 0
#format the data to display
def format_data(account):
    """Format account data into printable form"""
    account_name = account["name"]
    account_dis = account["description"]
    account_origin = account["country"]
    return f"{account_name}, a {account_dis}, from {account_origin}"

def check_winner(user_guess, a_followers, b_followers):
    """Take the user guess and the followers of both A and B , then returns the winner"""
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"

account_b = random.choice(data)
#generate random account from data
game_should_continue = True
while game_should_continue:

    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)
    # print the data in formated string
    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    # take user choice as input
    guess = input(str("Who has more followers? Type A or B: \t")).lower()
    print("\n" * 20)
    print(logo)

    # Check if user is correct or not
    a_account_followers = account_a["follower_count"]
    b_account_followers = account_b["follower_count"]
    is_correct = check_winner(guess, a_account_followers, b_account_followers)

    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        print(f"You're wrong! Final  score: {score}")
        game_should_continue = False
