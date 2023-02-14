data = [3, 30, 34, 5, 9]
max_num = str(max(data))
result = list(map(str,data))

for i in range(len(max_num)):
    print(i)
    try:
        result = sorted(result, key= lambda x : int(x[i]),reverse=True)
        print(result)
    except(IndexError): 
        pass

    
    


