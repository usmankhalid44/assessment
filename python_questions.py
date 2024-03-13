#                                                    PYTHON QUESTIONS
def fill_none_values(lst):
    last_non_none = lst[-1]
    filled_list = []
    for item in lst:
        if item is not None:
            last_non_none = item
            filled_list.append(item)
        else:
            filled_list.append(last_non_none)
    return filled_list
# Example:
original_list = [4, None,None, 1, 2, 3]
filled_list = fill_none_values(original_list)
print(filled_list)


def find_mismatched_case_words(string1, string2):
    words1 = string1.split()
    words2 = string2.split()

    mismatched_case_words = []
    for word1, word2 in zip(words1, words2):
        if word1.lower() == word2.lower() and word1 != word2:
            mismatched_case_words.append(word1)
            mismatched_case_words.append(word2)

    return mismatched_case_words


# Example:
string1 = "Datumlabs is an awesome place"
string2 = "Datumlabs.io Is an AWESOME pLace"
mismatched_case_words = find_mismatched_case_words(string1, string2)
print(mismatched_case_words)

def count_character_occurrences(string, char):
    count = 0
    string = string.lower()
    char = char.lower()
    for c in string:
        if c == char:
            count += 1
    return count

# Example:
string = 'mississippi'
char = 'P'
occurrences = count_character_occurrences(string, char)
print(f"The character '{char}' occurs {occurrences} times in the string '{string}'.")

def find_nth_largest_key(dictionary, n):
    sorted_items = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
    if n <= len(sorted_items):
        return sorted_items[n - 1][0]
    else:
        return None

# Example usage:
dictionary = {'a': 1, 'b': 200, 'c': 100, 'd': 30}
n = 1
nth_largest_key = find_nth_largest_key(dictionary, n)
print(f"The key of the {n}th largest value is '{nth_largest_key}'.")



