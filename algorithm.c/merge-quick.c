#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define SIZE 15
#define SWAP(x,y,z) ((z) = (x),(x) = (y), (y) = (z))

void makeList(int list[])
{
	for (int i = 0; i < SIZE; i++)
		list[i] = rand() % 100 + 1;
}

void printList(int list[])
{
	for (int i = 0; i < SIZE; i++)
		printf("%d ", list[i]);
	printf("\n");
}

void merge(int list[], int sorted[], int left, int mid, int right)
{
	int i, j, k,l; //여기서 k는 sorted 배열을 따라다닐 것이다.
	i = left, j = mid + 1; k = left;

	while (i <= mid && j <= right)
	{
		if (list[i] <= list[j])
			sorted[k++] = list[i++];
		else
			sorted[k++] = list[j++];
	}

	if (i > mid)
		for (l = j; l <= right; l++)
			sorted[k++] = list[l]; //위에 for문에서 l++를 해주고 있기 때문에 따로 l값을 증가시키지 않음
	else
		for (l = i; l <= mid; l++)
			sorted[k++] = list[l];

	//위에서 정렬했지만 원래 배열에 기록을 해줘야함
	for (l = left; l <= right; l++)
		list[l] = sorted[l];


}

void mergeSort(int list[], int sorted[], int left, int right)
{
	int mid;
	if (left < right) //조건의 뜻은 분할이 가능하다면 이 뜻이다.
	{
		mid = (left + right) / 2;
		mergeSort(list, sorted, left, mid); //먼저 왼쪽을 나누는 것
		mergeSort(list, sorted, mid + 1, right); //그 다음 오른쪽을 나누는 것
		merge(list, sorted, left, mid, right);// 정렬을 한다.
	}


}

//퀵정렬
//평균적으로 가장 빠른 정렬 방법,분할정복법 사용,무작위로 피벗을 선택하여 피벗값을 기준으로 정렬
//추가 배열이 필요하지 않음

int partition(int list[], int left, int right)
{
	int pivot, temp, low, high;

	pivot = list[left]; //일단 맨 왼쪽 값을 주는거임.
	low = left; high = right + 1; //do while문을 할 것이기 때문에 low는 left를 주는것임 do while문에 의해
	//시작하자마자 오른쪽으로 갈 것이기 때문에 high를 right+1을 주는 이유도 do while문에 의해 시작하자마자
	//범위를 벗어나 있다가 배열로 들어올 것이다.

	do
	{
		do 
			low++;
		 while (list[low] < pivot);

		 do
			 high--;
		 while (list[high] > pivot);

		 if (low < high) //함부로 스왑을 해주면 안되기 때문에 low가 high보다 작은지 확인하고 스왑을 해준다. 
			 SWAP(list[low], list[high], temp);
	} while (low < high);

	SWAP(list[left], list[high], temp);
	return high;
}
void quickSort(int list[], int left, int right)
{
	if (left < right)
	{
		int q = partition(list, left, right);
		quickSort(list, left, q - 1);
		quickSort(list, q + 1, right);
	}
}

int main()
{
	int list[SIZE], sorted[SIZE];
	srand(time(NULL));

	makeList(list);
	printList(list);

	//mergeSort(list, sorted, 0, SIZE - 1);
	quickSort(list, 0, SIZE - 1);
	printList(list);
}