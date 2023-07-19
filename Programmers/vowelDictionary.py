def solution(word):
    answer = 0
    wordList = []
    words = "AEIOU"
    def dfs(cnt, temp):
        if cnt == 5:
            return 
        for i in range(len(words)):
            wordList.append(temp+words[i])
            dfs(cnt+1, temp + words[i])
    dfs(0, "")
    return wordList.index(word) + 1