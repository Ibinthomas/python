class sobisco:
    def biscut(self):
        print("cream biscuts")
    def delivory(self):
        print("delivory")
    def time(self):
        print("9 am to 6:30 pm")

class eats_bites(sobisco):
    def supplay(self):
        print("supplay")
    def salary(self):
        print("salary")
    def stafs(self):
        print("staf details")

# class mk_markting(sobisco):
#     def stafs(self):
#         print("staf time")
#     def supplay(self):
#         print("every day")
#     def salary(self):
#         print("emp salary")

class wholeseler(eats_bites,sobisco):
    def credit(self):
        print("15 day credit")
    def prodects(self):
        print("prodect items")
    def stafs_who(self):
        print("stafs details")
    
class retales(eats_bites,wholeseler):
    def credit_pro(self):
        print("15 day credit")
    def prodect_iteams(self):
        print("prodect iteams")

a=sobisco()
a.biscut()

b=eats_bites()
b.supplay()

c=wholeseler()
c.credit()

d=retales()
d.biscut()

