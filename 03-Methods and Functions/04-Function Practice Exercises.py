#write a function that returns the lesser of two given numbers if both are even, but
#returns the greater if one or both numbers are odd.
def lesser_of_two_evens(a,b):
    #both numbers are even
    if a%2==0 and b%2==0:
        if a>b:
            result = b
        else:
            result = a
    else:
    #one or both numbers are even
        if a > b:
            result = a
        else:
            result = b
    return result

def myfunc(a,b):
    #both numbers are even
    if a%2==0 and b%2==0:
        print(min(a,b))
        #return min(a,b) this also we can do
    else:
    #one or both numbers are even
        print(max(a, b))
        #return max(a, b)

#write a function takes a two-word string and returns True if both words begin with same letter else false
def two_words_string(text):
    word_list = text.split();
    print(word_list)
    first = word_list[0]
    second = word_list[1]
    print(first,second)
    if first[0] == second[0]:
        return True
    else:
        return False
    # return first[0] == second[0]:


def two_words_string(text):
    word_list = text.split();
    print(word_list)
    return word_list[0][0] == word_list[1][0]

#Given two intergers,returns True if the sum of the integers is 20 or if one od the integer is 20
#if not return False
def makes_twenty(n1,n2):
    if n1+n2 == 20:
        return True
    elif n1 == 20 or n2 ==20:
        return True
    else:
        return False

def makes_twenty(n1,n2):
    return n1+n2 == 20 or n1 == 20 or n2 ==20

#Write a function that capitalizes  the first and fourth letters of a name macdonald
def old_macdonald(name):
    first_letter = name[0].upper()
    fourth_letter = name[3].upper()
    between_letter = name[1:3]
    between_letter1 = name[3:]
    return first_letter+between_letter+fourth_letter+between_letter1

def old_macdonald(name):
    first_half = name[:3]
    second_half = name[3:]
    return first_half.capitalize()+second_half.capitalize()
    #capitalize() changes the first letter of the word into Capital

#retun the given sentence in reverse
def reverse_words(text):
    words_list = text.split()
    print (words_list)
    reversed_list = words_list[::-1]
    #return reversed_list # this will give us the list[], we need to use join to get actual reversed string
    return ' '.join(reversed_list)

mylist = ['a','b','c']
print("after joining -- " + '--'.join(mylist))

#given an integer n,return True if n is within 10 of either 100 or 200
def absolute_num(n):
    return (abs(100-n) <=10) or (abs(200-n)<=10)

#Level 2 Porblems

#given a list of ints, return True if the array contains a 3 next t a 3 somewhere
def has_33(num):
    for i in range(0,len(num)-1):
        if num[i] == 3 and num[i+1]==3:
            return True
    return False
#has_33([1,3,3]) - True
#has_33([1,3,1,3]) - False

#given three integers between 1 t o11,if their sum is less than or equal to 21 then return their sum,
#if their sum is exceeds 21 and there's in an eleven in,reduce the total sum by 10.
#finally, if sum(even after adjustment) exceeds 21, return BUST
def black_jack(n1,n2,n3):
    sum = n1+n2+n3
    if sum <= 21:
        return sum
    elif sum>21 and n1==11 or n2==11 or n3==11:
        return sum-10
    else:
        return 'Bust'

    #black_jack(5,6,7),18
    #black_jack(9,9,9) - 'Bust'
    #black_jack(9,9,11) - 19
def black_jack(n1,n2,n3):
    if sum([n1,n2,n3]) <= 21:
        return sum([n1,n2,n3])
    elif 11 in [n1,n2,n3] and sum([n1,n2,n3])< 31:
        return sum([n1,n2,n3])-10
    else:
        return 'Bust'









