import re

def input_text():
    string = input("Input text: ")
    string = re.sub('[,.!?\n]', '', string)
    return string


def get_words_list(string: str):
    words = string.split()
    return words


def get_words_number(words: list):
    words_count = {}
    for item in words:
        if words_count.__contains__(item):
            continue
        words_count[item] = words.count(item)
    return words_count


def get_median_words_number(words_number: dict):
    words = words_number.values()
    words = list(words)
    if len(words) % 2 == 0:
        med = (words[int(len(words) / 2 - 1)] + words[int(len(words) / 2)]) / 2
    else:
        med = words[len(words) // 2]
    return med



def get_average_words_number(words: list, words_count: dict):
    return len(words) / len(words_count)



def get_ngrams(words: list, string: str, n: int):
    n_gram = {}
    for item in words:
        for i in range(len(item)):
            if i + n > len(item):
                break
            if not n_gram.__contains__(item[i:i + n]):
                n_gram[item[i: i + n]] = string.count(item[i:i + n])
    return n_gram


def show_top_ngrams(n_gram: dict, k: int):
    n_gram = sorted(n_gram, key=n_gram.get)
    n_gram.reverse()
    for i in range(k if len(n_gram) > k else len(n_gram)):
        print(n_gram[i])



def input_n_k():
    n = input("Input n: ")
    k = input("Input k: ")
    if n == "":
        n = 4
    if k == "":
        k = 10
    n = int(n)
    k = int(k)
    return [k, n]


def main():
    k, n = input_n_k()
    string = input_text()

    words = get_words_list(string)
    words_number = get_words_number(words)

    print("Words number: " + str(words_number))
    average_words_number = get_average_words_number(words, words_number)

    print("Average words number: " + str(average_words_number))
    median_words_number = get_median_words_number(words_number)

    print("Median words number: " + str(median_words_number))
    n_grams = get_ngrams(words, string, n)
    show_top_ngrams(n_grams, k)


if __name__ == '__main__':
    main()