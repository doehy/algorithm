#include <stdio.h>
#include <stdlib.h>

#define SIZE 100

typedef int element;

typedef struct
{
    element heap[SIZE];
    int n;
}HeapType;

void init(HeapType* HT)
{
    HT->n = 0;
}

void upheap(HeapType* HT)
{
    int i = HT->n; //부모노드와 크기비교를 위해 저장해둠
    int k = HT->heap[i]; //나중에 k가 자기위치를 찾으면 그 위치에 k가 들어갈 것이기 때문에 기억해둔다.

    while ((i != 1) && (k < HT->heap[i / 2]))
    {
        HT->heap[i] = HT->heap[i / 2];
        i /= 2;
    }
    HT->heap[i] = k;
}

void downHeap(HeapType* HT)
{
    int temp = HT->heap[1]; //삭제를 위해 제일 위로 올려놓은 값을 기억해둔다.
    int p = 1, c = 2;    //부모노드를 의미하는 p를 1로하고 왼쪽자식노드를 의미하는 c를 2로 저장해둔다.

    while (c <= HT->n) //마지막 노드까지 비교하기 위한 조건이다.
    {
        if ((c < HT->n) && (HT->heap[c + 1] < HT->heap[c]))// 이 조건을 만족한다는 것은 형제 노드가 있다는 것이고 형제 노드가 있으니 형제 노드끼리 크기를 비교하는 것이다.
            c++;// 이어서 형제노드끼리 비교를 할 때 여기서 부등호를 저렇게 하면 최소히프를 만족한다 했는데 아닌 것 같다. 부등호를 반대로 하면 밑에 c++가 아니라 조건 바로옆에 ';'를 써서 왼쪽으로 내려가면 된다. 이렇게 해도 최소히프를 할 수 있다.
        if (temp <= HT->heap[c]) // 지금 강의에서 하고 있는 것이 최소히프이니 자식노드보다 작다면 빠져나오는 것이다.
            break;
        HT->heap[p] = HT->heap[c];
        p = c;
        c *= 2;
    }
    HT->heap[p] = temp;
}
void insertItem(HeapType* HT, int k)
{
    HT->n++;
    HT->heap[HT->n] = k;
    upheap(HT);
}

int removeItem(HeapType* HT) //최대히프에서의 삭제는 가장 큰 키값을 삭제하는 것이니 루트를 삭제해주면 된다.
{
    int k = HT->heap[1]; //그래서 첫번째 값을 기억시키는 것이다.
    HT->heap[1] = HT->heap[HT->n];//히프에서의 삭제는 마지막 노드를 제일 위로 올리는 것이다.
    HT->n--;
    downHeap(HT);
    return k;
}

void heapSort(HeapType* HT1, element H[]) //원본히프를 살려놓는 히프정렬
{
    HeapType HT2; //새로운 히프를 만들어 준다.
    init(&HT2);

    for (int i = 1; i <= HT1->n; i++) //여기서 = 을 붙여야 한다.
    {
        HT2.heap[i] = HT1->heap[i];
        HT2.n++;
    }

    for (int i = 1; i <= HT1->n; i++)
        H[i] = removeItem(&HT2);    //HT2를 remove하면서 최소값을 새로운 배열H에 정렬하는 것이다.
}

void inPlaceHeapSort(HeapType* HT)
{
    int n = HT->n;
    int key;
    for (int i = 0; i < n; i++)
    {
        key = removeItem(HT); //제일 작은 값(지금 하고 있는 것이 최소히프이니)이 key에 들어갈 것이고
        HT->heap[HT->n + 1] = key;//위에서 리무브를 해서 n이 1 줄어들어 있으니 1을 증가시켜준 다음에 key를 넣으면 내림차순으로 정렬이 될 것이다.
    }
}
void printHeap(HeapType* HT)
{
    for (int i = 1; i <= HT->n; i++)
        printf("[%d] ", HT->heap[i]);
    printf("\n");
}

void printArray(int H[], int n)
{
    for (int i = 1; i <= n; i++)
        printf("[%d] ", H[i]);
    printf("\n");
}
int main()
{
    HeapType HT;
    init(&HT);
    element H[SIZE];

    srand(time(NULL));

    for (int i = 0; i < 10; i++)
    {
        int k = rand() % 100 + 1;
        insertItem(&HT, k);
        printf("[%d] ", k);
    }
    printf("\n"); getchar();
    printHeap(&HT);

    printf("Mint Value : %d\n", removeItem(&HT));
    printHeap(&HT); getchar();

    heapSort(&HT, H);
    printArray(H, HT.n);
    getchar();

    int n = HT.n;
    inPlaceHeapSort(&HT);
    printArray(HT.heap, n);
    printHeap(&HT); //아무것도 출력이 되지 않는다. 위에 inpalce함수를 써 제자리 정렬이 돼서 원본 배열이 깨져있기 때문이다.

    return 0;
}