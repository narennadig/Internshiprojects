from math import sqrt
ecd=0
plot1=[1,4]
plot2=[3,3]
for i in range(0,len(plot1)):
 ecd=ecd+(plot1[i]-plot2[i])**2

print(sqrt(ecd))
