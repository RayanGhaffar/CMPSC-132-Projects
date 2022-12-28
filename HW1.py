# HW1
# REMINDER: The work in this assignment must be your own original work and must be completed alone.


from itertools import permutations
from pickle import TRUE


def rectangle(perimeter,area):
    """
        >>> rectangle(14, 10)
        5
        >>> rectangle(12, 5)
        5
        >>> rectangle(25, 25)
        False
        >>> rectangle(50, 100)
        20
        >>> rectangle(11, 5)
        False
        >>> rectangle(11, 4)
        False
    """
    #- YOUR CODE STARTS HERE
    """Solving for the L and W can be done by using alegbra. Due to Python Syntax not allowing variables and wanting 
    simpler code in the function, I will explain how this function works using this comment -- skipping over lots of 
    unneccesary code and steps. P = 2X + 2Y, this algorithm will solve for Y in terms of X so that (P-2x)/2 = Y, plug Y 
    into the Area equation of A = X * Y to get a quadratic in terms of X. Once there, the Quadratic Formula will be used
    to solve for the roots. The final polynomial will always be -x^2 + (P/2)x - A. An if statement is in place to
    determine if there are 2 roots - the 2 different side lengths. The method will return False if 0 or 1 root is found.
    """
    #Creates the variables used in the quadratic formula
    a, b, c = -1, perimeter/2, -area

    #Returns false if only one side root existent, only 1 positive value side
    discrim= b**(2) - 4*a*c
    if discrim<1:
        return False

    #Determines the length and width
    x, y = (-b-(discrim **(1/2)))/(2*a), (-b+(discrim **(1/2)))/(2*a)

    #Determines if the values are postiive and integers
    if x>0 and y>0 and x.is_integer() and y.is_integer():
        x = int(x)
        y = int(y)
        #Returns the correct solution or false if not a real rectangle
        if x> y:
            return x
        return y
    return False

    


def to_decimal(oct_num):
    """
        >>> to_decimal(237) 
        159
        >>> to_decimal(35) 
        29
        >>> to_decimal(600) 
        384
        >>> to_decimal(420) 
        272
    """
    #- YOUR CODE STARTS HERE
    """ To convert a octal system value to a dec system value, this algorithm will use module division to find the 
    lowest sequenced value in a number, multiply it by the respective power of 8, then use floor division to remove it 
    from the integer. A while loop will be used to iterate through all values in the oct value until a final answer for
    the dec value is found
    """
    #Create variables
    dec_num, i=0, 0

    #while loop iterates throught the value
    while oct_num>0:
        dec_num += (oct_num % 10) * (8 ** (i))
        oct_num = oct_num// 10
        i+=1
    return dec_num


def largeFactor(num):
    """
        >>> largeFactor(15) # factors are 1, 3, 5
        5
        >>> largeFactor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
        40
        >>> largeFactor(13) # factor is 1 since 13 is prime
        1
    """
    #- YOUR CODE STARTS HERE
    """Method uses a for loop to iterate through all values from 2-num/2. Returns the largest factor. No need to check 
    for 1 or values larger than num/2 as they will be decimals and all values, even primes, have 1 as the smallest factor
    """
    #Creates variable
    max = 1
    for i in range(2, num//2 + 1):
        if num % i == 0:
            max =i

    return max



def hailstone(num):
    """
        >>> hailstone(10)
        [10, 5, 16, 8, 4, 2, 1]
        >>> hailstone(1)
        [1]
        >>> hailstone(27)
        [27, 82, 41, 124, 62, 31, 94, 47, 142, 71, 214, 107, 322, 161, 484, 242, 121, 364, 182, 91, 274, 137, 412, 206, 103, 310, 155, 466, 233, 700, 350, 175, 526, 263, 790, 395, 1186, 593, 1780, 890, 445, 1336, 668, 334, 167, 502, 251, 754, 377, 1132, 566, 283, 850, 425, 1276, 638, 319, 958, 479, 1438, 719, 2158, 1079, 3238, 1619, 4858, 2429, 7288, 3644, 1822, 911, 2734, 1367, 4102, 2051, 6154, 3077, 9232, 4616, 2308, 1154, 577, 1732, 866, 433, 1300, 650, 325, 976, 488, 244, 122, 61, 184, 92, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        >>> hailstone(7)
        [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        >>> hailstone(19)
        [19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    """
    #- YOUR CODE STARTS HERE
    """Returns a list of the hail stone sequence, where odds are multiplied by 3n+1 and evens are divided by 2 until 
    a result of n = 1 is reached."""
    
    #creates list 
    lst = [num]

    while lst[-1] != 1:
        #determines if even or odd
        if lst[-1] % 2 == 0:
            lst.append(lst[-1]//2)
        else:
            lst.append(lst[-1] * 3 + 1)
    return lst




def remove(txt):
    """
        >>> remove("Dots...................... many dots..X")
        ('Dots                       many dots  X', {'.': 24})
        >>> data = remove("I like chocolate cake!!(!! It's the best flavor..;.$ for real")
        >>> data[0]
        'I like chocolate cake      It s the best flavor      for real'
        >>> data[1]
        {'!': 4, '(': 1, "'": 1, '.': 3, ';': 1, '$': 1}
        
    """
    #- YOUR CODE STARTS HERE
    
    #Creates values and list
    lst = list(txt)
    dic ={}

    for i in range(len(lst)):
        #determines if it is a letter or not, if not then it will be removed. Spaces are ignored
        if lst[i].isalpha() == False and lst[i] != ' ':
            #determines if this is the first instance of the punc. mark or to add to the counter
            if lst[i] in dic:
                dic[lst[i]] += 1
            else:
                dic[lst[i]]=1
            #cleares the character out 
            lst[i]= ' '

    return ''.join(lst), dic



        




def translate(translation_file, msg):
    """
        >>> translate('abbreviations.txt', 'c u in 5.')
        'see you in 5.'
        >>> translate('abbreviations.txt', 'gr8, cu')
        'great, see you'
        >>> translate('abbreviations.txt', 'b4 lunch, luv u!')
        'before lunch, love you!'
    """
    # Open file and read lines into one string all the way to the end of the file
    with open(translation_file) as file:   
        contents = file.readlines()

    #- YOUR CODE STARTS HERE

    #creates dictionary
    d = {}

    # Splits into multiple messages each with an index
    msgs = msg.split(', ')

    #For loop to assign the key words to the dictionary
    for i in range(len(contents)):
        #Creates a temporary list to hold the values, then assigns them to the dictionary. Removes the \n and =
        lst = contents[i].strip('\n').split('=')
        d[lst[0]] = lst[1]     

    #for loop to change values in the msg. Iterates through each message
    for i in range(len(msgs)):
        #Temp Ensures that only the word that needs to be translated is altered. Splits the each message into indiv words
        temp = msgs[i].split(' ')
        
        # for loop iterates through each indiv. word (value in temp) and uses the dictionary to replace words as needed
        for j in range (len(temp)):
            #if statement checks if the ending character is a puncuation and will ignore if if necessary
            ch = temp[j][-1]
            flag = False
            if ch in '.?!,;:':
                temp[j]= temp[j].strip(ch)
                flag = True

            #checks if the word is an abbreviation in the dictionary and will sub it out if it is
            if temp[j] in d:
                temp[j] = d[temp[j]]

            #adds the puncuation back in if the word had one
            if flag:
                temp[j] += ch

        #rejoins the words back together with the space
        msgs[i] = ' '.join(temp)
    
    #Joins message back to string
    return ', '.join(msgs)
   



    




def addToTrie(trie, word):
    """      
        >>> trie_dict = {'a' : {'word' : True, 'p' : {'p' : {'l' : {'e' : {'word' : True}}}}, 'i' : {'word' : True}}} 
        >>> addToTrie(trie_dict, 'art')
        >>> trie_dict
        {'a': {'word': True, 'p': {'p': {'l': {'e': {'word': True}}}}, 'i': {'word': True}, 'r': {'t': {'word': True}}}}
        >>> addToTrie(trie_dict, 'moon') 
        >>> trie_dict
        {'a': {'word': True, 'p': {'p': {'l': {'e': {'word': True}}}}, 'i': {'word': True}, 'r': {'t': {'word': True}}}, 'm': {'o': {'o': {'n': {'word': True}}}}}
    """
    #- YOUR CODE STARTS HERE

    #creates a variable that will hold letters, used for counter purposes
    ch = ''
    #For loop goes through each letter of word
    for letter in word:
        #if the value is not already there, a blank value is assigend to the key,
        if letter not in trie:
            trie[letter] = {}

        #Accesses the next level of letters
        trie = trie[letter]

        #ch gets the new letter, when ch has all the letters in the word, the word is complete
        ch += letter
        if ch == word:
            trie['word'] = True 

            




def createDictionaryTrie(file_name):
    """        
        >>> trie = createDictionaryTrie("words.txt")
        >>> trie == {'b': {'a': {'l': {'l': {'word': True}}, 't': {'s': {'word': True}}}, 'i': {'r': {'d': {'word': True}},\
                     'n': {'word': True}}, 'o': {'y': {'word': True}}}, 't': {'o': {'y': {'s': {'word': True}}},\
                     'r': {'e': {'a': {'t': {'word': True}}, 'e': {'word': True}}}}}
        True
    """
    # Open file and read lines into one string all the way to the end of the file
    with open(file_name) as file:   
        contents = file.readlines()

    #- YOUR CODE STARTS HERE
    #Creates a trie dictionary to be used in this function
    d = {}
    
    #Creates a holder variable that will be used to remove the \n of a word
    ch = ''

    #For loop iterates through the contents list
    for word in contents:
        #Checks if the word has a \n, the last word doesn't. Removes the \n
        if word[-1:] == '\n':
            ch = word[:-1]
        #If the word doesn't have the \n, then the value is normal
        else:
            ch = word
        #calls upon the function, uses .lower() to make all lowercase
        addToTrie(d, ch.lower())
    return d


    




def wordExists(trie, word):
    """
        >>> trie_dict = {'a' : {'word' : True, 'p' : {'p' : {'l' : {'e' : {'word' : True}}}}, 'i' : {'word' : True}}} 
        >>> wordExists(trie_dict, 'armor')
        False
        >>> wordExists(trie_dict, 'apple')
        True
        >>> wordExists(trie_dict, 'apples')
        False
        >>> wordExists(trie_dict, 'a')
        True
        >>> wordExists(trie_dict, 'as')
        False
        >>> wordExists(trie_dict, 'tt')
        False
    """
    #- YOUR CODE STARTS HERE

    #Counter to limit and ensure that a True isn't accidentalyl returned if a word within in a word
    # is contained. Ex: 'A' should be true, 'armor' should not
    counter =len(word)
    
    #for loop iterates through the word
    for letter in word:
        #If the letter is not matched, False is returned
        if letter not in trie:
            return False
        #If the value True at the end of a word is reached, True is returned
        if trie[letter] and counter==1:
            return True   
        #If nothing is returned, move into the next level of the dictionary 
        counter -= 1
        trie = trie[letter]
        




if __name__=='__main__':
    import doctest
    doctest.run_docstring_examples(rectangle, globals(), name='HW1',verbose=True) # replace rectangle for the function name you want to test
