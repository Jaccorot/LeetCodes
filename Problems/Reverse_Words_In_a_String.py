"""

	Given an input string, reverse the string word by word.

	For example,
	Given s = "the sky is blue",
	return "blue is sky the".

"""
class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        a = s.split()
        temp=''
        for i in a[::-1]:
            temp += i
            temp += ' '
        return temp[:-1]