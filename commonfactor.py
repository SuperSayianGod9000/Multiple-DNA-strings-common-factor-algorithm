from itertools import product
patterns=["ATTTGGC","TGCCTTA","CGGTATC","GAAAATT"]
nucleotides=['A','T','G','C']

check=[]
newcheck=[]
answer=[]
answer2=[]
keyword=[]
def commonfactor(patterns,k,d):
    refstring=patterns.pop(0)
    for i in range(len(refstring)-k+1):
        
        count=0
        comparestring=refstring[i:i+k]
        for string in patterns:
            for j in range(len(string)-k+1):
                string1=string[j:j+k]
                for a in range(k):
                    check.append(ord(comparestring[a])-ord(string1[a]))

                if(check.count(0)>=k-d):
                    count=count+1
                    check.clear()
                    break

                else:
                    check.clear()


        if(count==len(patterns)):
            answer.append(comparestring)

    

    keyword=[''.join(i) for i in product(nucleotides,repeat=k)]
    for test in answer:
        for extrapattern in keyword:
    
            for y in range(k):
                newcheck.append(ord(test[y])-ord(extrapattern[y]))
        
         

            if(newcheck.count(0)>=k-d and extrapattern not in answer and extrapattern not in answer2):
                answer2.append(extrapattern)

            newcheck.clear()

   
    

    for word in answer2:
        count=0
        for string in patterns:
            for j in range(len(string)-k+1):
                string1=string[j:j+k]
                for a in range(k):
                    check.append(ord(word[a])-ord(string1[a]))

                if(check.count(0)>=k-d):
                    count=count+1
                    check.clear()
                    break

                else:
                    check.clear()

        
        if(count==len(patterns)):
            
            answer.append(word)

    print(answer)

commonfactor(patterns,3,1)



            



            

        
                
                
