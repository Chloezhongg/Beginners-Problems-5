def biggest_smallest_average():
    numsList = [7, 6, 23, 8.18, 18, 8, 7.2, 85, 915, 12]
    biggest = max(numsList)
    smallest = min(numsList)
    average = sum(numsList) / len(numsList)
    biggest_index = numsList.index(biggest)
    smallest_index = numsList.index(smallest)

    print(f"Biggest number: {biggest} at position {biggest_index}")
    print(f"Smallest number: {smallest} at position {smallest_index}")
    print(f"Average of all numbers: {average}")


def same_start_and_end():
    stringsList = ["abc", "123", "2332", "aBBA", "heelloo", "1212", "DcEfD"]
    count = 0

    for s in stringsList:
        if s[0].lower() == s[-1].lower():
            count += 1

    print(f"Number of strings with the same start and end character: {count}")


def i_like_pesto():
    iLikePesto = []
    otherFoods = []

    for _ in range(8):
        food = input("What's your favourite food? ").strip().lower()
        if food == 'pesto':
            iLikePesto.append(food)
        else:
            otherFoods.append(food)

    pesto_count = len(iLikePesto)
    print(f"Pesto is loved by {pesto_count} people!")
    for _ in range(pesto_count):
        print("I like pesto")

    print("\nOther Foods:")
    for food in otherFoods:
        print(food)


def list_of_good_cereals():
    cerealList = []
    disliked_cereals = ['sultana and bran', 'weetbix']

    while True:
        cereal = input("Enter Cereal: ").strip().lower()
        if cereal in disliked_cereals:
            break
        cerealList.append(cereal)

    print(cerealList)


# Uncomment the function you want to test
# biggest_smallest_average()
# same_start_and_end()
# i_like_pesto()
# list_of_good_cereals()
