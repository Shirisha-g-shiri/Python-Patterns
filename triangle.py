rows = 5


# for i  in range(rows+1):
#     for j in range(i,rows):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     print()   
# for i  in range(rows):
#     for j in range(i+1):    
#         print(" ",end=" ")
#     for j in range(rows,i,-1):
#         print("*",end=" ")
#     print() 
           

# for i in range(rows+1):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()
# for i in range(rows):    
#     for j in range(rows,i,-1):
#         print("*",end=" ")
#     print()        


# for i in range(rows):
#     print("* "*rows,end=" ")
#     print()    


for i in range(rows):
    for j in range(i+1):
        print("",end=" ")    
    for j in range(i,rows):
        print("*",end=" ")    
    print()    
for i in range(rows):
    for j in range(rows,i,-1):
        print("",end=" ")  
    for j in range(i+1):
        print("*",end=" ")      
    print()    