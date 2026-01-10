sum_e = 0
sum_o = 0
for i in range(2, 11, 2):
    print(i)
    sum_e = sum_e +i
print(sum_e)
for i in range(1, 11, 2):
    print(i)
    sum_o = sum_o +i
print(sum_o)

sum_ee = 0
sum_oo = 0
for i in range(1,11):
    if i%2 == 0:
        sum_ee += i
        
    else:
        sum_oo += i
        

print(f"Sum of even numbers are {sum_ee}")
print(f"Sum of odd numbers are {sum_oo}")