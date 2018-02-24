password="KualaLumpur"
n=100
a=str(input("Enter the password:"))
for i in range(0,n):
    if(a==password):
        continue
    else:
        print("Wrong password....")
        break
    print("Password accepted")
    
