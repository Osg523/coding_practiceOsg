#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// num_list_len은 배열 num_list의 길이입니다.
int solution(int num_list[], size_t num_list_len, int n) {
    int answer = 0;
    
    if ((num_list_len >= 3 && num_list_len <=100) && (n >= 1 && n <=100)){
         for (int i=0; i<100; i++) {
             if (num_list[i] >= 1 && num_list[i] <= 100) {
                 if (num_list[i] == n) {
                    answer = 1;
                 }
             }  
         }
    }
        
    return answer;
}

