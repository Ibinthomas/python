import numbers
from add import add 
from sub import sub
from div import div
from mult import mult
from mode import mode
while True:
    print("""
            1.ADD
            2.SUB
            3.DIV
            4.MODE
            5.MULT
""")
    choice=int(input("enter the choice :"))

    if choice==1:
        a,b=numbers.num()
        add(a,b)
    elif choice==2:
        a,b=numbers.num()
        sub(a,b)
    elif choice==3:
        a,b=numbers.num()
        div(a,b)
    elif choice==4:
        a,b=numbers.num()
        mode(a,b)
    elif choice==5:
        a,b=numbers.num()
        mult(a,b)
    elif choice==6:
        break
    else:
        print("invalid choice")

    


