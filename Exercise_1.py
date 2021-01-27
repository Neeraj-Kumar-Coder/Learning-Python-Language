dictionary = {"Mutable": "Liable to change",
              "Immutable": "Unchanging or unchangable",
              "Ignore": "Deliberately take no notice of",
              "Gunge": "Sticky and messy matter",
              "ROM": "Computing Read Only Memory"}
print("Enter the word which you want the meaning of: ", end="")
word = input()
print("The meaning of", word, "is :", dictionary[word.capitalize()])