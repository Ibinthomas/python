from abc import ABC,abstractmethod
class syn(ABC):
    @abstractmethod
    def reg(self):
        pass 
    def python(self):
        print('python topics')
    def php(self):
        print("php topics")
    
class staff(syn):
    def reg(self):
        print("staff details")
    def notes(self):
        print("notes")
    
class std(syn):
    def reg(self):
        print("std date")
    def exam(self):
        print("exams")

staff1=staff()

manu=std()