class Student:
    __name = ""
    __group = ""
        
    def set_name(self, name):
        self.__name = name
        
    def get_name(self):
        return self.__name

    def set_group(self, group):
        self.__group = group
        
    def get_group(self):
        return self.__group

    def get_info(self):
        info = []
        info.append([self.__name,self.__group])
        return info


