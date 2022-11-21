def recursive_fibonacci(n):  
   if n <= 1:  
       return n  
   else:  
       return(recursive_fibonacci(n-1) + recursive_fibonacci(n-2))
       
 
def non_recursive_fibonacci(n):
    first_num = 0
    second_num = 1
    print("The numbers in fibonacci series are [Non-Recursive] : ")
    print(f"{first_num}\n{second_num}")
    while(n-2):
        
        third_num = first_num + second_num
        first_num=second_num
        second_num=third_num
        
        print(third_num)
        n=n-1

numberOfTerms = int(input("How many terms do you want to print? "))  
 
if numberOfTerms <= 0:  
   print("Plese enter a positive integer")  
   
else:  
   print("Fibonacci sequence [Recursive]:")  
   for i in range(numberOfTerms):  
       print(recursive_fibonacci(i))  
       
non_recursive_fibonacci(numberOfTerms)  