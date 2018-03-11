#  factorial of a number given as input

print('ENTER THE NUMBER    ')
n=int(input())

fact=1

for i in range(1,n):
    fact=fact * i;

print(fact)

