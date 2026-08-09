#Program to accept lisy employee +ve salary, obtaining salary range from 0 to 500 and hike 10%,
#  hike guve 20% whose salary is 501-1000 and print salary of 10%hike emp and 20% hike
# emp(maxSal-1000, minSal-0)

#filtermapreduce
import functools
print("Enter list of salaries separated by space:")

sals=[float(sal) for sal in input().split() if 0<=float(sal)<=1000]

#obtain salaries ranges from 0 to 501
sal0_500=list(filter(lambda sal: 0<=sal<=500, sals))

#obtain salaries ranges from 501 to 1000
sal501_1000=list(filter(lambda sal: 501<=sal<=1000, sals))

#hike 10% for salary range 0 to 500
hksal0_500=list(map(lambda sal: sal*10/100, sal0_500))

#hike 20% for salary range 501 to 1000
hksal501_1000=list(map(lambda sal: sal*20/100, sal501_1000))

#get the total of those employees whose sal ranges from 0 to 500 before and after hike
totalsal0_500=functools.reduce(lambda sal1, sal2: sal1+sal2, sal0_500)
hktotalsal0_500=functools.reduce(lambda sal1, sal2: sal1+sal2,hksal0_500)

#get the total of those employees whose sal ranges from 501 to 1000 before and after hike
totalsal501_1000=functools.reduce(lambda sal1,sal2: sal1+sal2, sal501_1000)
hksal501_1000=functools.reduce(lambda sal1, sal2: sal1+sal2,hksal501_1000)

print("="*50)
print("sal0_500\t\tHiked sal0_500")
print("-"*50)

for osl,nsl in zip(sal0_500, hksal0_500):
    print("\t{}\t\t{}".format(osl,nsl))
print("------------")
print("sal501_1000\thiked sal501_1000")
print("-"*50)

for osl, nsl in zip(sal501_1000, hksal501_1000):
    print("\t{}\t\t{}".format(osl,nsl))
    print("================")
    print("\t{}\t\t{}".format(totalsal501_1000, hksal501_1000))
    print("="*50)

gtotsal0_1000=totalsal0_500+totalsal501_1000
ghktotsal0_1000=hktotalsal0_500+hksal501_1000
print("Grand tota paid by company before hike:{}".format(gtotsal0_1000))
print("Grand total paid by company after hike:{}".format(ghktotsal0_1000))
print("="*50)






        


