from collections import Counter

VOWELS = ["A", "E", "I", "O", "U"]

players = {"Keivn": 0, "Stuart": 0}


def minion_game(string):
    list_split = list(string)
    # for iter in list_split:
    #     if iter in VOWELS:
    #         players["Keivn"] += 1
    #     else:
    #         players["Stuart"] += 1
    #
    # max_key = max(players, key=players.get)
    # max_value = players[max_key]

    not_vowels_list = [char for char in string if char not in VOWELS]
    vowels_list = [char for char in string if char in VOWELS]

    counter_vowels = Counter(vowels_list)
    counter_consants = Counter(not_vowels_list)
    vowels_most_common = counter_vowels.most_common()
    consants_most_common = counter_consants.most_common()

    print(
        f"Most common for \n\
    Vowels: {vowels_most_common} \n\
    Consants: {consants_most_common}"
    )

    players["Keivn"] = sum(value for _, value in vowels_most_common)
    players["Stuart"] = sum(value for _, value in consants_most_common)

    print(f"Kevin score: {players['Keivn']}")
    print(f"Stuart score: {players['Stuart']}")

    for key, _ in vowels_most_common :
        key_index = list_split.index(key)
        for string_iter in list_split[key_index:]:
            if key is string_iter:
                match_vowels = [char for char in list_split if string_iter+1 in ]



    # print(f"Winner: {max_key} with score {max_value}")


if __name__ == "__main__":
    # s = input()
    s = "BANANA"
    minion_game(s)
