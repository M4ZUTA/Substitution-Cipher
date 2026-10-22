def calculate_letter_frequencies(text):
    frequencies = {}
    letters_count = 0

    for letter in text:
        if letter.isascii() and letter.isalpha():
            letter = letter.upper()
            frequencies[letter] = frequencies.get(letter, 0) + 1
            letters_count += 1

    if not letters_count:
        return {}

    for letter, count in frequencies.items():
        frequencies[letter] = count / letters_count

    return dict(sorted(frequencies.items(), key=lambda item: item[1], reverse=True))


def calculate_n_gram_frequencies(cipher_text: str, n_gram_length: int = 2):

    n_gram_frequencies = {}
    n_grams_count = 0

    for i in range(len(cipher_text) - n_gram_length - 1):
        n_gram = cipher_text[i:i + n_gram_length]
        if n_gram.isalpha() and len(n_gram) == n_gram_length:
            if n_gram in n_gram_frequencies:
                n_gram_frequencies[n_gram] += 1
            else:
                n_gram_frequencies[n_gram] = 1
            n_grams_count += 1

    for letter, count in n_gram_frequencies.items():
        n_gram_frequencies[letter] = count / n_grams_count

    # Sort the dictionary
    n_gram_frequencies = dict(sorted(n_gram_frequencies.items(), key=lambda item: item[1], reverse=True))
    top_10 = dict(list(n_gram_frequencies.items())[:10])
    return top_10


def calculate_doubles_frequencies(cipher_text: str):

   #Finding all the double letter combinations.

    doubles_frequencies = {}
    doubles_count = 0

    for i in range(len(cipher_text) - 1):
        double = cipher_text[i:i + 2]
        if double.isalpha() and double[0] == double[1]:
            if double in doubles_frequencies:
                doubles_frequencies[double] += 1
            else:
                doubles_frequencies[double] = 1
            doubles_count += 1

    for double, count in doubles_frequencies.items():
        doubles_frequencies[double] = count / doubles_count

    return dict(sorted(doubles_frequencies.items(), key=lambda item: item[1], reverse=True))


def main():
    #main function
    class Theme:
        GREEN = "\033[92m"
        DARKCYAN = "\033[36m"
        BOLD = "\033[1m"
        END = "\033[0m"
    print("********************************************************************************\n")
    print(Theme.GREEN+ Theme.BOLD +"            Welcome to the Frequency Analysis program\n" + Theme.END)
    print(Theme.DARKCYAN+"This program lets you obtain the frequency of each letter \n in the  Monoalphabetic cipher text file and prints the \n results in the console.\n"+Theme.END)
    print("********************************************************************************")

    # Reading the cipher text from text file
    with open('Aleem S.txt', 'r', encoding='UTF-8') as file:
        cipher_text = file.read()

    # Performing letter frequency analysis
    letter_frequencies = calculate_letter_frequencies(cipher_text)
    print(Theme.GREEN+"\nLetter frequencies:\n"+Theme.END)
    for letter, frequency in letter_frequencies.items():
        print(f'{letter} = {round(frequency * 100, 2)}%')

    # Performing letter-combination frequency analysis in different combinations
    two_letters_combinations_frequencies = calculate_n_gram_frequencies(cipher_text, n_gram_length=2)
    three_letters_combinations_frequencies = calculate_n_gram_frequencies(cipher_text, n_gram_length=3)
    double_letters_combinations_frequencies = calculate_doubles_frequencies(cipher_text)
    four_letters_combinations_frequencies = calculate_n_gram_frequencies(cipher_text, n_gram_length=4)

    print(Theme.GREEN+"\nTwo letters combinations frequencies:\n"+Theme.END)
    for letter, frequency in two_letters_combinations_frequencies.items():
        print(f'{letter} = {round(frequency * 100, 2)}%')

    print(Theme.GREEN+"\n Three letters combinations frequencies:\n"+Theme.END)
    for letter, frequency in three_letters_combinations_frequencies.items():
        print(f'{letter} = {round(frequency * 100, 2)}%')

    print(Theme.GREEN+"\nDouble letters combinations frequencies:\n"+Theme.END)
    for double, frequency in double_letters_combinations_frequencies.items():
        print(f'{double} = {round(frequency * 100, 2)}%')

    print(Theme.GREEN+"\nFour letters combinations frequencies:\n"+Theme.END)
    for letter, frequency in four_letters_combinations_frequencies.items():
        print(f'{letter} = {round(frequency * 100, 2)}%')


if __name__ == '__main__':
    main()
