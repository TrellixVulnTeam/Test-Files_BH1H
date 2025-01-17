# Python3 program to generate n-bit Gray codes 
import math as mt 
def bi_to_num(k):
    no=int(k)
    
    sum=0
    k=0
    while no>0:
        
        sum=sum+(2**k)*(no%10)
        no=no//10
        k+=1
    return sum    
        
    
# This function generates all n bit Gray  
# codes and prints the generated codes 
def generateGrayarr(n): 
  
    # base case 
    if (n <= 0): 
        return
  
    # 'arr' will store all generated codes 
    arr = list() 
  
    # start with one-bit pattern 
    arr.append("0") 
    arr.append("1") 
  
    # Every iteration of this loop generates  
    # 2*i codes from previously generated i codes. 
    i = 2
    j = 0
    while(True): 
  
        if i >= 1 << n: 
            break
      
        # Enter the prviously generated codes  
        # again in arr[] in reverse order.  
        # Nor arr[] has double number of codes. 
        for j in range(i - 1, -1, -1): 
            arr.append(arr[j]) 
  
        # append 0 to the first half 
        for j in range(i): 
            arr[j] = "0" + arr[j] 
  
        # append 1 to the second half 
        for j in range(i, 2 * i): 
            arr[j] = "1" + arr[j] 
        i = i << 1
  
    # prcontents of arr[] 
    for i in range(len(arr)): 
        print(bi_to_num(arr[i]) ,end=' ')
  
# Driver Code 
T=int(input())
for i in range(T):
    n=int(input())
    generateGrayarr(n)
  
# This code is contributed  
# by Mohit kumar 29 
