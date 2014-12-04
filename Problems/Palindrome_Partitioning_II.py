"""
	Given a string s, partition s such that every substring of the partition is a palindrome.

	Return the minimum cuts needed for a palindrome partitioning of s.

	For example, given s = "aab",
	Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.
"""
def minCut(s):
	temp = s
	tempTimes = 0
	while len(s)!= 0:
		count = 1
		pieces =[]
		count = 0
		while (len(temp) != 0):
			loop = True
			strS = temp
			while (len(strS) != 0)  and loop:
				if strS == strS[-1::-1]:
					pieces.append(temp[:len(strS)])
					loop = False
					break
				else:
					strS=strS[:-1]

			temp = temp[len(pieces[-1:][0]):]
			cutTimes = len(pieces)-1
		s=s[:-1]
		if ((tempTimes > cutTimes) or (tempTimes == 0) ):
			tempTimes = cutTimes

	print tempTimes

minCut('aaabaa')