class Individual(): # Made a class with a Individual constractor with two variables


    def add_name(self): 
        invalid_characters_name  = ["!",  '"', "@", "#",'$','%','^', '&', '*',"(", ")","_",'+','=',',', '<', '>', '/', '?', ';', ':', '[', ']', '{', '}', '\\']
        while(True): # continuous loop until a valid name is entered 
            name = input("Enter a name: ")
            for letter in name: 
                for invalid_char in invalid_characters_name:
                    if letter == invalid_char: # if invalid character found continue the loop and get a new input
                        continue
            self.name = name # name was valid save it
            break # exit the loop cause the valid name was found


    def add_email(self):
        invalid_characters_email = ["!", '"', "'", "#",'$','%','^', '&',  '*',"(", ")",'+','=',',', '<', '>', '/', '?', ';', ':', '[', ']', '{', '}', '\\']
        while(True): # continuous loop to until valid email  is entered
            email = input("Enter a email: ")
            for letter in  email: 
                for invalid_char in invalid_characters_email:
                    if letter == invalid_char: ## if invalid character found continue the loop and get a new input
                        continue

            self.email = email
            break # exit the loop cause the valid name was found

class Student(Individual): # sub class, and  is accessing super class
    def add_studentID(self):
        while(True): # check until you have valid student ID
            try:
                student_ID = input("Enter a student ID: ")
                int(student_ID) # check if the input can be converted to the number if not go to except and continue the loop
                if len(student_ID) <= 7: # if the student lenght less or = 7 exit the loop
                    self.student_ID = student_ID 
                    break
                else:
                    print("Too long!")
            except:
                print("Not a number!") 

    def add_program_of_study(self):
        program_of_study = input("Enter a program of study: ")
        self.program_of_study = program_of_study

class Instructor(Individual): # sub class, and accessing super class


    def add_instructorID(self):
        while(True): #  check until you have valid instructor ID 
            try:
                instructor_ID = input("Enter an instructor ID: ")
                int(instructor_ID) # check if the input can be converted to the number if not go to except and continue the loop
                if len(instructor_ID) <= 5: # # if the insrtuctor lenght less or = 5 exit the loop
                    self.instructor_ID = instructor_ID
                    break

                else:
                    print("Too long!")
            except:
                print("Not a number!")

    def add_last_institution_graduated_from(self):
        last_institution_graduated_from = input("Enter the last institution you graduated from: ") 
        self.last_institution_graduated_from = last_institution_graduated_from

    def add_highest_degree_earned(self):
        highest_degree_earned = input("Enter the highest degree you've earned: ")
        self.highest_degree_earned = highest_degree_earned

def display_information(individual):
    print(individual.name)
    print(individual.email)
    if type(individual) == Student: # if the instance is a student print attrubutes specific to students
        print(individual.program_of_study)

    elif type(individual) == Instructor: # if the instance is a instructor print attrubutes specific to instructor
        print(individual.last_institution_graduated_from)
        print(individual.highest_degree_earned)

college_records  = [] # make a list to store indivudals instances
another = input("Press y to enter another individual: ")
if another == "y": # if the user enters y allow them to enter another individual 
    type_individual =  input("Press s to enter a student, press i to enter an instructor: ")
    if type_individual == 's': # click s for student
        student = Student() # create an object of type student
        student.add_name()
        student.add_email()
        student.add_studentID()
        student.add_program_of_study()
        college_records.append(student)
        display_information(student)

    elif type_individual  == 'i': # # click i for instructor
        instructor = Instructor() # create an object of type instructor
        instructor.add_name()
        instructor.add_email()
        instructor.add_instructorID()
        instructor.add_last_institution_graduated_from()
        instructor.add_highest_degree_earned()
        college_records.append(instructor)
        display_information(instructor)