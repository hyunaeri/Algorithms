#pragma warning (disable: 4996)
#include <stdio.h>

int main(void) {

	int year; scanf("%d", &year);

	if ((year % 4 == 0 && year % 100 != 0) || (year % 4 == 0 && year % 400 == 0)) {

		printf("1"); // 윤년은 1을 출력
	}

	else
		printf("0");  // 평년은 0을 출력

	return 0;
}