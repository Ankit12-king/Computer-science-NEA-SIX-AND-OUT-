def get_upcoming_matches():
    upcoming_matches = [
        {"match": "India vs Pakistan", "date": "5th January 2024"},
        {"match": "Australia vs England", "date": "7th January 2024"},
        {"match": "South Africa vs New Zealand", "date": "10th January 2024"},
        {"match": "Bangladesh vs Sri Lanka", "date": "12th January 2024"},
    ]
    return upcoming_matches

def display_upcoming_matches():
    matches = get_upcoming_matches()
    print("\nUpcoming Cricket Matches:")
    for match in matches:
        print(f"{match['match']} - {match['date']}")


display_upcoming_matches()
