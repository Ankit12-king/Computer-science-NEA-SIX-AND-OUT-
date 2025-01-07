def get_cricket_news():
    cricket_news = [
        "India announces squad for the 2024 World Cup.",
        "Australia's Pat Cummins set to return from injury.",
        "England's Joe Root hits a double century in the Ashes.",
        "Pakistan's Babar Azam named ICC Cricketer of the Year.",
        "Sri Lanka qualifies for the 2024 T20 World Cup semifinals.",
    ]
    return cricket_news

def display_cricket_news():
    news = get_cricket_news()
    print("\nLatest Cricket News:")
    for item in news:
        print(f"- {item}")
        
display_cricket_news()
