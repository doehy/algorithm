import sys
input =sys.stdin.readline

s1 = input().strip()
s2 = input().strip()

sign = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
sign2 = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}

#문자->숫자 
def to_num(s):
    l=len(s) #문자열 길이
    num =0 #결과값 저장 
    visited = [0]*l
    for i in range(l):
        if visited[i]==0: #아직 방문 x
            if i+1<len(s) and s[i:i+2] in sign2.keys(): #작은 숫자가 큰 숫자의 왼쪽에 오는 경우
                visited[i], visited[i+1] =1,1
                num += int(sign2[s[i:i+2]])
            else:
                visited[i]=1
                num+=int(sign[s[i]])
    return num

#숫자->문자            
def to_str(n):
    s=""
    while n>0:
        if n>=1000:
            s+="M"
            n-=1000
        elif n>=900:
            s+="CM"
            n-=900
        elif n>=500:
            s+="D"
            n-=500
        elif n>=400:
            s+="CD"
            n-=400
        elif n>=100:
            s+="C"
            n-=100
        elif n>=90:
            s+="XC"
            n-=90
        elif n>=50:
            s+="L"
            n-=50
        elif n>=40:
            s+="XL"
            n-=40
        elif n>=10:
            s+="X"
            n-=10
        elif n>=9:
            s+="IX"
            n-=9
        elif n>=5:
            s+="V"
            n-=5
        elif n>=4:
            s+="IV"
            n-=4
        elif n>=1:
            s+="I"
            n-=1
    return s

nresult = to_num(s1)+to_num(s2)
print(nresult)
print(to_str(nresult))