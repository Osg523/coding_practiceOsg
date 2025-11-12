def solution(s):
    answer = ""
    dic = {"zero":0,"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}
    num = ""
    lis1 = []
    for i in s:
        if i <= "9":
            lis1.append(i)
        else:
            num += i
            
        for k in dic:
            if num in dic:
                lis1.append(num)
                num = ""
            
    for i in lis1:
        if i in dic:
            answer += str(dic[i])
        else:
            answer += i
    
    return int(answer)

#푼 뒤 피드백에서 배운점: replace()라는 함수를 알게됨
