n = int(input())
text = list(input())
answer = 0
textLeng = len(text)

def check(leng):
	temp = set()
	count = 0 # count를 0으로 초기화한 이유는 별 것 없다.
	left = 0
	ret = leng
	for i in range(len(text)):
		if text[i] not in temp:
			if count == leng:
				right = i # 반복문에서 다시 여기서부터 봐	
				break
			count += 1
			temp.add(text[i])
		right = i
	if right == textLeng - 1:
		return textLeng
	while left <= right and right < textLeng: # 길이를 제한을 둬야하는게 결국 리스트 범위를 벗어날 수 있기 때문이다.
		if count <= leng and text[right] not in temp:
			ret = max(ret, right + 1 - left)
		else:
			ret = max(ret, right - left)
		if text[right] not in temp: # 근데 현재 값이 temp에 들어있지 않은 경우
			if count < leng:
				count += 1 # 이건 종류를 세는거야 종류 업
				temp.add(text[right]) # 종류 추가	
			else: # 하지만 이젠 한계야
				temp.discard(text[left]) # 그렇다면 일단 왼쪽 것을 없애고 
				temp.add(text[right])
				left += 1
		else: # 이미 들어있던 건데
			if count < leng: # count가 현재 한계보다 작은 경우는
				right += 1
			else: # 근데 같아 어쩌라고 
				temp.discard(text[left]) # 그렇다면 일단 왼쪽 것을 없애고
				left += 1
		right += 1
	return ret

if n >= textLeng: # 최대 종류의 개수 n이 입력된 문자열의 길이보다 크거나 같다면 그냥 n을 출력하면 된다.
	print(n)
else: # 하지만 그렇지 않다면 경우의 수를 살펴봐야 한다.
	print(check(n))
