import random 
from game_data import data 
# Add art.
from art import logo, vs
from replit import clear 


# Generate a random account from the game data.
def get_random_account():
    """Grabs a random account from the game_data file"""
    return random.choice(data)


# Format account data into printable format.
def format_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    
    return f"{name}, {description}, from {country}. "

def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

def game():
    print(logo)
    score = 0 
    game_should_continue = True 
    account_a = get_random_account()
    account_b = get_random_account()
    
    # Make game repeatable.
    while game_should_continue:
        # Make B become the next A.
        account_a = account_b
        account_b = get_random_account()

        while account_a == account_b:
            account_b = get_random_account()

        print(f"Compare A: {format_data(account_a)}")
        print(vs)
        print(f"Against B: {format_data(account_b)}")
        
        # Ask user for a guess.
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        
        ## Get follower count.
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        
        # Check if user is correct.
        is_correct = check_answer(guess, a_follower_count, b_follower_count)
        
        # Clear screen between rounds.
        clear()
        print(logo)
        
        # Score Keeping.
        if is_correct:
            score += 1
            print(f"You're right. Your current score is {score}.")
        else: 
            game_should_continue = False
            print(f"Sorry, that was wrong. Your final score is {score}. ")


game()






    
















