import sqlite3


class DB_Controller:
    __db = sqlite3.connect('university.db')
    __sql = __db.cursor()


    def create_tables(self):
        self.__sql.execute("""CREATE TABLE IF NOT EXISTS Teachers(
                            name TEXT UNIQUE ,
                            qualification TEXT
                            );""")
        self.__db.commit()


        self.__sql.execute("""CREATE TABLE IF NOT EXISTS Subjects(
                            name TEXT UNIQUE ,
                            teacher TEXT,
                            hours INT,
                            FOREIGN KEY (teacher) REFERENCES Teachers(name)
                            );""")
        self.__db.commit()

        self.__sql.execute("""CREATE TABLE IF NOT EXISTS Groups(
                            group_number TEXT UNIQUE, 
                            subject TEXT,
                            FOREIGN KEY (subject) REFERENCES Subjects(name)
                            );""")
        self.__db.commit()


        self.__sql.execute("""CREATE TABLE IF NOT EXISTS Students(
                    name TEXT UNIQUE ,
                    group_number TEXT,
                    FOREIGN KEY (group_number) REFERENCES Groups(group_number)
                    );""")
        self.__db.commit()
        print("Kaif")


    def add_student(self, name, group):
        k = -1
        for value in self.__sql.execute("SELECT name FROM Students"):
            if name == value[0]:
                return -1
        for value in self.__sql.execute("SELECT group_number FROM Groups"):
            if group == value[0]:
                k = 0
        if k == 0:
            if self.__sql.fetchone() is None:
                self.__sql.execute(f"INSERT INTO Students VALUES (?, ? )", (name, group))
                self.__db.commit()
            return 0
        return -1


    def del_student(self, name):
        self.__sql.execute(f"DELETE FROM Students WHERE name = ?",(name,))
        self.__db.commit()
        print("Deletion was successful\n")


    def print_students(self):
        for value in self.__sql.execute("SELECT * FROM Students"):
            print("Full name: " + value[0] + ";\t Group: "+ value[1])


    def add_teacher(self, name, qualification):
        for value in self.__sql.execute("SELECT name FROM Teachers"):
            if name == value[0]:
                return -1
        if self.__sql.fetchone() is None:
            self.__sql.execute(f"INSERT INTO Teachers VALUES (?, ?)", (name, qualification))
            self.__db.commit()
            return 0
        return -1


    def del_teacher(self, name):
        self.__sql.execute(f"DELETE FROM Teachers WHERE name = ?", (name,))
        self.__db.commit()
        print("Deletion was successful\n")


    def print_teachers(self):
        for value in self.__sql.execute("SELECT * FROM Teachers"):
            print("Full name: " + value[0] + ";\tQualification: " + value[1])


    def add_group(self, number, subjects):
        k = 0
        for value in self.__sql.execute("SELECT group_number FROM Groups"):
            if number == value[0]:
                return -1
        for value in self.__sql.execute("SELECT name FROM Subjects"):
            if subjects == value[0]:
                k = 0
        if k == 0:
            if self.__sql.fetchone() is None:
                self.__sql.execute(f"INSERT INTO Groups VALUES(?, ? )", (number, subjects))
                self.__db.commit()
                return 0
        return -1


    def del_group(self, number):
        self.__sql.execute(f"DELETE FROM Groups WHERE group_number = ?", (number,))
        self.__db.commit()
        print("Deletion was successful\n")


    def print_groups(self):
        for value in self.__sql.execute("SELECT * FROM Groups"):
            print("Group number: " + value[0] + "\tSubject:" + value[1])


    def add_subject(self, name, teacher, hours):
        k = -1
        for value in self.__sql.execute("SELECT name FROM Subjects"):
            if name == value[0]:
                return -1
        for value in self.__sql.execute("SELECT name FROM Teachers"):
            if teacher == value[0]:
                k = 0
        try :
            hours  = int(hours)
        except ValueError:
            return -1
        if k == 0:
            if self.__sql.fetchone() is None:
                self.__sql.execute(f"INSERT INTO Subjects VALUES (?, ?, ?)", (name, teacher, hours))
                self.__db.commit()
                return 0
        return -1


    def del_subject(self, name):
        self.__sql.execute(f"DELETE FROM Subjects WHERE name = ?", (name,))
        self.__db.commit()
        print("Deletion was successful\n")


    def print_subjects(self):
        for value in self.__sql.execute("SELECT * FROM Subjects"):
            print("Subject name: " + value[0] + "\tTeacher: " + value[1] + "\tHours :" + str(value[2]))


    def close_db(self):
        self.__db.close()




