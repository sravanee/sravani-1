n=int(raw_input())
temp=n
re=0
while(n!=0):
	r=n%10
	re=re*10+r
	n/=10
if(temp==re):
	print "yes"
else:
	print "no"
