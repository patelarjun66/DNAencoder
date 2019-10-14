'''
Encoder.py
Driver Program
Program written and tested in Python3
'''
from collections import deque
import unittest

DNAdict = {'a':'TGAT','c':'TGAC','t':'TCTA','ACTA':'a','ACTG':'c','AGAT':'t'}
RNAdict = {'a':'UGAU','c':'UGAC','t':'UCUA'}

def main(str):
    output = ""
    str = str.replace(" ","")
    #if input is DNA it will be upper case and length multiple of 4
    if str.isupper():
        if len(str) % 4 == 0:
            output = TranslateDNAToString(str)
    #else input will be string and have to be converted to DNA/RNA
    else:
        output = TranslateStringToDNA(str)
    return(output)


#function to translate ascii string to DNA:
def TranslateStringToDNA(str):
    out = ""
    #iterate through string and find character in corresponding dictionary
    for i in range(len(str)):
        out += DNAdict[str[i]]
    return out


#function to translate ascii string to RNA:
def TranslateStringToRNA(str):
    out = ""
    #to translate to RNA use following for loop in place of above for loop
    for i in range(len(str)):
        out +=RNAdict[str[i]]
    return out
    
    
#function to translate DNA to ascii string:
def TranslateDNAToString(str1):
    out = ""
    group = ''
    #iterate through string in lengths of 4 and translate to corresponding dictionary values
    for i in range(0,len(str1)):
        if len(group)<4:
            group+=str1[i]
        if len(group)%4 == 0:
            out+=DNAdict[group]
            group = ''
    return out


#function to find DNA substring in string input:
def asciiSub(str):
    DNAencodeddict = {'TGAT':'a','TGAC':'c','TCTA':'t'}
    #create queue to move through array in groups of 4
    queue = deque([' ',' ',' ',' '])
    str1 = ''
    #move through string searching for first instance of DNA of length 4
    for i in range(0,len(str)):
        str1 = queue[0]+queue[1]+queue[2]+queue[3]
    #search for current 4 length string in dictionary
        if str1 in DNAencodeddict.keys():
            return i-4
    #move forward in strong by popping first value from queue and appending new value
        queue.popleft()
        queue.append(str[i])
    return -1
    
    
#function to find DNA substring in string input:
def longestCommonSubsequence(str1,str2,len1,len2):
    table = [[0 for x in range(len2+1)] for x in range(len1+1)] 
  
    # create table to store when character in str1 matches any character in str2
    for i in range(len1+1): 
        for j in range(len2+1): 
            if i == 0 or j == 0: 
                table[i][j] = 0
            elif str1[i-1] == str2[j-1]: 
                table[i][j] = table[i-1][j-1] + 1
            else: 
                table[i][j] = max(table[i-1][j], table[i][j-1]) 
  
    # initialize final return list(to be converted to string)
    index = table[len1][len2] 
    lcs = [""] * (index+1) 
    lcs[index] = "" 

    #iterate through arrays append to lcs array when characters match
    i = len1 
    j = len2 
    while i > 0 and j > 0: 
        if str1[i-1] == str2[j-1]: 
            lcs[index-1] = str1[i-1] 
            i-=1
            j-=1
            index-=1
        elif table[i-1][j] > table[i][j-1]: 
            i-=1
        else: 
            j-=1
    #convert array to string and return
    return "".join(lcs) 



class Test(unittest.TestCase):
    #testing encoding functionality
    def test_encodingtest1(self):
        actual = main('a')
        expected = 'TGAT'
        self.assertEqual(actual, expected)
    def test_encodingtest2(self):
        actual = main('cat')
        expected = 'TGACTGATTCTA'
        self.assertEqual(actual, expected)
    def test_encodingtest3(self):
        actual = main('c a t')
        expected = 'TGACTGATTCTA'
        self.assertEqual(actual, expected)
    #testing decoding functionality
    def test_decodingtest1(self):
        actual = main('ACTGACTAAGAT')
        expected = 'cat'
        self.assertEqual(actual, expected)
    def test_decodingtest2(self):
        actual = main('ACTG ACTA AGAT')
        expected = 'cat'
        self.assertEqual(actual, expected)
    def test_blankinputtest(self):
        actual = main('')
        expected = ''
        self.assertEqual(actual, expected)
    #testing search for ascii interface
    def test_asciisubstringinterface(self):
        actual = asciiSub('ansfuafnaTGAThihsaifns')
        expected = 9
        self.assertEqual(actual, expected)
    def test_asciisubstringinterface2(self):
        actual = asciiSub('aTGATb')
        expected = 1
        self.assertEqual(actual, expected)
    def test_asciisubstringinterface3(self):
        actual = asciiSub('')
        expected = -1
        self.assertEqual(actual, expected)
    def test_asciisubstringinterface4(self):
        actual = asciiSub('oifnaoifnanfanifnaonf')
        expected = -1
        self.assertEqual(actual, expected)
    #testing common subsequence interface
    def test_commonsubsequenceinterface(self):
        actual = longestCommonSubsequence('TGATCTAGCTAGCTGATCGA','TGACTGACGTGTGCATGC',len('TGATCTAGCTAGCTGATCGA'),len('TGACTGACGTGTGCATGC'))
        expected = 'TGACTGCTGTGATG'
        self.assertEqual(actual, expected)
    
unittest.main()