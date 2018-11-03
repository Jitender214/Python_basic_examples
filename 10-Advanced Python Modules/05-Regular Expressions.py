import re

patterns = ['term1','term2']

text = 'this is a string with term1, but not the other term'

for pattern in patterns:
    print('Searcing for "%s" in: \n "%s"' %(pattern,text))
    if re.search(pattern , text):
        print("\n ")
        print("Match was found")
    else:
        print("\n ")
        print("Match was not found")

match = re.search(patterns[0],text)
print(match.start())
print(match.end())

split_term = '@'
pharse = "what is your email , is it hello@gmail.com"
print(re.split(split_term,pharse))
print(re.search(split_term,pharse))


print(re.findall('match','here is one match, another match'))

def multi_read(patterns1,pharse1):
    for pattern in patterns1:
        print('Searching for pharse using re check: %r' %pattern)
        print(re.findall(pattern,pharse1))
        print("\n")

test_pharse = 'sdsd....sssddd....sdddsddd...dsds.....dssss....sdddd'
test_patterns = ['sd*','sd+','sd?','sd{3}','sd{2,3}']

multi_read(test_patterns,test_pharse)

test_pharse1 = 'This is a string! but it has punctuation. how can we remove?'
print(re.findall('[^!.? ]+',test_pharse1))
#Use [^!.?] to check for matches that are not a !.? or space. add the + to check that the match appears at least once


def multi_re_find(patterns1,pharse1):
    for pattern in patterns1:
        print('Searching for pharse using re check: %r' %pattern)
        print(re.findall(pattern,pharse1))
        print("\n")

test_pharse2 = 'This is an example sentense. Lets see if we can find some letters'

test_patterns2 = ['[a-z]+','[A-z]+','[a-zA-Z]+','[A-Z][a-z]+']
multi_re_find(test_patterns2,test_pharse2)


test_pharse3 = 'This is a string with some numbers 1233 and a symbol #hashing'

test_patterns3 = [r'\d+',r'\D+',r'\s+',r'\S+',r'\w+',r'\W+']
multi_re_find(test_patterns3,test_pharse3)



