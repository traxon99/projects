'''
Author: Jackson Yanek
KUID: 3094054
Date: 09/30/2022
Lab: lab04
Last modified: 09/30/2022
Purpose: list comparisons
'''



file1_name = input('Enter name of first data file: ')
file2_name = input('Enter name of second data file: ')
file1 = open(file1_name,'r')
file2 = open(file2_name,'r')
nums1 = []
nums2 = []
count = 0

for line in file1:
    nums1.append(line.strip())
        
for i in range(len(nums1)):
    nums1[i] = int(nums1[i])
        
for line in file2:
    nums2.append(line.strip())

for i in range(len(nums2)):
    nums2[i] = int(nums2[i])    


sum1 = sum(nums1)
sum2 = sum(nums2)
avg1 = sum(nums1)/len(nums1)
avg2 = sum(nums2)/len(nums2)
for checknum1 in nums1:
    for checknum2 in nums2:
        if checknum1 == checknum2:
            count += 1
    
    
if sum1 > sum2:
    print('The first list has the larger sum of',sum1)
elif sum1 < sum2:
    print('The second list has the larger sum of',sum2)
elif sum1 == sum2:
    print('Both lists have the same sum of',sum1)
if avg1 > avg2:
    print(f'The first list has the larger average of {avg1:0.1f}')
elif avg1 < avg2:
    print('The second list has the larger average of',avg2)
elif avg1 == avg2:
    print(f'Both lists have the same average of {avg1:0.1f}')
print ('Count of values that appear in both lists: ',count)
if nums1 == nums2[::-1]:
    print('The lists are palindromes')
else:
    print('The lists are not palindromes')
