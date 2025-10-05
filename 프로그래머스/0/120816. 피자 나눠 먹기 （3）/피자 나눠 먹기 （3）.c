#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int slice, int n) {
    int answer = 0;
    answer = n / slice;
    int k = n % slice;
    if (k>0){
        answer += 1;
    }
    return answer;
}