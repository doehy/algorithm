#include <stdio.h>
#include <stdlib.h>

#define FALSE 0
#define TRUE 1

typedef struct IncidentEdge // 정점에 연결된 간선
{
	char aName; //간선에 의해 연결된 인접정점에 이름을 나타내기 위한 변수
	int weight; //나중에 응용문제를 풀기위해 미리 넣어둔 가중치 변수
	struct IncidentEdge* next;
}IncidentEdge;

typedef struct Vertex //정점구조
{
	char vName; //정점의 이름
	int isVisit; //DFS , BFS를 하면서 추가한 변수이다. 정점을 갔다왔는지 아닌지를 판별해준다.
	IncidentEdge* iHead; //나와 연결된 간선들의 리스트
	struct Vertex* next;
}Vertex;

typedef struct	//위에 정점과 간선 구조를 아우르는 그래프구조 정점을 기준으로 그래프를 판단할 것이고 제일 첫번째로 만들어지는 정점이 트리의 루트노드라고 생각
{		
	Vertex * vHead;
}Graph;

void init(Graph* G)
{
	G->vHead = NULL;
}

void makeVertex(Graph* G, char vName) //정점을 만드는 함수
{
	Vertex* v = (Vertex*)malloc(sizeof(Vertex));
	v->vName = vName;
	v->isVisit = FALSE;//2번째 강의떄 만들어진 라인 처음 만들어지는 정점은 들렀을리가 없기 때문에 FALSE로 만듦.
	v->iHead = NULL;
	v->next = NULL; //단순연결리스트 이므로 나의 다음에는 NULL값은 넣어놓는다.

	Vertex* q = G->vHead;//insertLast형태로 만들 것이다.
	if (q == NULL)
		G->vHead = v;
	else
	{
		while (q->next != NULL)
			q = q->next;
		q->next = v;
	}
}

void makeIncidentEdge(Vertex* v, char aName, int w) //makeVertex와 같은 구조이다.
{
	IncidentEdge* p = (IncidentEdge*)malloc(sizeof(IncidentEdge));
	p->aName = aName;
	p->weight = w;
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
	Vertex* v = G->vHead; //처음부터 찾아야하니까 G(그래프)->vHead를 주는 것이다.
	while (v->vName != vName)
		v = v->next;
	return v;
}

void insertEdge(Graph* G, char v1, char v2, int w)
{
	Vertex* v = findVertex(G, v1); //간선을 연결시키기 위해서는 일단 그 정점이 어디있는지 찾아야한다.
	makeIncidentEdge(v, v2, w);
	v = findVertex(G, v2); //반대의 상황에서도 연결되어 있는것이기 때문에 반대로도 한번 해준다.
	makeIncidentEdge(v, v1, w);
}

void dfs(Graph* G, char vName) //그래프와 시작정점의 이름을 인자값으로 준다.
{
	Vertex* v = findVertex(G, vName);
	IncidentEdge* p;

	if (v->isVisit == FALSE)
	{
		v->isVisit = TRUE;
		printf("(%c) ", v->vName);
	}

	for (p = v->iHead; p != NULL; p = p->next)
	{
		v = findVertex(G, p->aName);
		if (v->isVisit == FALSE)
			dfs(G, v->vName);
	}
}

void bfs(Graph* G, char vName)
{
	Vertex* v = findVertex(G, vName);
	IncidentEdge* p;
	Vertex* q; //bfs에서는 정점 포인터를 하나 더 만들어준다.

	if (v->isVisit == FALSE)
	{
		v->isVisit = TRUE;
		printf("(%c) ", v->vName);
	}

	while (v != NULL)
	{
		for (p = v->iHead; p != NULL; p = p->next)
		{
			q = findVertex(G, p->aName);
			if (q->isVisit == FALSE)
			{
				q->isVisit = TRUE;
				printf("(%c) ", q->vName);
			}
		}
		v = v->next;
	}



}

void print(Graph* G)
{
	Vertex* p = G->vHead;
	IncidentEdge* q;
	for (; p != NULL; p = p->next)
	{
		printf("(%c) : ", p->vName);
		for (q = p->iHead; q != NULL; q = q->next)
			printf("(%c , %d) ", q->aName, q->weight);
		printf("\n");
	}
	printf("\n");
}


int main()
{
	Graph G; //그래프를 만들고
	init(&G); //그래프를 초기화 시켰다.

	//정점들을 만들었다.
	makeVertex(&G, 'a'); makeVertex(&G, 'b'); makeVertex(&G, 'c');
	makeVertex(&G, 'd'); makeVertex(&G, 'e');

	//정점들을 연결시켜주는 간선들을 만들었다. 뒤에 숫자들은 가중치를 의미하는 것인데
	//일단 지금은 아무 의미가 없다.
	insertEdge(&G, 'a', 'b', 1); insertEdge(&G, 'a', 'c', 2);
	insertEdge(&G, 'a', 'e', 3); insertEdge(&G, 'b', 'c', 1);
	insertEdge(&G, 'c', 'd', 1); insertEdge(&G, 'c', 'e', 3);
	insertEdge(&G, 'd', 'e', 1); 

	print(&G);

	dfs(&G, 'a'); printf("\n");
	bfs(&G, 'a'); printf("\n");

	return 0;
} 