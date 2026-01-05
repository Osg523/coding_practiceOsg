def solution(todo_list, finished):
    return [todo_list[i] for i,j in enumerate(finished) if not j]