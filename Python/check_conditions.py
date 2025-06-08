#pangram is a sentece that contains every single letter of the alphabet at least once.
def is_pangram(testing_sentence):
    requirements = "abcdefghijklmnopqrstuvwxyz"
    for char in requirements:
        if char not in testing_sentence.lower():
            return False
    return True