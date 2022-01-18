#include <stdio.h>
#include <stdlib.h>

typedef struct Edge //12주차 부터 edgㄷ가 추가됨.
{
    char v1, v2;
    int weight;
    struct Edge* next;
}Edge;

typedef struct IncidentEdge
{
    char aName;
    Edge* e;
    struct IncidentEdge* next;
}IncidentEdge;

typedef struct Vertex
{
    char vName;
    IncidentEdge* iHead;
    struct Vertex* next;
}Vertex;

typedef struct
{
    Vertex* vHead;
    Edge* eHead;        //12주차 새로 추가된 변수 
    int eCount, vCount;//정점의 n-1개의 간선을 만드는 것이니 개수를 세워줘야한다.
}Graph;

void init(Graph* G) //init함수도 바뀌었다.
{
    G->vHead = NULL;
    G->eHead = NULL;
    G->vCount = G->eCount = 0;
}

void makeVertex(Graph* G, char vName)
{
    Vertex* v = (Vertex*)malloc(sizeof(Vertex));
    v->vName = vName;
    v->iHead = NULL;
    v->next = NULL;
    G->vCount++;

    Vertex* q = G->vHead;
    if (q == NULL)
        G->vHead = v;
    else
    {
        while (q->next != NULL)
            q = q->next;
        q->next = v;
    }
}

void makeIncidentEdge(Vertex* v, char aName, Edge* e)
{
    IncidentEdge* p = (IncidentEdge*)malloc(sizeof(IncidentEdge));
    p->aName = aName;
    p->e = e;
    p->next = NULL;
    IncidentEdge* q = v->iHead;
    if (q == NULL)
        v->iHead = p;
    else
    {
        while (q->next != NULL)
            q = q->next;
        q->next = p;
    }
}

Vertex* findVertex(Graph* G, char vName)
{
    Vertex* v = G->vHead;
    while (v->vName != vName)
        v = v->next;
    return v;
}

void insertEdge(Graph* G, char v1, char v2, int w)
{
    Edge* e = (Edge*)malloc(sizeof(Edge));
    e->weight = w;
    e->v1 = v1;
    e->v2 = v2;
    e->next = NULL;
    G->eCount++;

    Edge* q = G->eHead;
    if (q == NULL)
        G->eHead = e;
    else
    {
        while (q->next != NULL)
            q = q->next;
        q->next = e;
    }
    Vertex* v = findVertex(G, v1);
    makeIncidentEdge(v, v2, e);
    v = findVertex(G, v2);
    makeIncidentEdge(v, v1, e);
}

void print(Graph* G)
{
    Vertex* p = G->vHead;
    IncidentEdge* q;
    for (; p != NULL; p = p->next)
    {
        printf("[%c] : ", p->vName);
        for (q = p->iHead; q != NULL; q = q->next)
            printf("[%c, %d] ", q->aName, q->e->weight);
        printf("\n");
    }
    printf("\n");
}

void incSort(Graph* G, Edge* e[]) //12주차 첫번쨰 강의
{
    int i, least;
    Edge* p = G->eHead;
    for (i = 0; i < G->eCount; i++)
    {
        e[i] = p;
        p = p->next;
    }

    for (i = 0; i < G->eCount - 1; i++)
    {
        least = i;
        for (int j = i + 1; j < G->eCount; j++)
            if (e[j]->weight < e[least]->weight)
                least = j;

        p = e[least];
        e[least] = e[i];
        e[i] = p;
    }

    for (i = 0; i < G->eCount; i++)
        printf("[%c%c(%d)] ", e[i]->v1, e[i]->v2, e[i]->weight);
    printf("\n\n");
}

int vFind(int v[], int vNum)
{
    if (v[vNum] == -1)
        return vNum;

    while (v[vNum] != -1)
        vNum = v[vNum];
    return vNum;
}

void vUnion(int v[], int vNum1, int vNum2)
{
    int r1 = vFind(v, vNum1);
    int r2 = vFind(v, vNum2);

    if (r1 != r2)
        v[r2] = r1;
}
void kruskal(Graph* G, Edge* e[], int v[])
{
    int eCnt = 0,i=0;//빨강색을 칠해는지는 간선의 개수 그리고 배열의 인덱스 i를 0으로 초기화
    int vNum1, vNum2; //정점 번호
    Edge* p;

    while (eCnt < G->vCount - 1) 
    {
        p = e[i];
        vNum1 = vFind(v, p->v1 - 97); //97은 아스키코드값으로 'a'이고 배열의 인덱스와 연결해주기 위해서 빼는것임
        vNum2 = vFind(v, p->v2 - 97);

        if (vNum1 != vNum2) //다르다는 것은 서로부모가 다르다는 것이고 그러면 사이클이 안 만들어진다는 의미
        {                   //고래서 일단 출력을 해준다.
            printf("%d. [%c%c (%d)]\n", eCnt + 1, p->v1, p->v2, p->weight);
            eCnt++;
            vUnion(v, vNum1, vNum2); //빨강색 선이 그어진 부분을 합집합으로 만들어줘야함 만들어주는 함수
        }
        i++;
    }
}
int main()
{
    Graph G;
    init(&G);


    makeVertex(&G, 'a'); makeVertex(&G, 'b'); makeVertex(&G, 'c');
    makeVertex(&G, 'd'); makeVertex(&G, 'e'); makeVertex(&G, 'f');
    makeVertex(&G, 'g');

    insertEdge(&G, 'a', 'b', 29); insertEdge(&G, 'a', 'f', 10);
    insertEdge(&G, 'b', 'c', 16); insertEdge(&G, 'b', 'g', 15);
    insertEdge(&G, 'c', 'd', 12); insertEdge(&G, 'd', 'g', 18);
    insertEdge(&G, 'd', 'e', 22); insertEdge(&G, 'e', 'f', 27);
    insertEdge(&G, 'e', 'g', 25);

    print(&G);

    Edge* e[20]; //정렬된 간선을 저장할 간선들의 포인터를 기억할 배열을 만들고 20은 그냥 넉넉한 공간을 확보한것이다.
    incSort(&G, e);

    //이 주석을 기준으로 위에는 정렬을 한 거고 이제 밑에서는 크루스칼 알고리즘을 구현할 것이다.

    int v[10] = { -1,-1, -1, -1, -1, -1, -1, -1, -1, -1 }; //개수에 맞게 -1로 다 초기화를 시켜놓은 것이다.
    kruskal(&G, e, v); 
    

}