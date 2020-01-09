''' regular expression
    A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
'''

''' search :only search with one instance of match'''

'''
findall	Returns a list containing all matches
search	Returns a Match object if there is a match anywhere in the string
split	Returns a list where the string has been split at each match
sub	Replaces one or many matches with a string
'''
import re
string='search this inside of this text'
a=re.search('this',string)
print(a) #<re.Match object; span=(7, 11), match='this'>
print(a.group()) #this
print(a.start()) #7
print(a.span()) #(7,11) start to end index match

#compile
# compile a regular expressions pattern and return a python object

''' findall : to search multiple instances of search'''
pattern=re.compile('this')
b=pattern.findall(string)
print(b) #['this', 'this']

''' full match : check sample with exact match with string'''
pattern2=re.compile('search this inside of this text')
c=pattern2.fullmatch(string)
print(c) #<re.Match object; span=(0, 31), match='search this inside of this text'>


''' match :matches one or more instance '''
string2='search this inside of this text extra part'
pattern3=re.compile('search this inside of this text')
d=pattern3.match(string2)
print(d)

#output:
#<re.Match object; span=(0, 31), match='search this inside of this text'>

''' regex101.com website'''
pattern4=re.compile(r"([a-zA-Z]).([a])")
e=pattern4.match(string)
print(e.group()) #sea
print(e.group(0)) #sea
print(e.group(1)) #s
print(e.group(2)) #a

#split() :returns a list where the string has been split at each match:
import re
str = "The rain in Spain"
x = re.split("\s", str) #\s white spaces
print(x)
#['The', 'rain', 'in', 'Spain']

#maxsplit :Split the string only at the first occurrence:
import re
str = "The rain in Spain"
x = re.split("\s", str, 1)
print(x)
#['The', 'rain in Spain']

#sub()
str = "The rain in Spain"
x = re.sub("\s", "9", str) #replace white space with 9
print(x)
#The9rain9in9Spain

#sub :replace only count times
str = "The rain in Spain"
x = re.sub("\s", "9", str, 2)
print(x)
#The9rain9in Spain

'''
.span() returns a tuple containing the start-, and end positions of the match.
.string returns the string passed into the function
.group() returns the part of the string where there was a match
'''

'''
[]	A set of characters	"[a-m]"	
\	Signals a special sequence (can also be used to escape special characters)	"\d"	
.	Any character (except newline character)	"he..o"	
^	Starts with	"^hello"	
$	Ends with	"world$"	
*	Zero or more occurrences	"aix*"	
+	One or more occurrences	"aix+"	
{}	Exactly the specified number of occurrences	"al{2}"	
|	Either or	"falls|stays"

'''

'''
\A	Returns a match if the specified characters are at the beginning of the string	"\AThe"	
\b	Returns a match where the specified characters are at the beginning or at the end of a word	r"\bain"
    r"ain\b"	
\B	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word	r"\Bain"
    r"ain\B"	
\d	Returns a match where the string contains digits (numbers from 0-9)	"\d"	
\D	Returns a match where the string DOES NOT contain digits	"\D"	
\s	Returns a match where the string contains a white space character	"\s"	
\S	Returns a match where the string DOES NOT contain a white space character	"\S"	
\w	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, 
    and the underscore _ character)	"\w"	
\W	Returns a match where the string DOES NOT contain any word characters	"\W"	
\Z	Returns a match if the specified characters are at the end of the string	"Spain\Z"	

'''