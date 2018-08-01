import csv
from tkinter import*
class manage_students():
    
    def __init__(self):
        #initialize
        self.root = Tk()
        self.root.title('Sudent Roster Management')

        #frames
        self.left_frame = Frame(self.root)
        self.right_frame = Frame(self.root)
        self.bottom_frame = Frame(self.root)

        #entry for Student Name
        self.name_entry = Entry(self.left_frame)

        #label for entry and label for space
        self.entry_label = Label(self.left_frame, text = 'Student Name')
        self.space_label = Label(self.left_frame, text = '\n\n')
        #buttons
        self.add_button = Button(self.bottom_frame , text = 'Add' ,
                                 command = self.add_student)
        self.remove_button = Button(self.bottom_frame , text = 'remove' ,
                                    command = self.remove_student)

        #pack left
        self.entry_label.pack()
        self.name_entry.pack()
        self.space_label.pack()
        self.left_frame.pack(side = LEFT)

        #pack right
        self.right_frame.pack(side = RIGHT)

        #pack bottom
        self.add_button.pack(side = LEFT)
        self.remove_button.pack(side = LEFT)
        self.bottom_frame.pack(side =BOTTOM)
        
        #initialize lists for sudents / checks and check variables
        self.students = []
        self.checkvars = []
        self.check_buttons = []
        

        #load file to fill student list
        filename = 'student_list.txt'
        try:
            f = open(filename)
            for line in f:
                self.students.append(line.rstrip())
        except:
            pass

        #use the pulled info to create the checkboxes   
        self.create_checks()

        #mainloop
        self.root.mainloop()


    def add_student(self):
        student = self.name_entry.get()          #get the info from entry box      
        self.students.append(student.title())    #add to the list of students
        self.name_entry.delete(0, 'end')         #remove text from box
        self.write_to_file()                     #write new list to file
        self.add_check()                         #add a checkbox for new student

    def create_checks(self):
         #create int variable and checkbutton for each student 
        for student in self.students:
          self.var = IntVar()
          self.var.set(0)
          self.checkvars.append(self.var)
          self.check_button = Checkbutton(self.right_frame , text = student ,
                                          variable = self.var)
          self.check_button.pack()
          self.check_buttons.append(self.check_button)

    def add_check(self):
        for student in self.students:
            if student == self.students[-1]: #if student is the last one added               
                self.var = IntVar()          #create IntVar/checkbutton
                self.var.set(0)          
                self.checkvars.append(self.var) #add var to list
                button_name = Checkbutton(self.right_frame, text = student,
                                          variable = self.var)
                self.check_buttons.append(button_name) #add button to list
                
                button_name.pack()
            #this stops from creating extra checks if another student has
                #same name as the last in the index
                break
    def write_to_file(self):
        #save current student list to file
        file = open('student_list.txt' , 'w')
        for student in self.students:
            file.write(student + '\n')
        file.close()
            
            
    def remove_student(self):
        for var in self.checkvars:
            if var.get() == 1:  #check if check is on
                index = self.checkvars.index(var)
                #student and check will have same index in respective lists
                self.check_buttons[index].destroy() #remove the checkbox
                #remove student and the IntVar from their lists
                del self.check_buttons[index]
                del self.students[index]                 
                del self.checkvars[index]        
        #write new student list to the file                     
        self.write_to_file()      
        

app = manage_students()
