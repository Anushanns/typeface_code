a=input()
b=input()
s=len(b)
s1=len(a)
lastIndex = b[s-1];
count = 0;
for i in range(s1):
    if lastIndex in a[i]:
        count =count +1


print(count)