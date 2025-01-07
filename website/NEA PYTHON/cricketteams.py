def get_cricket_teams():
    teams = [
        "India",
        "Australia",
        "England",
        "South Africa",
        "New Zealand",
        "Pakistan",
        "Sri Lanka",
        "Bangladesh",
        "West Indies",
        "Afghanistan",
        "Ireland",
        "Zimbabwe",
    ]
    return teams

def display_cricket_teams():
    teams = get_cricket_teams()
    print("\nList of Cricket Teams:")
    for team in teams:
        print(f"- {team}")

display_cricket_teams()
