import sys
import nltk
# nltk.download('wordnet')
from nltk.corpus import wordnet

def readInput():
    # input = sys.argv[1]
    input = 'The bank can guarantee deposits will eventually cover future tuition costs ' \
            'because it invests in adjustable-rate mortgage securities.'
    # word = sys.argv[2]
    word = 'bank'

    return input, word


def lesk(input, word):

    bestSense = 'n'
    maxOverlap = 0
    context = input.split()
    print('Context: ', context)

    synsets = wordnet.synsets(word)

    for synset in synsets:
        if synset.name().__contains__('.' + 'n' + '.'):
            print('Name: ', synset.name())
            print('Definition: ', synset.definition())
            print('Example: ', synset.examples())
            # print('Lemma name: ', synset.lemmas()[0].name())

            # Signature
            signature = str(synset.definition()) + ' '
            for example in synset.examples():
                signature += str(example)
            signature = signature.replace('(', '').replace(')', '')
            signature = signature.split()
            print('Signature: ', signature, '\n')

            overlap = len(set(context) & set(signature))

            if overlap > maxOverlap:
                maxOverlap = overlap
                bestSense = synset.definition()
            #
            # print('Sense: ', bestSense)
            # print('Overlap: ', maxOverlap)

    print('Best Sense: ', bestSense)
    print('Max Overlap: ', maxOverlap)

if __name__ == '__main__':
    input, word = readInput()
    lesk(input, word)