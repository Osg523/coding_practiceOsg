solution = lambda num_list: num_list.index([i for i in num_list if i < 0][0]) if len([i for i in num_list if i < 0]) != 0 else -1

""" 
배운점
1.([i for i in range(len(num_list)) if num_list[i] < 0] or [-1])[0] 
> or 연산자는 앞에가 빈 리스트면 뒤에 값을 반환한다.
2.next()함수는 iter객체에서 사용할 수 있다. iter객체의 존재를 알게 되었다.
""'
