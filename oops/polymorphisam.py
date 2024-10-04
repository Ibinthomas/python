# class bank:
#     def __init__(self):
#         print("add bank ")
# class user(bank):
#     def __init__(self):
#         print("add user details")

# sbi=bank()
# ibi=user()

class school:
    def notes(self,*sub):
        print("notes",sub)

class student(school):
    def notes(self,sub):
        print("note in student")
        super().notes('python','web',sub)

ibin=student()
ibin.notes('hello')