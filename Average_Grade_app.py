from tkinter import*
import webbrowser
import os

class Grade():

    def __init__(self):
        #initialize 
        self.root = Tk()
        self.root.title( 'Average Grade')
        #Frames 
        self.left_frame = Frame(self.root)
        self.right_frame = Frame(self.root)
        self.bottom_frame = Frame(self.root)

        #student menu label
        self.option_label = Label(self.left_frame, text = 'Student Roster')

        #student menu
        self.students = {} #must pass dict
        self.read_students() #read students in from file
        self.option_var = StringVar()
        self.student_menu = OptionMenu(self.left_frame, self.option_var,
                         *self.students) #star here says keys from dict no values
        self.set_menu_default() #set the default option in menu
                                  
        #entry
        self.entry1 = Entry(self.left_frame)
        self.entry2 = Entry(self.left_frame)
        self.entry3 = Entry(self.left_frame)

        #label the entries for test input
        self.label_entry1 = Label(self.left_frame , text = 'Test 1')
        self.label_entry2 = Label(self.left_frame , text = 'Test 2')
        self.label_entry3 = Label(self.left_frame , text = 'Test 3')

        #empty label to create space above button
        self.space = Label(self.left_frame , text = '\n\n')

        #buttons
        self.button = Button(self.bottom_frame, text= 'Grade Tests' ,
                             command = self.calc)

        self.file_button = Button(self.bottom_frame, text= 'Grade Book' ,
                                  command = self.grade_book)

        #label
        self.grades = StringVar()
        self.grade_label = Label(self.right_frame ,
                                 textvariable = self.grades)

        self.grades.set('TEST 1:  \nTEST 2:  \nTEST 3:  \nAVERAGE:  ')
        #pack left side
        self.option_label.pack()
        self.student_menu.pack()
        self.label_entry1.pack()
        self.entry1.pack()
        self.label_entry2.pack()
        self.entry2.pack()
        self.label_entry3.pack()        
        self.entry3.pack()
        self.space.pack()
        self.left_frame.pack(side = LEFT)

        #pack right side
        self.grade_label.pack(side = LEFT)
        self.right_frame.pack(side = RIGHT)

        #pack bottom
        
        self.button.pack(side = LEFT)
        self.file_button.pack(side = RIGHT)
        self.bottom_frame.pack(side = BOTTOM)

        

        self.root.mainloop()

    #some attributes need initialized to use in functions
        self.letter1 = None
        self.letter2 = None
        self.letter3 = None
        self.average = None
    #functions for program   
    def calc(self):
        """When the 'Grade Tests' button is clicked."""
        try:
            test1 = int(self.entry1.get())
            test2 = int(self.entry2.get())
            test3 = int(self.entry3.get())
        #if nothing or alpha char entered program won't error
        except ValueError:  
            self.entry_error()
        else:
            self.letter1 = self.get_grade(test1)
            self.letter2 = self.get_grade(test2)
            self.letter3 = self.get_grade(test3)
            if self.letter1 and self.letter2 and self.letter3:
                self.average = format((test1 + test2 + test3) / 3 , '.2f')
                self.selected_student = self.option_var.get()
                self.set_label()
                self.write_to_file()
        
        

    def get_grade(self, num):
        if num >= 90 and num <= 100:
            grade = 'A'
            return grade
        elif num >= 80 and num <= 89:
            grade = 'B'
            return grade
        elif num >= 70 and num <= 79:
            grade = 'C'
            return grade
        elif num >= 60 and num <= 69:
            grade = 'D'
            return grade
        elif num >= 0 and num <= 59:
            grade = 'F'
            return grade
        else:
            self.range_error()
        

    def set_label(self):
        """Set the label with the grades."""
        self.grades.set(self.selected_student + '\n' +
                        'TEST 1: ' + self.letter1 +
                        '\nTEST 2: ' + self.letter2 +
                        '\nTEST 3: '  + self.letter3 +
                        '\nAVERAGE: ' + self.average +
                        ' ' + str(self.get_grade(float(self.average))))

    def range_error(self):
        """Set label for instance that grade is out of score range."""

        self.grades.set('One or more\n test score is\n out of range.')

    def entry_error(self):
        """set label for instance of empty or alpha entries."""
        self.grades.set('One or more\n test score is\n not valid entry.')

    def write_to_file(self):
        """Write the grades to the file."""
        filename = 'Average_Grade.txt'
        info = self.selected_student + '\n' + \
                        'TEST 1: ' + self.letter1 + \
                        '\nTEST 2: ' + self.letter2 + \
                        '\nTEST 3: '  + self.letter3 + \
                        '\nAVERAGE: ' + self.average + \
                        " " + str(self.get_grade(float(self.average))) + \
                        '\n\n\n'
       
        f = open(filename , 'a')
        f.write(info)                
        f.close()
               
              
        
    def grade_book(self):
        """open the grade book file."""
        if os.path.isfile('Average_Grade.txt'):
            webbrowser.open('Average_Grade.txt')
        else:
            self.grades.set('No Grades Imputed')

    def read_students(self):

        file = open('student_list.txt', 'r')
                
        for student in file:
            self.students[student.rstrip()] = None
        if len(self.students.keys()) == 0:
            self.students['no students found'] = None

        file.close()
                
                
            
            
            
               

    def set_menu_default(self):
        if self.students:
            self.option_var.set('Select Student')
        else:
            self.option_var.set('Roster Empty')


grade = Grade()
