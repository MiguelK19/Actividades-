Lista = [1,3,4,2,7,0]
for i in range(len(Lista)):
    for j in range(len(Lista)):
        if Lista[i] + Lista[j] == 10:
            print(Lista[i]," + ",Lista[j])
