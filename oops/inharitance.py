# class parent:
#     def land(swlf):
#         print("land")
#     def balance(self):
#         print("1crose")

# class son(parent):
#     def bike(self):
#         print("bike")

# ibee=son()
# ibee.bike()
# ibee.balance()
# ibee.land()

# print('*'*40)

# class syneffo:
#     def web(self):
#         print(('pyrhon'))
#     def php(self):
#         print('"php')

# class novani(syneffo):
#     def web(self):
#         print("web dev")
#         print("degital markating")

# anu=novani()
# anu.web()
# anu.php()
# anu.web()



#MULTIPLE INHARITANCE

# class dad:
#     def shop(self):
#         print("shop")
#     def car(self):
#         print("car")
    
# class mom:
#     def dress(self):
#         print('dress')
#     def kitchen(self):
#         print("grosery")

# class son(mom,dad):
#     def bike(self):
#         print("bike")

# a=son()
# a.bike()
# a.car()
# a.kitchen()
# a.dress()
# a.shop()

# multilevel inheritance

# class cu:
#     def exam(self):
#         print("exam notification")
#     def result(self):
#         print("exam result")
# class college(cu):
#     def nots(self):
#         print("notes")
#     def rooms(self):
#         print("class rooms")

# class student(college):
#     def uniform(self):
#         print("uniforms")

# std=student()
# std.exam()
# std.result()
# std.nots()
# std.uniform()
# std.rooms()

#HIRARCICAL INHARITANCE

# class college:
#     def exam(self):
#         print("exam")
#     def result(self):
#         print("result")
# class chm(college):
#     def notes(self):
#         print("notes")
#     def assignement():
#         print("assignment")
# class bio(college):
#     def notes(self):
#         print("notes")
#     def assignement():
#         print("assignment")

# s=chm()
# s.assignement()

# HYBRID INHERITANCE

class synnefo:
    def python(self):
        print("python")
    def network(self):
        print("network")
    def cyber(self):
        print("cyber")

class teacher(synnefo):
    def labs(self):
        print("labs")
    def exams(self):
        print("exam")
    def topics(self):
        print("topics")

class nonteach(synnefo):
    def office(self):
        print("office")
    def technical(self):
        print("technical")
    def placement(self):
        print("placement")

class student(synnefo,teacher):
    def result(self):
        print("result")
    def attendence(self):
        print("attendence")
    def exams(self):
        print("exams")

a=synnefo()
a.python()

b=teacher()
b.topics()

c=nonteach()
c.office()

d=student()
d.python()