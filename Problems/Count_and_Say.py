"""
	The count-and-say sequence is the sequence of integers beginning as follows:
	1, 11, 21, 1211, 111221, ...

	1 is read off as "one 1" or 11.
	11 is read off as "two 1s" or 21.
	21 is read off as "one 2, then one 1" or 1211.
	Given an integer n, generate the nth sequence.

	Note: The sequence of integers will be represented as a string.
"""
def countAndSay(n):
	s = '1'
	if n == 1:
		print int(s)
	else :
		for count in range(1,n):
			strA = ''
			temp = ''
			for i in s+'!':
				if temp == i:
					countI += 1
				else:
					if temp !='':
						strA += str(countI)
						strA += temp
					countI = 1

				temp = i

			s = strA
		print int(s)

countAndSay(4)
			
