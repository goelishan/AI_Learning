# check pallindrome

# method 1
def is_pallindrome(word):
    return word==word[::-1]

print(is_pallindrome('madam'))

# method 2

def check_pallindrome(word):
    left,right=0,len(word)-1
    word=word.lower()
    while left<right:
        if word[left]!=word[right]:
           return False
        left+=1
        right-=1
    return True

print(check_pallindrome('Madam'))    


# ----------------------------------------------------------------------------------------------------

# find prime numbers in a list of numbers

def find_prime(num):
    prime=[]
    for n in range(2,num+1):
        is_prime=True

        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                is_prime=False
                break
        if is_prime:
            prime.append(n)
    return prime[::-1]


print(find_prime(40))

def generate_prime(num):

    for n in range(2,num+1):
        is_prime=True

        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                is_prime=False
                break
        if is_prime:
            yield n

for p in generate_prime(20):
    print(p)


def twin_primes(num):
    prime=[]

    for n in range(2,num+1):
        is_prime=True

        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                is_prime=False
                break
        
        if is_prime:
            prime.append(n)
    
    twin_prime=[]
    for i in range(len(prime) - 1):
        if prime[i + 1] - prime[i] == 2:
            twin_prime.append((prime[i], prime[i + 1]))
    
    return twin_prime

print(twin_primes(30))

# ------------------------------------------------------------------------------------------------------------------------

# generate fibonacci series using yield

def fibonacci(n):
    a,b=1,1
    count=0
    while count<n:
        yield a
        a,b=b,a+b
        count+=1

for num in fibonacci(10):
    print(num)

def fibonacci_1(max_value):
    a,b=0,1
    while a<=max_value:
        yield a
        a,b=b,a+b

for num in fibonacci_1(50):
    print(num)

