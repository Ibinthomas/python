f=open('python/ibin2.txt','a')
a=int(input("Enter the first no"))
i=1
for i in range(i,11):
    f.write(str(i)+'*'+str(a)+'='+str(i*a)+'\n')