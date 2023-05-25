#include <stdio.h>

int sum, val, max, mode;
int arr[100 + 2];

int main() 
{
	// freopen("input.txt", "r", stdin);
	
	for (int i = 0; i < 10; i++) 
	{
		scanf("%d", &val);
		sum += val;			// 합계
		arr[val / 10]++;	// 나타난 횟수
	}

	for (int i = 0; i < 100; i++) 
	{
		if (max < arr[i])
		{
			max = arr[i];
			mode = i * 10; // 원래 숫자
		}
			
	}
	printf("%d\n%d\n", sum / 10, mode);
}