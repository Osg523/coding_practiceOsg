#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int solution(const char* my_string, const char* is_prefix) {
    int answer = 1;

    for (size_t i = 0; i < strlen(is_prefix); i++) {
        if (my_string[i] != is_prefix[i]) {
            answer = 0;
        }
    }
    return answer;
}
