import Students
import Teachers
import Groups
import Subjects
import DB


class Action:
    __db = DB.DB_Controller()
    __st = Students.Student()
    __tc = Teachers.Teacher()
    __gr = Groups.Group()
    __sub = Subjects.Subject()


    def get_records(self,key):
        if key == 1:
            self.__db.print_students()
        elif key == 2:
            self.__db.print_teachers()
        elif key == 3:
            self.__db.print_groups()
        else:
            self.__db.print_subjects()

    def add_record(self, key):
        if key == 1:
            self.__st.set_name(input("Enter student full name: "))
            print("Make sure the group exists!")
            self.__st.set_group(input("Enter group number: "))
            key = self.__db.add_student(self.__st.get_name(), self.__st.get_group())
            if key == -1:
                print("\nA student has already been added or an attempt is made to add to a non-existent group!\n")
            else:
                print("\nAdded successfully!\n")

        elif key == 2:
            self.__tc.set_name(input("Enter teacher full name: "))
            self.__tc.set_qualification(input("Enter qualification: "))
            key = self.__db.add_teacher(self.__tc.get_name(), self.__tc.get_qualification())
            if key == -1:
                print("\nTrying to add a teacher again!\n")
            else:
                print("\nAdded successfully!\n")

        elif key == 3:
            self.__gr.set_number(input("Enter group number: "))
            self.__gr.set_subjects(input("Enter major set_subject in group:"))
            key = self.__db.add_group(self.__gr.get_number(),self.__gr.get_subjects())
            if key == -1:
                print("\nTrying to add a group again!\n")
            else:
                print("\nAdded successfully!\n")

        else:
            self.__sub.set_name(input("Enter sugject name: "))
            self.__sub.set_teacher(input("Enter teacher full name: "))
            self.__sub.set_hours(input("Enter number of hours: "))
            key = self.__db.add_subject(self.__sub.get_name(),self.__sub.get_teacher(),self.__sub.get_hours())
            if key == -1:
                print("\nError, incorrect data entry\n")
            else:
                print("\nAdded successfully!\n")

    def del_record(self, key):
        if key == 1:
            name = input("Enter student full name: ")
            self.__db.del_student(name)
        elif key == 2:
            name = (input("Enter teacher full name: "))
            self.__db.del_teacher(name)
        elif key == 3:
            name = (input("Enter group number: "))
            self.__db.del_group(name)
        else:
            name = (input("Enter sugject name: "))
            self.__db.del_subject(name)