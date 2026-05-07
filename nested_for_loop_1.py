# NESTED FOR LOOP
# 115
L =[100,200,35,40,60]
out=[]
for i in range(len(L)):
    temp_sum=0
    for j in range(len(L)):
        if i!=j:
            temp_sum+=L[j]
    out.append(temp_sum)
print(out)
