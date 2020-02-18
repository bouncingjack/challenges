from data import DICTIONARY, LETTER_SCORES
import os

def load_words():
    """Load dictionary into a list and return list"""
    with open(os.path.join(os.path.dirname(__file__), DICTIONARY), 'r') as f:
        return f.read().splitlines()
    

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    
    score = 0
    for letter in [x.capitalize() for x in word if x.capitalize() in LETTER_SCORES.keys()]:      
        score += LETTER_SCORES[letter.capitalize()]
    return score

def max_word_value(words=load_words()):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    
    max_value = {'word': '', 'score': 0}
    
    for w in words:
        word_score = calc_word_value(w)
        if word_score > max_value['score']:
            max_value = {'word': w, 'score': word_score}
    return max_value['word']

if __name__ == "__main__":
    pass # run unittests to validate
