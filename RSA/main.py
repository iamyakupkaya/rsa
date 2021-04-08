
import ast
prime_series=list()
without_prime_series=list()
enc_list=list()
decrp_list=list()
decrp_text_list=list()
p=0
q=0

#for 2 numbers find GCD... and append list!
def GCD(num1,num2):
    without_prime_series.clear()
    if(num1<num2):
        for i in range(2,num1+1):
            if(num1%i==0 and num2%i==0):
                without_prime_series.append(i)
        return without_prime_series
    elif(num2<num1):
        for i in range(2,num2+1):
            if(num1%i==0 and num2%i==0):
                without_prime_series.append(i)
        return without_prime_series

    else:
        without_prime_series.append(num1)
        return without_prime_series


def takeNumber():
    changing = True
    global a
    global b
    while (changing):
        print("PLEASE ENTER THE 'p' AND 'q' VALUES BELOW:")
        a1 = input("Enter a prime number for p: ")
        b1 = input("Enter a prime number for q: ")
        print("************************************************************************************")


        if (a1.isnumeric() and b1.isnumeric()):
            a = int(a1)
            b = int(b1)
            changing = False
        else:
            changing = True
    prime=GCD(a,b)
    if (len(prime) > 0):
        if (prime[0] == a and prime[0] == b):
            print("Please write different two number...!")
            takeNumber()

        else:
            print("Please choose q and q again. Because GCD (p,q) is not 1 ")
            takeNumber()

    return a,b

# prime two numbers between them
def GCDPrime(new_fi_n):
    prime_series.clear()
    for i in range(2,new_fi_n):
        if new_fi_n % i == 0: #Here not GCD
            continue
        else: # Here GCD Numbers
           # print("{} sayısı {} sayısı ile asaldır.".format(new_fi_n,i))
            prime_series.append(i)
    return prime_series
def select_e(new_fi_n):
    global newe
    # 1<e<new_fi_n_ and  GCD(e,new_fi_n-1)=1
    ourlistprime=GCDPrime(new_fi_n) # this is prime list between Fhi
    newe =ourlistprime[0]
    return int(newe)


def find_d(public_key,fhi):
    count=1
    while(True):
        if ((count*public_key)%fhi==1):
            return count
        else:
            count=count+1

def Encryption(public_key,n):
    ascii_list=list()
    enc_list.clear()
    global real_text
    real_text = input("Please write text for Encryption:")
    text=real_text
    list_text = list(text)
    for i in range(0, len(list_text)):
        ascii_list.append(ord(list_text[i]))
    for k in ascii_list:
        c=(k**public_key)%n
        enc_list.append(c)

    return enc_list

def Decryption(d,n):
    decrp_list.clear()
    decrp_text_list.clear()
    ourtext=input("please write encription List for decryption:")
    res = ast.literal_eval(ourtext)
    for k in res:
        m=(k**d)%n
        decrp_list.append(m)

    for i in decrp_list:
        decrp_text_list.append(chr(i))
    return "".join(decrp_text_list)





# Starting Program
p,q=takeNumber()
result=GCD(p,q)
if (len(result)==0): #Sayılar kendi arlarında Asal.
    n=p*q
    fi_n=(p-1)*(q-1)
    public_key=select_e(fi_n) # e
    d=find_d(public_key,fi_n)



    enc=Encryption(public_key,n)
    print("Encryption Text:")
    print(enc)
    text=Decryption(d,n)
    print("After Decryption:"+text)
    print("p={0}".format(p))
    print("q={0}".format(q))
    print("n={0}".format(n))
    print("Fi(n)={0}".format(fi_n))
    print("e={0}".format(public_key))
    print("d={0}".format(d))
    print("Public Key={0}".format((n,public_key)))
    print("Private Key={0}".format((n,d)))
    print("Your Plain Text={0}".format(real_text))
    print("Encryption List:{0}".format(enc))
    print("Decryption List:{0}".format(decrp_list))


# =====================================================================
    f = open('encryption.txt', 'w')

    f.write("public key:{0}\n".format((n,public_key)))
    f.write("Decryption List:{0}\n".format(decrp_list))



    f.close()






else:
    print("Error!")



