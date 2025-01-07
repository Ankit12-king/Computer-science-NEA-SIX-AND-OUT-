def get_cricket_players():
    players = [
        "Virat Kohli",
        "Joe Root",
        "Steve Smith",
        "Babar Azam",
        "Kane Williamson",
        "Pat Cummins",
        "Jasprit Bumrah",
        "Shaheen Afridi",
        "Trent Boult",
        "Shakib Al Hasan",
        "Rashid Khan",
        "AB de Villiers",
    ]
    return players

def display_cricket_players():
    players = get_cricket_players()
    print("\nList of Cricket Players:")
    for player in players:
        print(f"- {player}")

display_cricket_players()
