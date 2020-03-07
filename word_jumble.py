import os
import sys
from sys import argv
from random import randrange


def setup_dict():
    with open("/usr/share/dict/words", 'r') as dict_file:
        dict_list = dict_file.read().splitlines()
    return dict_list


def sort_word(word):
    """ sorts str word alphabetically """
    return ''.join(sorted(word.lower()))


def sort_words(word_list):
    """ for every word in word_list, sort the word's characters alphabetically, return new list """
    result = []
    for word in word_list:
        result.append(sort_word(word))
    return result


class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


class WordJumbleSolver:
    def __init__(self, words, indices, answer_format=None):
        """ Initialize the game! """
        self.jumbled_unsorted = words
        self.jumbled = sort_words(words)
        self.indices = self.get_indices_dict(indices)
        self.dict = setup_dict()
        self.sorted_dict = sort_words(self.dict)

        self.solved_words = self.find_anagrams()
        self.jumbled_answer = self.get_answer()
        self.answer = self.solve_answer(answer_format)

    def get_answer(self):
        j_answer = ""
        for i in range(len(self.jumbled)):
            for index in self.indices[sort_word(self.solved_words[i])][::-1]:
                j_answer += self.solved_words[i][index]
        return j_answer

    def solve_answer(self, answer_format):
        possible_answers = dict()
        for length in answer_format:
            possible_answers[length] = []
        if answer_format is None:
            for i in range(len(self.sorted_dict)):
                if self.sorted_dict[i] == sort_word(self.jumbled_answer):
                    return self.dict[i]
        else:
            if all(char in self.jumbled_answer for char in "stinks"):
                print("WORKING?!")
            for i in range(len(self.dict)):
                for length in answer_format:
                    if len(self.dict[i]) == length and all(char in self.jumbled_answer for char in self.dict[i].lower()):
                        possible_answers[length].append(self.dict[i])
            good_answers = []
            for i in range(len(possible_answers[answer_format[0]])):
                for j in range(len(possible_answers[answer_format[1]])):
                    sorted_combined = sort_word(possible_answers[answer_format[0]][i]+possible_answers[answer_format[1]][j])
                    if sort_word(self.jumbled_answer) == sorted_combined:
                        good_answers.append(f"{possible_answers[answer_format[0]][i]} {possible_answers[answer_format[1]][j]}")
            return good_answers

    def find_anagrams(self):
        """ search through every word in sorted_words to find  """
        anagrams = []
        for i in range(len(self.sorted_dict)):
            for word in self.jumbled:
                if self.sorted_dict[i] == word:
                    anagrams.append(self.dict[i].lower())
        return anagrams

    def get_indices_dict(self, indices):
        word_to_index = {}
        for i in range(len(self.jumbled)):
            indices[i].sort()
            word_to_index[self.jumbled[i]] = indices[i]
        return word_to_index

    def print_answer(self):
        print('\033[4m\033[95mWORD JUMBLE SOLVER!\033[0m')
        for i in range(len(self.jumbled)):
            solved_word = self.solved_words[i]
            for index in self.indices[sort_word(solved_word)][::-1]:
                solved_word = f"{solved_word[:index]}\033[4m\033[94m{solved_word[index]}\033[0m{solved_word[index+1:]}"
            for word in self.jumbled_unsorted:
                if sort_word(word) == sort_word(self.solved_words[i]):
                    print(f"{word}: {solved_word}")
        print(f"\nJumbled Answer: {self.jumbled_answer}")
        if len(self.answer) > 1:
            print(f"Possible solutions: \033[94m\033[1m{self.answer}\033[0m")
        elif len(self.answer) == 1:
            print(f"Solution: \033[94m\033[1m{self.answer[0]}\033[0m")
        else:
            print("\033[91mNo solutions found!\033[0m")


if __name__ == '__main__':

    jumble = WordJumbleSolver(["dcaiic", "lcaecrleit", "cpalaa", "hmtycirh", "tlinmusioa"],
                              [[0, 2, 3], [1, 2, 5, 7], [0, 3, 5], [1, 3, 5, 7], [2, 4, 5, 6, 7]],
                              [7, 12])
    jumble.print_answer()

    # jumble = WordJumbleSolver(
    #     # Jumbled words
    #     ['TEFON', 'SOKIK', 'NIUMEM', 'SICONU'],
    #     # index of circled letters
    #     [[2, 4], [0, 1, 3], [4], [3, 4]],
    #     # format of final answer! # of letters in each word. DON'T INCLUDE THE LENGTH IF THE ANSWER IS ONE WORD!
    #     [2, 6]
    # )
    # jumble.print_answer()
