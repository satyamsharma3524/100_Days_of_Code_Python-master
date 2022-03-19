import pandas

alphabets = pandas.read_csv("nato_phonetic_alphabet.csv")

# create a dictionary in {letter: word} format

new_alphabet_dict = {row.letter: row.code for (index, row) in alphabets.iterrows()}

# Create a list of the phonetic code words from a word that the user inputs
is_alphabet = True
while is_alphabet:
    user_word = input("Enter a word : ").upper()
    try:
        nato_phonetic_list = [new_alphabet_dict[letter] for letter in user_word]
        print(nato_phonetic_list)
        is_alphabet = False
    except KeyError:
        print("Sorry, Only letter sin the alphabets please.")
