S=int(input())
y=int(input())
x=int(input())/100
z = ((S*(1+x)**y)*((1+x)**(1/12) -1))/((1+x)**y -1)
print(z)
print((z*y*12)-S)

