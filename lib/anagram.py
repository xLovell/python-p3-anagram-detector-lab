# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, anagrams):
        anagram_list = []
        for anagram in anagrams:
            if(sorted(anagram) == sorted(self.word)):
                anagram_list.append(anagram)
        return anagram_list
    
