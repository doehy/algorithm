n = int(input())
text = list(input())

for i in text:


# 001010110
# 000010111
# 000001111

# 011110010
# 001110011
# 000110111
# 000011111
# 0, 1 및/또는 ? 문자로 구성된 문자열이 제공됩니다. 패턴이라고 하죠.

# 이진 문자열(각 문자가 0 또는 1인 문자열)이 패턴과 일치한다고 가정합니다. 각 문자를 0 또는 1(각 문자에 대한 선택은 독립적임)로 대체하여 문자열이 동일해지도록 할 수 있습니다. 예를 들어 0010은 ?01?과 일치하지만 010은 1?, ??, ?? 또는 ???와 일치하지 않습니다.

# 이진 문자열의 비용을 문자열을 내림차순으로 정렬하는 데 필요한 "문자열의 임의의 연속 하위 문자열 역방향" 형식의 최소 작업 수로 정의합니다.

# 당신은 주어진 패턴과 일치하는 것들 중에서 가능한 최소 비용의 이진 문자열을 찾아야 합니다. 답변이 여러 개인 경우 해당 답변 중 하나를 인쇄합니다.

# 입력
# 첫 번째 줄에는 검정 사례의 수인 단일 정수 t(1≤t≤3≤104)가 포함됩니다.

# 각 테스트 케이스의 첫 번째 줄과 유일한 줄에는 문자 0, 1 및/또는 ?로 구성된 문자열(1≤|s|≤3≤105)이 포함됩니다.

# 모든 테스트 사례에 대한 문자열 길이의 합은 3⁄105를 초과하지 않습니다
# .

# 산출량
# 각 테스트 사례에 대해 주어진 패턴과 일치하는 이진 문자열 중 가능한 최소 비용으로 이진 문자열을 인쇄합니다. 답변이 여러 개인 경우 해당 답변 중 하나를 인쇄합니다.

# 메모
# 예제의 첫 번째 테스트 사례에서 결과 문자열의 비용은 0입니다.

# 두 번째 테스트 사례에서 결과 문자열의 비용은 2입니다. 하위 문자열을 1번째 문자에서 5번째 문자로 역변환할 수 있으며 문자열 00101을 얻을 수 있습니다. 그런 다음 하위 문자열을 3번째 문자에서 4번째 문자로 역변환하고, 내림차순으로 정렬된 문자열 00011을 얻습니다.