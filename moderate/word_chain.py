#!/usr/bin/env python2
'''
# CodeEval - Word Chain (Partially Correct)
# https://www.codeeval.com/open_challenges/135/
'''

from sys import argv


class Word(object): 
    ''' Node of a linked list'''
    def __init__(self, word, next_word=None):
        self.word = word
        self.next_word = next_word


def create_word_chain(word, list_of_words, word_chains):
    list_of_words = list_of_words[:] # create local copy
    list_of_words.remove(word)
    head = Word(word)
    word_chains[word] = head
    cur = head
    while len(list_of_words):
        found = 0
        for word in list_of_words:
            if word[0] == cur.word[-1]:
                #print("Found new node")
                new_word = Word(word)
                cur.next_word = new_word
                cur = new_word
                list_of_words.remove(word)
                found = 1
                break
        if not found:
            return


def calc_word_chain_length(word_node, word_chains_length):
    i = 1
    cur = word_node
    while cur.next_word != None:
        i += 1
        cur = cur.next_word
    word_chains_length[word_node.word] = i


def main():
    f = open(argv[1], "rt")
    for line in f:
        words = line.strip().split(",")
        # {starting_word: word_chain_linked_list,...}
        word_chains = {} 
        # {starting_word: length_of_word_chain_linked_list,...}
        word_chains_length = {} 
        for word in words:
            create_word_chain(word, words, word_chains)
            calc_word_chain_length(word_chains[word], word_chains_length)

        largest_word_chain = max(word_chains_length.values())
        if largest_word_chain == 1:
            print("None")
        else:
            print(largest_word_chain)

    f.close()


if __name__ == "__main__":
    main()
