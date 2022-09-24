'''As part of project evaluation, we would like to evaluate coding skills as well.
Could you handle below problem statement
Find vowel (a, e, i, o, u) words in given statement and return 1st word having max occurrences of vowels in it
Ex: Statement "This is apple" should return "apple" (as it has 2 vowels in it)
You can use Python, as per your convenient.
Try to write your own code, instead of using inbuilt libraries.
we should cover Unit Test cases for the code written (simple unit test cases, not required fully implemented Unit Test cases)'''
sentence = 'this is apple'

words = sentence.split(' ')
print(words)

def words_in_vowels(word):
    count = 0
    for i in word.lower():
        if i in ['a','e','o','i','u']:
            count+=1
    return count

def find_max_vowels(words):
    alist =[(word,words_in_vowels(word)) for word in words]
    alist.sort(key=lambda x:x[1])
    return alist[-1][0]

word = find_max_vowels(words)
print(word)

import unittest

class TestStringMethod(unittest.TestCase):

    def test_String1(self):
        actual = words_in_vowels(word),find_max_vowels(words)

        expected = (2,"apple")

        self.assertEqual(actual, expected, "hi")



if __name__ == '__main__':
    unittest.main()