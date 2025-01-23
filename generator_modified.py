import random

def getWords(filename):
    """Reads words from a file and returns them as a tuple."""
    with open(filename, 'r') as file:
        words = file.read().strip().split()
    if not words:
        raise ValueError(f"The file '{filename}' is empty or contains no valid words.")
    return tuple(words)

# Initialize the vocabulary by reading from the text files
articles = getWords('articles.txt')
nouns = getWords('nouns.txt')
verbs = getWords('verbs.txt')
prepositions = getWords('prepositions.txt')

def sentence():
    """Builds and returns a formatted sentence."""
    return (nounPhrase() + " " + verbPhrase() + ".").capitalize()

def nounPhrase():
    """Builds and returns a noun phrase."""
    return random.choice(articles) + " " + random.choice(nouns)

def verbPhrase():
    """Builds and returns a verb phrase."""
    return random.choice(verbs) + " " + nounPhrase() + " " + prepositionalPhrase()

def prepositionalPhrase():
    """Builds and returns a prepositional phrase."""
    return random.choice(prepositions) + " " + nounPhrase()

def main():
    """Allows the user to input the number of sentences to generate."""
    try:
        number = int(input("Enter the number of sentences: "))
        for count in range(number):
            print(sentence())
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

if __name__ == "__main__":
    main()
