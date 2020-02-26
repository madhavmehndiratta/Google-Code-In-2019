def multiply(res, res_size): 
    car = 0
    for i in range(res_size): 
        product = res[i] * 2 + car 
  
        res[i] = product % 10
  
        car = product // 10

    while (car): 
        res[res_size] = car % 10
        car = car // 10
        res_size+=1
  
    return res_size 
  
def compute(num): 
    if (num == 0) :  
        print("1") 
        return
      
    res=[0 for i in range(1024)] 
    res_size = 0
    temp = 2 
  
    while (temp != 0): 
        res[res_size] = temp % 10 
        res_size+=1
        temp = temp // 10
  
    for i in range(2, num + 1): 
        res_size = multiply(res, res_size) 
    
    print()
    print(f"The Value for {2}^{exponent} is ",end="") 
    for i in range(res_size - 1, -1, -1): 
        print(res[i], end="")
    print()
    print() 
  
exponent = int(input("[?] Enter any number between 1 and 1024: "))
compute(exponent) 