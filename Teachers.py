class Teacher:
    __name = ""
    __qualification = ""
        
        
    def set_name(self, name):
        self.__name = name
        
    def get_name(self):
        return self.__name

    def set_qualification(self, qualification):
        self.__qualification = qualification
        
    def get_qualification(self):
        return self.__qualification

    def get_info(self):
        info = []
        info.append([self.__name,self.__qualification])
        return info


    
