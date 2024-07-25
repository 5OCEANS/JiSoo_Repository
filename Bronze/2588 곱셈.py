num1 = int(input()) 
num2 = int(input()) 


t = num1 * (num2 % 10) 
fo = num1 * ((num2 // 10) % 10)  
fi = num1 * (num2 // 100) 
s = num1 * num2  

print(t)
print(fo)
print(fi)
print(s)