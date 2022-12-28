# HW3
# REMINDER: The work in this assignment must be your own original work and must be completed alone.

class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                          

#=============================================== Part I ==============================================

class Stack:
    '''
        >>> x=Stack()
        >>> x.pop()
        >>> x.push(2)
        >>> x.push(4)
        >>> x.push(6)
        >>> x
        Top:Node(6)
        Stack:
        6
        4
        2
        >>> x.pop()
        6
        >>> x
        Top:Node(4)
        Stack:
        4
        2
        >>> len(x)
        2
        >>> x.peek()
        4
    '''
    def __init__(self):
        self.top = None
    
    def __str__(self):
        temp=self.top
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out='\n'.join(out)
        return ('Top:{}\nStack:\n{}'.format(self.top,out))

    __repr__=__str__


    def isEmpty(self):
        # YOUR CODE STARTS HERE
        #If the top value is none, that means there are no value in the Stack
        if self.top is None:
            return True
        return False

    def __len__(self): 
        # YOUR CODE STARTS HERE
        #isEmpty is used to save unneccary variable creation if the stack is empty
        if self.isEmpty():
            return 0

        #Cycles through the linked list and counts the number of nodes
        counter = 0
        current = self.top
        while current is not None:
            counter+=1 
            current = current.next
        return counter

    def push(self,value):
        # YOUR CODE STARTS HERE
        #Creates a new node, adds it to Stack, determines if it is the first. Always makes it the top
        nn = Node(value)
        if self.isEmpty():
            nn.next = None
        else:
            nn.next = self.top
        self.top = nn


     
    def pop(self):
        # YOUR CODE STARTS HERE
        #Creates a temporary Node to hold the top Node. Unlinks the top Node, and returns its value
        if self.isEmpty() == False:
            tempNode = self.top
            self.top = self.top.next
            return tempNode.value

    def peek(self):
        # YOUR CODE STARTS HERE
        #returns the top value of the top node
        return self.top.value


#=============================================== Part II ==============================================

class Calculator:
    def __init__(self):
        self.__expr = None


    @property
    def getExpr(self):
        return self.__expr

    def setExpr(self, new_expr):
        if isinstance(new_expr, str):
            self.__expr=new_expr
        else:
            print('setExpr error: Invalid expression')
            return None

    def _isNumber(self, txt):
        '''
            >>> x=Calculator()
            >>> x._isNumber(' 2.560 ')
            True
            >>> x._isNumber('7 56')
            False
            >>> x._isNumber('2.56p')
            False
        '''
        # YOUR CODE STARTS HERE
        #try/except will try to cast txt as a float, returns true if works, false if it doesn't
        try:
            x = float(txt)
            return True
        except:
            return False

    #split converts a strong input into a uniform input for the calculator, without unnecceary spaces
    def _split(self, txt):
        #list holds the values, and gets the first value
        lst = []
        #appends to the list by removing spaces from txt, received help by LA Shivani to use a for loop
        # for removing spaces, original idea was .replace() but was told to not do that.
        #Also combines multip digit numbers
        for i in range(len(txt)):
            if txt[i] != ' ':
                if self._isNumber(txt[i]):
                    varStr = txt[i]
                    j=i+1
                    while j<len(txt) and self._isNumber(txt[j]):
                        varStr += txt[j]
                        txt = txt[:j] + ' ' +txt[j+1:]
                        j+=1
                    i+= len(varStr) -1
                    lst.append(float(varStr))
                elif txt[i] == '.':
                    lst.append('.')
                else:
                    lst.append(txt[i])
        
        #Allows for expression with no operands to work by addings parenthesis to lone numbers
        lst.append(')')
        lst.insert(0, '(')

        #Combines digits in a decimal. Without this, 5.34 is seen as [5.0, 3.0, 4.0]
        #iterator variable used to cycle through a changing list
        i = 0
        while i <len(lst):
            if lst[i] =='.':
                lst = self.findFloat(lst, i)
            i+=1
        #Determines a negative number and combines indices
        lst = self._findNegative(lst)
        
        #Removes inserted parentheses from earlier as findFloat is complete
        del lst[0]
        del lst[-1]

        #Checks validations, returns lst or a False from validation
        if not self.validation(lst):
            return None
        return lst

    #Combines adjacent values in a list into a decimal if supposed to. Done before validation to avoid error
    def findFloat(self, lst, i):
        #Makes a list of indices to skip when returning
        skipList=[]

        # i = index of decimal, i-1 = index left decimal. Puts a leading 0 if there isn't a val there
        if not self._isNumber(lst[i-1]):
            i+=1
            lst.insert(i-1, 0.0)

        #Adds the current decimal as an index to skip
        skipList.append(i)

        #Gets the end of number, then concatenates them to a string, then casts as float       
        if i+1<len(lst) and self._isNumber(lst[i+1]):
            #Adds the value with proper power of 10 by finding how far it is from the decimal place (j-i-1)
            skipList.append(i+1)
            lst[i-1] = str(int(lst[i-1])) +  '.' + str(int(lst[i+1]))

        #Creates a new list of values to hold non-skipped values
        lst2=[]
        #assigns all of lst except the values after a decimal as we already combined them into a sum
        for j in range (len(lst)):
            if j not in skipList:
                lst2.append(lst[j])
        return lst2

    def validation(self, lst):
        #Checks for missing operators and operands. There should always be 1 more operand than operator
        numCounter, operatorCounter =0,0
        #Finds the number of parenthesises, each open should have a close. Combined into one loop
        openParen, closeParen = 0,0
        #also by the way my program views parenthesis, implied multiplication automatically doesn't work
        
        #Checks consecutive numbers and operators. Critical in niche scenarios where counters don't work
        for i in range(len(lst)-1):
            #If statements are broken up for readibility. 
            #checks adjacent floats
            if self._isNumber(lst[i]) and self._isNumber(lst[i+1]):
                #print('consecutive numbers')
                return False
            #checks adjacent operators
            elif isinstance(lst[i], str) and isinstance(lst[i+1], str) and lst[i] in '^*/+-' and lst[i+1] in '^*/+-':
                #print('consecutive operators') 
                return False

        for i in lst:
            #Checks for unsupported characters
            if not self._isNumber(i) and  i not in '()^*/+-. ':
                #print('Invalid charater', i)
                return False
            elif self._isNumber(i):
                numCounter+=1
            elif i in '^*/+-':
                operatorCounter+=1
            elif i =='(':
                openParen +=1
            elif i == ')' and closeParen<openParen:
                closeParen +=1
            elif i ==')' and closeParen>=openParen or '(' not in lst[:lst.index(i)]:
                #print("Parenthesis Error")
                return False
        #Checks for unmatched operators/numbers and consectuvies 
        if numCounter != operatorCounter+1:
            #print('Mismatched Operators and Operands')
            return False

        return True

    
    #Checks through a list (expression input) for numbers that should be negative. @returns new list
    def _findNegative(self, lst):
        #list of indexs to skip. Uses a skip instead because delete messes with indexing and loops
        skipList=[] 
        for i in range(len(lst)-1):
            if i> 0 and lst[i] == '-' and self._isNumber(lst[i+1]) and isinstance(lst[i-1], str) and lst[i-1] in '(^*/+-':
                lst[i+1] = -1 *lst[i+1]
                skipList.append(i)
            elif i ==0 and lst[i] == '-' and self._isNumber(lst[i+1]):
                lst[i+1] = -1 *lst[i+1]
                skipList.append(i)
            
        #iterates through the lst and assigns needed indices to a new list
        lst2 = []
        for i in range(len(lst)):
            if i not in skipList:
                lst2.append(lst[i])

        return lst2
        
    
    def _getPostfix(self, txt):
        '''
            Required: _getPostfix must create and use a Stack for expression processing
            >>> x=Calculator()
            >>> x._getPostfix('     2 ^       4')
            '2.0 4.0 ^'
            >>> x._getPostfix('          2 ')
            '2.0'
            >>> x._getPostfix('2.1        * 5        + 3       ^ 2 +         1 +             4.45')
            '2.1 5.0 * 3.0 2.0 ^ + 1.0 + 4.45 +'
            >>> x._getPostfix('2*5.34+3^2+1+4')
            '2.0 5.34 * 3.0 2.0 ^ + 1.0 + 4.0 +'
            >>> x._getPostfix('2.1 * 5 + 3 ^ 2 + 1 + 4')
            '2.1 5.0 * 3.0 2.0 ^ + 1.0 + 4.0 +'
            >>> x._getPostfix('( .5 )')
            '0.5'
            >>> x._getPostfix ('( ( 2 ) )')
            '2.0'
            >>> x._getPostfix ('2 * (           ( 5 +-3 ) ^ 2 + (1 + 4 ))')
            '2.0 5.0 -3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix ('(2 * ( ( 5 + 3) ^ 2 + (1 + 4 )))')
            '2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix ('((2 *((5 + 3  ) ^ 2 + (1 +4 ))    ))')
            '2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix('2* (       -5 + 3 ) ^2+ ( 1 +4 )')
            '2.0 -5.0 3.0 + 2.0 ^ * 1.0 4.0 + +'

            # In invalid expressions, you might print an error message, adjust doctest accordingly
            # If you are veryfing the expression in calculate before passing to postfix, this cases are not necessary

            >>> x._getPostfix('2 * 5 + 3 ^ + -2 + 1 + 4')
            >>> x._getPostfix('     2 * 5 + 3  ^ * 2 + 1 + 4')
            >>> x._getPostfix('2    5')
            >>> x._getPostfix('25 +')
            >>> x._getPostfix(' 2 * ( 5      + 3 ) ^ 2 + ( 1 +4 ')
            >>> x._getPostfix(' 2 * ( 5 + 3 ) ^  2 + ) 1 + 4 (')
            >>> x._getPostfix('2 *      5% + 3       ^ + -2 +1 +4')
        '''

        # YOUR CODE STARTS HERE
        postfixStack = Stack()  # method must use postfixStack to compute the postfix expression
        #creates variable that will hold the expression, txt uses split and will either be a
        #list or the Boolean False. If it's a list, program works as intended, False stops it
        postfix, txt = '', self._split(txt) 
        if txt is None:
            return None
        else:
            #Loops through the txt list
            for i in txt:
                #Assigns a number to postfix
                if self._isNumber(i):
                    postfix += str(i) + ' '
                #Assigns an operator to post fix stack. The stack is ordered in precedence
                elif i in '^*/+-(':
                    #While i does not have precedence in the stack, pop values
                    while not self._precedence(postfixStack, i):
                        postfix += postfixStack.pop() + ' '
                    #Once there is precedence, add the new operator
                    postfixStack.push(i)
                # ) has the lowest priority, ( can be added in directly tho
                elif i == ')':
                    #Pop until an open parenthesis is found, then pop the parenthesis but not into stack
                    while postfixStack.peek() != '(':
                        postfix += postfixStack.pop() + ' '
                    postfixStack.pop()
                    
                    
        #Pops remaining operators as operators at the end aren't popped because no precedence after        
        while not postfixStack.isEmpty():
            postfix += postfixStack.pop() +' '

        #Sets the final postFix expression and removes remaining space
        postfix= postfix.strip()    
        return postfix


    #used to determine if the current operator has precedence above all in the stack, ordered in 
    #precedence so we only need to evaluate the node the current top
    #Essentially, what's on the right is prioritized over whats on the left
    def _precedence(self, stack, ch):
        if not stack.isEmpty():
            #Checks each operand, returns false if there is higher precedence already in the stack
            if ch == '^' and stack.top.value in '^':
                return False
            elif ch in '*/' and stack.top.value in '^*/':
                return False
            elif ch in '+-' and stack.top.value in '^*/+-':
                return False
            elif ch == ')':
                return False

        #Means this new operand is the highest operator in precedence    
        return True

    @property
    def calculate(self):
        '''
            calculate must call _getPostfix
            calculate must create and use a Stack to compute the final result as shown in the video lecture
            
            >>> x=Calculator()
            >>> x.setExpr('4        + 3 -       2')
            >>> x.calculate
            5.0
            >>> x.setExpr('-2 +          3.5')
            >>> x.calculate
            1.5
            >>> x.setExpr('      4 +           3.65  - 2        / 2')
            >>> x.calculate
            6.65
            >>> x.setExpr('23 / 12 - 223 + 5.25      * 4 * 3423')
            >>> x.calculate
            71661.91666666667
            >>> x.setExpr('2-3*4')
            >>> x.calculate
            -10.0
            >>> x.setExpr('7^2^3')
            >>> x.calculate
            5764801.0
            >>> x.setExpr(' 3 * ((( 10 - 2*3 )) )')
            >>> x.calculate
            12.0
            >>> x.setExpr('      8 / 4 * (3 - 2.45 * ( 4   - 2 ^ 3 )       ) + 3')
            >>> x.calculate
            28.6
            >>> x.setExpr('2 * ( 4 +        2 * (         5 - 3 ^ 2 ) + 1 ) + 4')
            >>> x.calculate
            -2.0
            >>> x.setExpr(' 2.5 +         3 * (2 + ( 3.0) * ( 5^2-2 * 3 ^ ( 2 )         ) * ( 4 ) ) * ( 2 / 8 + 2 * ( 3 - 1 /3 ) ) - 2 / 3^ 2')
            >>> x.calculate
            1442.7777777777778
            

            # In invalid expressions, you might print an error message, but code must return None, adjust doctest accordingly
            >>> x.setExpr(" 4 ++ 3+ 2") 
            >>> x.calculate
            >>> x.setExpr("4  3 +2")
            >>> x.calculate
            >>> x.setExpr('( 2 ) * 10 - 3 *( 2 - 3 * 2 ) )')
            >>> x.calculate
            >>> x.setExpr('( 2 ) * 10 - 3 * / ( 2 - 3 * 2 )')
            >>> x.calculate
            >>> x.setExpr(' ) 2 ( *10 - 3 * ( 2 - 3 * 2 ) ')
            >>> x.calculate
            >>> x.setExpr('(    3.5 ) ( 15 )') 
            >>> x.calculate
            >>> x.setExpr('3 ( 5) - 15 + 85 ( 12)') 
            >>> x.calculate
            >>> x.setExpr("( -2/6) + ( 5 ( ( 9.4 )))") 
            >>> x.calculate
        '''

        if not isinstance(self.__expr,str) or len(self.__expr)<=0:
            print("Argument error in calculate")
            return None

        calcStack = Stack()   # method must use calcStack to compute the  expression

        # YOUR CODE STARTS HERE
        #Makes a string of the new postfix expression and splits to list for easier traversal and spacing
        postfix = self._getPostfix(self.__expr)
        if postfix is None:
            return None
        postfix = postfix.split()
    
        for i in postfix:
            #pushes numbers to stack
            if self._isNumber(i):
                calcStack.push(float(i))
            #Calculates using operators
            else:
                #Creates variables to hold the values
                b = calcStack.pop()
                a = calcStack.pop()
                if i == '^':
                    calcStack.push(a ** b)
                elif i == '*':
                    calcStack.push(a*b)
                #Exception for division by 0 
                elif i == '/':
                    if b==0:
                        return None
                    calcStack.push(a/b)
                elif i == '+':
                    calcStack.push(a+b)
                elif i =='-':
                    calcStack.push(a-b)
                else:
                    return None
        #returns the value, only node in stack
        return calcStack.top.value
        

#=============================================== Part III ==============================================

class AdvancedCalculator:
    '''
        >>> C = AdvancedCalculator()
        >>> C.states == {}
        True
        >>> C.setExpression('a = 5;b = 7 + a;a = 7;c = a + b;c = a * 0;return c')
        >>> C.calculateExpressions() == {'a = 5': {'a': 5.0}, 'b = 7 + a': {'a': 5.0, 'b': 12.0}, 'a = 7': {'a': 7.0, 'b': 12.0}, 'c = a + b': {'a': 7.0, 'b': 12.0, 'c': 19.0}, 'c = a * 0': {'a': 7.0, 'b': 12.0, 'c': 0.0}, '_return_': 0.0}
        True
        >>> C.states == {'a': 7.0, 'b': 12.0, 'c': 0.0}
        True
        >>> C.setExpression('x1 = 5;x2 = 7 * ( x1 - 1 );x1 = x2 - x1;return x2 + x1 ^ 3')
        >>> C.states == {}
        True
        >>> C.calculateExpressions() == {'x1 = 5': {'x1': 5.0}, 'x2 = 7 * ( x1 - 1 )': {'x1': 5.0, 'x2': 28.0}, 'x1 = x2 - x1': {'x1': 23.0, 'x2': 28.0}, '_return_': 12195.0}
        True
        >>> print(C.calculateExpressions())
        {'x1 = 5': {'x1': 5.0}, 'x2 = 7 * ( x1 - 1 )': {'x1': 5.0, 'x2': 28.0}, 'x1 = x2 - x1': {'x1': 23.0, 'x2': 28.0}, '_return_': 12195.0}
        >>> C.states == {'x1': 23.0, 'x2': 28.0}
        True
        >>> C.setExpression('x1 = 5 * 5 + 97;x2 = 7 * ( x1 / 2 );x1 = x2 * 7 / x1;return x1 * ( x2 - 5 )')
        >>> C.calculateExpressions() == {'x1 = 5 * 5 + 97': {'x1': 122.0}, 'x2 = 7 * ( x1 / 2 )': {'x1': 122.0, 'x2': 427.0}, 'x1 = x2 * 7 / x1': {'x1': 24.5, 'x2': 427.0}, '_return_': 10339.0}
        True
        >>> C.states == {'x1': 24.5, 'x2': 427.0}
        True
        >>> C.setExpression('A = 1;B = A + 9;C = A + B;A = 20;D = A + B + C;return D - A')
        >>> C.calculateExpressions() == {'A = 1': {'A': 1.0}, 'B = A + 9': {'A': 1.0, 'B': 10.0}, 'C = A + B': {'A': 1.0, 'B': 10.0, 'C': 11.0}, 'A = 20': {'A': 20.0, 'B': 10.0, 'C': 11.0}, 'D = A + B + C': {'A': 20.0, 'B': 10.0, 'C': 11.0, 'D': 41.0}, '_return_': 21.0}
        True
        >>> C.states == {'A': 20.0, 'B': 10.0, 'C': 11.0, 'D': 41.0}
        True
        >>> C.setExpression('A = 1;B = A + 9;2C = A + B;A = 20;D = A + B + C;return D + A')
        >>> C.calculateExpressions() is None
        True
        >>> C.states == {}
        True
    '''
    def __init__(self):
        self.expressions = ''
        self.states = {}

    def setExpression(self, expression):
        self.expressions = expression
        self.states = {}

    def _isVariable(self, word):
        '''
            >>> C = AdvancedCalculator()
            >>> C._isVariable('volume')
            True
            >>> C._isVariable('4volume')
            False
            >>> C._isVariable('volume2')
            True
            >>> C._isVariable('vol%2')
            False
        '''
        # YOUR CODE STARTS HERE
        if len(word) >0 and word[0].isalpha() and word.isalnum():
            return True
        return False
       

    def _replaceVariables(self, expr):
        '''
            >>> C = AdvancedCalculator()
            >>> C.states = {'x1': 23.0, 'x2': 28.0}
            >>> C._replaceVariables('1')
            '1'
            >>> C._replaceVariables('105 + x')
            >>> C._replaceVariables('7 * ( x1 - 1 )')
            '7 * ( 23.0 - 1 )'
            >>> C._replaceVariables('x2 - x1')
            '28.0 - 23.0'
        '''
        # YOUR CODE STARTS HERE
        flag = False
        for key in self.states:
            if key in expr:
                flag = True
                expr= expr.replace(key, str(self.states[key]))
                #expr = expr[:expr.index(key)] + str(self.states[key]) + expr[expr.index(key)+len(str(expr.index(key)))+1:]

        #Returns true if the expression is a value or an expression that was correctly replaced  
        if expr.isnumeric() or flag:
            return expr
        return None
        
    def calculateExpressions(self):
        self.states = {} 
        calcObj = Calculator()     # method must use calcObj to compute each expression
        # YOUR CODE STARTS HERE
        #Create dictionary and splits expressions into a list
        lst = self.expressions.split(';')
        d={}
        #Make a second dictionary to obtain copies
        d2 = {}
        
        for i in lst:
            #Only gets values until the last as that is the return line
            if i!= lst[-1]:
                #Splits expression into parts 
                parts = i.split(' = ') #List ['a', '5']
                varName = parts[0]

                #returns None if not a valid variable name
                if not self._isVariable(varName):
                    self.states ={}
                    return None
                
                #Gets the expression, assigns to a dictionary, and replaces values using self.states
                #A new expression that has the variable replaced
                #Try/except for when an expression needs to be calcuated first
                try:
                    calcObj.setExpr(parts[1])
                    val = self._replaceVariables(calcObj.calculate)
                except:
                    val = self._replaceVariables(parts[1])
                    calcObj.setExpr(val)
                if calcObj.calculate is None:
                    self.states = {}
                    return None
                self.states[parts[0]] = calcObj.calculate
                #Adds self.states to the dictionary as a value
                d[i] = self.states
                
                #Copies the data to d2
                d2[i] = d[i].copy()

        #Returns d2 after calculating final value
        calcObj.setExpr(self._replaceVariables(lst[-1].strip('return ')))
        d2['_return_'] = calcObj.calculate
        return d2
        