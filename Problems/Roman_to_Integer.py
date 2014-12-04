'''
	Given a roman numeral, convert it to an integer.

	Input is guaranteed to be within the range from 1 to 3999.
'''

def romanToInt(s):
    result = 0
    romanDict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    for i in s[-1::-1]:
        symbol = 1
        if i in ['I','X','C'] and 5 * romanDict[i] <= result:
            symbol = -1
        print 'symbol=',symbol,i,'---result=',result

        result += romanDict[i] * symbol

    print result


romanToInt('MCDIV')