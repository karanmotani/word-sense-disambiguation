import sys
import nltk
nltk.download('wordnet')
from nltk.corpus import wordnet

# Read the Inputs: the input sentence and the word
def readInput():
    # input = sys.argv[1]
    input = 'The bank can guarantee deposits will eventually cover future tuition costs ' \
            'because it invests in adjustable-rate mortgage securities.'
    # word = sys.argv[2]
    word = 'bank'

    return input, word


# Simplied Lesk Algorithm Function
def lesk(input, word):

    context = input.split()
    context.remove(word)

    synsets = wordnet.synsets(word)
    maxOverlap = 0
    bestSense = 0

    # Initial best-sense <- most frequent sense for word
    if synsets[0].name().__contains__('.' + 'n' + '.'):
        bestSense = synsets[0].definition()
    print('Input sentence: ', input)
    print('Word: ', word)
    print('Best Sense: ', bestSense)
    print('\n')

    for synset in synsets:
        if synset.name().__contains__('.' + 'n' + '.'):
            print('Name: ', synset.name())
            print('Definition: ', synset.definition())
            print('Example: ', synset.examples())

            # Signature
            signature = str(synset.definition()) + ' '
            for example in synset.examples():
                signature += str(example)
            signature = signature.replace('(', '').replace(')', '').replace(';', '').replace(',', '').replace('.', '')
            signature = signature.split()
            if word in signature:
                signature.remove(word)

            overlap = len(set(context) & set(signature))
            print('Overlap: ', overlap)
            if overlap > maxOverlap:
                maxOverlap = overlap
                bestSense = synset.definition()

                print('Best Sense changed: ', bestSense)
            print('\n')

    print('\n----------------------------------------------- OUTPUT -----------------------------------------------\n')
    print('Best Sense: ', bestSense)
    print('Max Overlap: ', maxOverlap)

if __name__ == '__main__':
    input, word = readInput()
    lesk(input, word)