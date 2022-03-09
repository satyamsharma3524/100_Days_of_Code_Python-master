import pandas

alphabets = pandas.read_csv("nato_phonetic_alphabet.csv")

# create a dictionary in {letter: word} format

new_alphabet_dict = {row.letter: row.code for (index, row) in alphabets.iterrows()}

# Create a list of the phonetic code words from a word that the user inputs

user_word = input("Enter a word : ").upper()
nato_phonetic_list = [new_alphabet_dict[letter] for letter in user_word]
print(nato_phonetic_list)
