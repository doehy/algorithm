#include <stdio.h>
#include <stdlib.h>

#define FALSE 0
#define TRUE 1

typedef struct Edge
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
    int isVisit;
    IncidentEdge* iHead;
    struct Vertex* next;
}Vertex;

typedef struct
{
    Vertex* vHead;
    Edge* eHead;
    int eCount, vCount;
}Graph;

void init(Graph* G)
{
    G->vHead = NULL;
    G->eHead = NULL;
    G->vCount = G->eCount = 0;
}

void makeVertex(Graph* G, char vName)
{
    Vertex* v = (Vertex*)malloc(sizeof(Vertex));
    v->vName = vName;
    v->isVisit = FALSE;
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

char getMinVertex(Graph* G, int d[])
{
    Vertex* p = G->vHead;
    char vName;

    for (; p != NULL; p = p->next)
    {
        if (p->isVisit == FALSE)
        {
            vName = p->vName;
            break;
        }
    }
    //여기까지 왔다는 것은 한번도 방문하지 않았던 정점에 이름을 vName이 가지고 있을 것이다.
    
    for (p = G->vHead; p != NULL; p = p->next)
        if (p->isVisit == FALSE && (d[p->vName - 97] < d[vName - 97]))
            vName = p->vName;

    return vName;
}
void prim(Graph* G, char vName, int d[])
{
    Vertex* p = findVertex(G, vName);
    IncidentEdge* q;
    char c;

    d[p->vName - 97] = 0;

    for (int i = 0; i < G->vCount; i++)
    {
        c = getMinVertex(G, d);
        p = findVertex(G, c);
        p->isVisit = TRUE;
        printf("(%c) ", p->vName);
        for (q = p->iHead; q != NULL; q = q->next)
        {
            p = findVertex(G, q->aName);
            if (p->isVisit == FALSE)
                d[q->aName - 97] = q->e->weight;
        }
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

    int d[10] = { 100,100, 100, 100, 100, 100, 100, 100, 100, 100 };

    prim(&G,'b',d);

}