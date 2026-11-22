import random
q = []
a = []
lenght=[]
n=0
number=0
print("after writing all questions and answer write end")
while n!="end":
    n=input("question: ")
    if n!="end":
        q.append(n)
        v=input("answer: ")
        a.append(v)
        lenght.append(number)
        number+=1
l="yes"
print("for revealing the answer press enter")
while l!="no":
    options=lenght.copy()
    for w in range(len(q)):
        b=random.choice(options)
        o=input(f"{q[b]}: ")
        if o=="correction":
            q[b]=input(f"original:({q[b]}) corrected: ")
            a[b]=input(f"original:({a[b]}) corrected: ")
        else:
            print(a[b])
        options.remove(b)
    print("end of set")
    l=input("again?")
    while l not in("yes","no"):
        l=input("answer must be yes/no: ")
    if l=="yes":
        h=input("add questions: ")
        while h not in("yes","no"):
            h=input("answer must be yes/no: ")
        n=0
        if h=="yes":
            while n!="end":
                n=input("question: ")
                if n!="end":
                    q.append(n)
                    v=input("answer: ")
                    a.append(v)
                    lenght.append(number)
                    number+=1

        
