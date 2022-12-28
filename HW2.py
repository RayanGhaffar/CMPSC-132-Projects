# HW2
# REMINDER: The work in this assignment must be your own original work and must be completed alone.

from base64 import standard_b64decode
from operator import truediv
import random
from re import A, T
from unicodedata import name

class Course:
    '''
        >>> c1 = Course('CMPSC132', 'Programming in Python II', 3)
        >>> c2 = Course('CMPSC360', 'Discrete Mathematics', 3)
        >>> c1 == c2
        False
        >>> c3 = Course('CMPSC132', 'Programming in Python II', 3)
        >>> c1 == c3
        True
        >>> c1
        CMPSC132(3): Programming in Python II
        >>> c2
        CMPSC360(3): Discrete Mathematics
        >>> c3
        CMPSC132(3): Programming in Python II
        >>> c1 == None
        False
        >>> print(c1)
        CMPSC132(3): Programming in Python II
    '''
    def __init__(self, cid, cname, credits):
        # YOUR CODE STARTS HERE
        #initialized values
        self.cid = cid
        self.cname = cname
        self.credits = credits



    def __str__(self):
        # YOUR CODE STARTS HERE
        return f'{self.cid}({self.credits}): {self.cname}'

    __repr__ = __str__

    def __eq__(self, other):
        # YOUR CODE STARTS HERE
        #Returns false if other is None or the cids don't match
        if isinstance(other, Course) and self.cid == other.cid:
            return True
        return False
       



class Catalog:
    ''' 
        >>> C = Catalog()
        >>> C.courseOfferings
        {}
        >>> C._loadCatalog("cmpsc_catalog_small.csv")
        >>> C.courseOfferings
        {'CMPSC 132': CMPSC 132(3): Programming and Computation II, 'MATH 230': MATH 230(4): Calculus and Vector Analysis, 'PHYS 213': PHYS 213(2): General Physics, 'CMPEN 270': CMPEN 270(4): Digital Design, 'CMPSC 311': CMPSC 311(3): Introduction to Systems Programming, 'CMPSC 360': CMPSC 360(3): Discrete Mathematics for Computer Science}
        >>> C.removeCourse('CMPSC 360')
        'Course removed successfully'
        >>> C.courseOfferings
        {'CMPSC 132': CMPSC 132(3): Programming and Computation II, 'MATH 230': MATH 230(4): Calculus and Vector Analysis, 'PHYS 213': PHYS 213(2): General Physics, 'CMPEN 270': CMPEN 270(4): Digital Design, 'CMPSC 311': CMPSC 311(3): Introduction to Systems Programming}
        >>> isinstance(C.courseOfferings['CMPSC 132'], Course)
        True
    '''

    def __init__(self):
        # YOUR CODE STARTS HERE
        self.courseOfferings = {}

    def addCourse(self, cid, cname, credits):
        # YOUR CODE STARTS HERE
        if cid in self.courseOfferings:
            'Course already added'
        else: 
            self.courseOfferings[cid] = Course(cid, cname, credits)
            return 'Course added successfully'


    def removeCourse(self, cid):
        # YOUR CODE STARTS HERE
        if cid in self.courseOfferings:
            del self.courseOfferings[cid]
            return 'Course removed successfully'
        else: 
            return 'Course not found'

    def _loadCatalog(self, file):
        with open(file, "r") as f:
            course_info = f.read()
        # YOUR CODE STARTS HERE
        #Converts string into list, then gets indiviudal values of each line for key-value pair
        lst = course_info.split('\n')
        for str in lst:
            #uses indexing and splitting to get key and value
            self.addCourse(str.split(',')[0], str.split(',')[1], str.split(',')[2])

        


class Semester:
    '''
        >>> cmpsc131 = Course('CMPSC 131', 'Programming in Python I', 3)
        >>> cmpsc132 = Course('CMPSC 132', 'Programming in Python II', 3)
        >>> math230 = Course("MATH 230", 'Calculus', 4)
        >>> phys213 = Course("PHYS 213", 'General Physics', 2)
        >>> econ102 = Course("ECON 102", 'Intro to Economics', 3)
        >>> phil119 = Course("PHIL 119", 'Ethical Leadership', 3)
        >>> spr22 = Semester()
        >>> spr22
        No courses
        >>> spr22.addCourse(cmpsc132)
        >>> isinstance(spr22.courses['CMPSC 132'], Course)
        True
        >>> spr22.addCourse(math230)
        >>> spr22
        CMPSC 132; MATH 230
        >>> spr22.isFullTime
        False
        >>> spr22.totalCredits
        7
        >>> spr22.addCourse(phys213)
        >>> spr22.addCourse(econ102)
        >>> spr22.addCourse(econ102)
        'Course already added'
        >>> spr22.addCourse(phil119)
        >>> spr22.isFullTime
        True
        >>> spr22.dropCourse(phil119)
        >>> spr22.addCourse(Course("JAPNS 001", 'Japanese I', 4))
        >>> spr22.totalCredits
        16
        >>> spr22.dropCourse(cmpsc131)
        'No such course'
        >>> spr22.courses
        {'CMPSC 132': CMPSC 132(3): Programming in Python II, 'MATH 230': MATH 230(4): Calculus, 'PHYS 213': PHYS 213(2): General Physics, 'ECON 102': ECON 102(3): Intro to Economics, 'JAPNS 001': JAPNS 001(4): Japanese I}
    '''


    def __init__(self):
        # --- YOUR CODE STARTS HERE
        #dictionary stores courses that are taken in the semester
        self.courses = {}



    def __str__(self):
        # YOUR CODE STARTS HERE
        if len(self.courses) == 0:
            return 'No courses'
        else:
            return "; ".join(self.courses)

    __repr__ = __str__

    def addCourse(self, course):
        # YOUR CODE STARTS HERE
        #adds a course if it is not already in the semester dictionary
        if course.cid in self.courses:
            return 'Course already added'
        else:
            self.courses[course.cid] = course
        


    def dropCourse(self, course):
        # YOUR CODE STARTS HERE
        #removes a course if in the semester dictionary
        if course.cid in self.courses:
            del self.courses[course.cid]
        else:
            return 'No such course'

    @property
    def totalCredits(self):
        # YOUR CODE STARTS HERE
        #iterates through all course ids, gets the object/value, then gets the credits and adds it to the sum
        sum =0
        for course in self.courses:
            sum+= int(self.courses[course].credits)
        return sum
        
                      

    @property
    def isFullTime(self):
        # YOUR CODE STARTS HERE
        #returns true or false depending on if a semester has at least 12 credits
        if self.totalCredits >= 12:
            return True
        return False

    
class Loan:
    '''
        >>> import random
        >>> random.seed(2)  # Setting seed to a fixed value, so you can predict what numbers the random module will generate
        >>> first_loan = Loan(4000)
        >>> first_loan
        Balance: $4000
        >>> first_loan.loan_id
        17412
        >>> second_loan = Loan(6000)
        >>> second_loan.amount
        6000
        >>> second_loan.loan_id
        22004
        >>> third_loan = Loan(1000)
        >>> third_loan.loan_id
        21124
    '''
    

    def __init__(self, amount):
        # YOUR CODE STARTS HERE
        #initates attributes
        self.loan_id = self.__getloanID
        self.amount = amount


    def __str__(self):
        # YOUR CODE STARTS HERE
        return f'Balance: ${self.amount}'

    __repr__ = __str__


    @property
    def __getloanID(self):
        # YOUR CODE STARTS HERE
        #returns a random number that will be assigned to a seed
        return random.randint(10000, 99999)


class Person:
    '''
        >>> p1 = Person('Jason Lee', '204-99-2890')
        >>> p2 = Person('Karen Lee', '247-01-2670')
        >>> p1
        Person(Jason Lee, ***-**-2890)
        >>> p2
        Person(Karen Lee, ***-**-2670)
        >>> p3 = Person('Karen Smith', '247-01-2670')
        >>> p3
        Person(Karen Smith, ***-**-2670)
        >>> p2 == p3
        True
        >>> p1 == p2
        False
    '''

    def __init__(self, name, ssn):
        # YOUR CODE STARTS HERE
        #Initate attributes, _snn is marked as private 
        self.name = name
        self._ssn = ssn

    def __str__(self):
        # YOUR CODE STARTS HERE
        #returns the name and last four of ssn using lastFour function
        return f'Person({self.name}, ***-**-{self.lastFour}'
    
    @property
    def getInitials(self):
        #this function will use string splitting, indexing, and returns to find the initials of a name. Used in subclasses
        nameList= self.name.split(' ')
        initials=''
        for part in nameList:
            initials += part[0].lower()
        return initials


    @property
    def lastFour(self):
        #Finds the last four the snn using string slicing.
        #Placed in Super class as it uses get_ssn() which is private, and is to be used in subclasses
        
        return self.get_ssn()[-4:]
    

    __repr__ = __str__

    def get_ssn(self):
        # YOUR CODE STARTS HERE
        return self._ssn

    def __eq__(self, other):
        # YOUR CODE STARTS HERE
        if isinstance(other, Person) and self.get_ssn() == other.get_ssn():
            return True
        return False

class Staff(Person):
    '''
        >>> C = Catalog()
        >>> C._loadCatalog("cmpsc_catalog_small.csv")
        >>> s1 = Staff('Jane Doe', '214-49-2890')
        >>> s1.getSupervisor
        >>> s2 = Staff('John Doe', '614-49-6590', s1)
        >>> s2.getSupervisor
        Staff(Jane Doe, 905jd2890)
        >>> s1 == s2
        False
        >>> s2.id
        '905jd6590'
        >>> p = Person('Jason Smith', '221-11-2629')
        >>> st1 = s1.createStudent(p)
        >>> isinstance(st1, Student)
        True
        >>> s2.applyHold(st1)
        'Completed!'
        >>> st1.registerSemester()
        'Unsuccessful operation'
        >>> s2.removeHold(st1)
        'Completed!'
        >>> st1.registerSemester()
        >>> st1.enrollCourse('CMPSC 132', C)
        'Course added successfully'
        >>> st1.semesters
        {1: CMPSC 132}
        >>> s1.applyHold(st1)
        'Completed!'
        >>> st1.enrollCourse('CMPSC 360', C)
        'Unsuccessful operation'
        >>> st1.semesters
        {1: CMPSC 132}
    '''
    def __init__(self, name, ssn, supervisor=None):
        # YOUR CODE STARTS HERE
        #Calls constructor of Person superclass and initates a private attribute
        super().__init__(name, ssn)
        self._supervisor = supervisor


    def __str__(self):
        # YOUR CODE STARTS HERE
        #returns a formatted summary of the name (from the super class) and id (from the id property method))
        return f'Staff({self.name}, {self.id})'

    __repr__ = __str__


    @property
    def id(self):
        # YOUR CODE STARTS HERE
        #returns the id using the get_ssn() from the super class, and getInitials to find initials 
        initials = self.getInitials
        return f'905{initials}{super().lastFour}'
    
    @property   
    def getSupervisor(self):
        # YOUR CODE STARTS HERE
        return self._supervisor

    def setSupervisor(self, new_supervisor):
        # YOUR CODE STARTS HERE
        if isinstance(new_supervisor, Staff):
            self._supervisor = new_supervisor
            return 'Completed!'
        


    def applyHold(self, student):
        # YOUR CODE STARTS HERE
        if isinstance(student, Student):
            student.hold = True
            return 'Completed!'


    def removeHold(self, student):
        # YOUR CODE STARTS HERE
        if isinstance(student, Student):
            student.hold = False
            return 'Completed!'

    def unenrollStudent(self, student):
        # YOUR CODE STARTS HERE
        if isinstance(student, Student):
            student.active = False
            return 'Completed!'

    def createStudent(self, person):
        # YOUR CODE STARTS HERE
        return Student(person.name, person.get_ssn(), 'Freshman')




class Student(Person):
    '''
        >>> C = Catalog()
        >>> C._loadCatalog("cmpsc_catalog_small.csv")
        >>> s1 = Student('Jason Lee', '204-99-2890', 'Freshman')
        >>> s1
        Student(Jason Lee, jl2890, Freshman)
        >>> s2 = Student('Karen Lee', '247-01-2670', 'Freshman')
        >>> s2
        Student(Karen Lee, kl2670, Freshman)
        >>> s1 == s2
        False
        >>> s1.id
        'jl2890'
        >>> s2.id
        'kl2670'
        >>> s1.registerSemester()
        >>> s1.enrollCourse('CMPSC 132', C)
        'Course added successfully'
        >>> s1.semesters
        {1: CMPSC 132}
        >>> s1.enrollCourse('CMPSC 360', C)
        'Course added successfully'
        >>> s1.enrollCourse('CMPSC 465', C)
        'Course not found'
        >>> s1.semesters
        {1: CMPSC 132; CMPSC 360}
        >>> s2.semesters
        {}
        >>> s1.enrollCourse('CMPSC 132', C)
        'Course already enrolled'
        >>> s1.dropCourse('CMPSC 360')
        'Course dropped successfully'
        >>> s1.dropCourse('CMPSC 360')
        'Course not found'
        >>> s1.semesters
        {1: CMPSC 132}
        >>> s1.registerSemester()
        >>> s1.semesters
        {1: CMPSC 132, 2: No courses}
        >>> s1.enrollCourse('CMPSC 360', C)
        'Course added successfully'
        >>> s1.semesters
        {1: CMPSC 132, 2: CMPSC 360}
        >>> s1.registerSemester()
        >>> s1.semesters
        {1: CMPSC 132, 2: CMPSC 360, 3: No courses}
        >>> s1
        Student(Jason Lee, jl2890, Sophomore)
        >>> s1.classCode
        'Sophomore'
    '''
    def __init__(self, name, ssn, year):
        random.seed(1)
        # YOUR CODE STARTS HERE
        super().__init__(name, ssn)
        self.classCode = year
        self.semesters = {}
        self.hold, self.active = False, True
        self.account = self.__createStudentAccount()
        


    def __str__(self):
        # YOUR CODE STARTS HERE
        return f'Student({self.name}, {self.id}, {self.classCode})'

    __repr__ = __str__

    def __createStudentAccount(self):
        # YOUR CODE STARTS HERE
        if self.active:
            return StudentAccount(self)


    @property
    def id(self):
        # YOUR CODE STARTS HERE
        #returns the id using the getInitials method that was inheirited and the lastFour in the Person superclass
        return f'{self.getInitials}{super().lastFour}'

    def registerSemester(self):
        # YOUR CODE STARTS HERE
        #finds index and determines what year the student is, then makes a new key-value pair with the new data
        if self.active and self.hold == False:
            index = len(self.semesters) + 1
            if 3<= index <= 4:
                self.classCode = 'Sophomore'
            elif 5<= index <=6:
                self.classCode = 'Junior'
            elif index > 6:
                self.classCode = 'Senior'

            self.semesters[index] = Semester()
        else:
            return 'Unsuccessful operation'


    def enrollCourse(self, cid, catalog):
        # YOUR CODE STARTS HERE
        #uses the Semester class's addCourse to enroll in a new course
        if cid not in catalog.courseOfferings:
            return "Course not found"
        elif self.active == False or self.hold:
            return 'Unsuccessful operation'
        elif cid in self.semesters[len(self.semesters)].courses: 
            return 'Course already enrolled'
        else:
            #adds the cid to the end of the courses dictionary. Uses the length of semesters to find last value
            self.semesters[len(self.semesters)].addCourse(catalog.courseOfferings[cid])
            self.account.chargeAccount(self.account.CREDIT_PRICE * int(catalog.courseOfferings[cid].credits))
            return 'Course added successfully'

    def dropCourse(self, cid):
        # YOUR CODE STARTS HERE
        #Drops the course using .pop()
        if self.active == False or self.hold:
            return "Unnsuccessful operation"
        elif cid not in self.semesters[len(self.semesters)].courses:
            return 'Course not found'
        else:
            #removes the last course, saves the course to temp and temp is used to access the number of credits
            temp = self.semesters[len(self.semesters)].courses.pop(cid)
            self.account.makePayment(self.account.CREDIT_PRICE /2 * int (temp.credits))
            return 'Course dropped successfully'
            

    def getLoan(self, amount):
        # YOUR CODE STARTS HERE
        #deteremines if the account is active and full time, they uses the loan object to make a payment
        if self.active:
            if self.semesters[len(self.semesters)].isFullTime:
                temp = Loan(amount)
                self.account.loans[temp.loan_id] = temp
                self.account.makePayment(amount)
            else:
                return 'Not full-time'
        else:
            return 'Unsuccessful operation'
        


class StudentAccount:
    '''
        >>> C = Catalog()
        >>> C._loadCatalog("cmpsc_catalog_small.csv")
        >>> s1 = Student('Jason Lee', '204-99-2890', 'Freshman')
        >>> s1.registerSemester()
        >>> s1.enrollCourse('CMPSC 132', C)
        'Course added successfully'
        >>> s1.account.balance
        3000
        >>> s1.enrollCourse('CMPSC 360', C)
        'Course added successfully'
        >>> s1.account.balance
        6000
        >>> s1.enrollCourse('MATH 230', C)
        'Course added successfully'
        >>> s1.enrollCourse('PHYS 213', C)
        'Course added successfully'
        >>> print(s1.account)
        Name: Jason Lee
        ID: jl2890
        Balance: $12000
        >>> s1.account.chargeAccount(100)
        12100
        >>> s1.account.balance
        12100
        >>> s1.account.makePayment(200)
        11900
        >>> s1.getLoan(4000)
        >>> s1.account.balance
        7900
        >>> s1.getLoan(8000)
        >>> s1.account.balance
        -100
        >>> s1.enrollCourse('CMPEN 270', C)
        'Course added successfully'
        >>> s1.account.balance
        3900
        >>> s1.dropCourse('CMPEN 270')
        'Course dropped successfully'
        >>> s1.account.balance
        1900.0
        >>> s1.account.loans
        {27611: Balance: $4000, 84606: Balance: $8000}
        >>> StudentAccount.CREDIT_PRICE = 1500
        >>> s2 = Student('Thomas Wang', '123-45-6789', 'Freshman')
        >>> s2.registerSemester()
        >>> s2.enrollCourse('CMPSC 132', C)
        'Course added successfully'
        >>> s2.account.balance
        4500
        >>> s1.enrollCourse('CMPEN 270', C)
        'Course added successfully'
        >>> s1.account.balance
        7900.0
    '''
    
    #Outside so it can mutateed by the user
    CREDIT_PRICE =1000

    def __init__(self, student):
        # YOUR CODE STARTS HERE
        #initates values, loans and credit_price used elsewhere
        self.student = student
        self.balance =0
        self.loans = {}
    
    



    def __str__(self):
        # YOUR CODE STARTS HERE
        #return statement for name, id, and balance
        return f'Name: {self.student.name}\nID: {self.student.id}\nBalance: ${self.balance}'

    __repr__ = __str__


    def makePayment(self, amount):
        # YOUR CODE STARTS HERE
        self.balance -= amount
        return self.balance


    def chargeAccount(self, amount):
        # YOUR CODE STARTS HERE
        self.balance += amount
        return self.balance




if __name__=='__main__':
    import doctest
    #doctest.testmod()  # OR
    doctest.run_docstring_examples(Student, globals(), name='HW2',verbose=True) # replace Course for the class name you want to test