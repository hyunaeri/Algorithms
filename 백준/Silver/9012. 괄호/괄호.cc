#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

// 백준 9012 괄호 (스택 구현 문제)

char str[51]; // 하나는 널문자를 위해 여유를..
int N;

int main() {
    int value; // 항상 0보다 크거나 같음을 유지하면서 반복문을 돌아야함.
    scanf("%d", &N);

    for(int i = 0; i < N; i++) {

        value = 0;
        scanf("%s", str);

        for(int j = 0; j < strlen(str); j++) {

            if(value < 0)
                break;

            if(str[j] == '(')
                value++;
            if(str[j] == ')')
                value--;


        }
        if(value == 0)
            printf("YES\n");
        else
            printf("NO\n");
    }
}