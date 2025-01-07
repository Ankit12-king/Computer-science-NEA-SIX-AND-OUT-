import random

def generate_stats():
    runs_scored = random.randint(0, 100)
    balls_faced = random.randint(1, 30)
    wickets_taken = random.randint(0, 1)
    return runs_scored, balls_faced, wickets_taken

def batter_vs_bowler():
    batters = [
        "Virat Kohli", "Joe Root", "Steve Smith", "Kane Williamson", "Babar Azam"
    ]
    bowlers = [
        "Jasprit Bumrah", "Shaheen Afridi", "Pat Cummins", "Kagiso Rabada", "Rashid Khan"
    ]
    years = ["2023", "2022", "2021", "2020", "2019", "2018"]

    print("Available Batters:")
    for batter in batters:
        print(f"- {batter}")

    print("\nAvailable Bowlers:")
    for bowler in bowlers:
        print(f"- {bowler}")

    print("\nAvailable Years:")
    for year in years:
        print(f"- {year}")

    batter = input("\nEnter the name of the batter: ")
    while batter not in batters:
        print("Invalid batter name. Please choose from the list.")
        batter = input("Enter the name of the batter: ")

    bowler = input("Enter the name of the bowler: ")
    while bowler not in bowlers:
        print("Invalid bowler name. Please choose from the list.")
        bowler = input("Enter the name of the bowler: ")

    year = input("Enter the year: ")
    while year not in years:
        print("Invalid year. Please choose from the list.")
        year = input("Enter the year: ")

    print(f"\nMatchup: {batter} vs {bowler} in {year}")

    runs, balls, wickets = generate_stats()
    strike_rate = (runs / balls) * 100 if balls > 0 else 0

    print(f"\nStats:")
    print(f"- {batter} scored {runs} runs off {balls} balls (Strike Rate: {strike_rate:.2f})")
    if wickets:
        print(f"- {bowler} took {wickets} wicket.")
    else:
        print(f"- {bowler} did not take any wickets.")

if __name__ == "__main__":
    batter_vs_bowler()
