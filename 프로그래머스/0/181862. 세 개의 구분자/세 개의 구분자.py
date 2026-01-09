def solution(myStr):
    if len(myStr.translate(str.maketrans("abc","   ")).strip()) != 0:
        return myStr.translate(str.maketrans("abc","   ")).strip(" ").split()
    return ["EMPTY"]