n=int(raw_input())
fact=1
for i in range(1,n+1):
	if i==0:
		fact=1
	fact=fact*i
print fact
