import random

def generate_innings_scores(innings):
    return [random.randint(0, 300) for _ in range(innings)]

def calculate_average(scores):
    non_ducks = [score for score in scores if score > 0]
    if non_ducks:
        return sum(non_ducks) / len(non_ducks)
    return 0

def cricketer_stats():
    cricketers = []

    num_cricketers = int(input("How many cricketers' stats would you like to generate? "))

    for _ in range(num_cricketers):
        name = input("Enter the cricketer's name: ")
        cricketers.append(name)

    for cricketer in cricketers:
        test_scores = generate_innings_scores(5)
        odi_scores = generate_innings_scores(5)

        test_average = calculate_average(test_scores)
        odi_average = calculate_average(odi_scores)

        print(f"\nStats for {cricketer}:")
        print("Test Match Scores:", test_scores)
        print("Test Match Average:", test_average)
        print("ODI Scores:", odi_scores)
        print("ODI Average:", odi_average)


cricketer_stats()
