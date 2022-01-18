#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define max(a,b) (((a) > (b)) ? (a) : (b))

typedef struct AVLNode	//root가 계속 바뀔 수 잇으니 AVLType은 만들지 않는다.
{
	int key;
	struct AVLNode* left;
	struct AVLNode* right;
}AVLNode;

int getHeight(AVLNode* node)
{
	int height = 0;
	if (node != NULL)
		height = 1 + max(getHeight(node->left), getHeight(node->right));

	return height;
}

int getBalance(AVLNode* node)
{
	if (node == NULL)
		return 0;

	return getHeight(node->left) - getHeight(node->right);
}

AVLNode* rotateRight(AVLNode* p)
{
	AVLNode* c = p->left;
	p->left = c->right;
	c->right = p;
	return c;
}

AVLNode* rotateLeft(AVLNode* p)
{
	AVLNode* c = p->right;
	p->right = c->left;
	c->left = p;
	return c;
}

AVLNode* createNode(int key)
{
	AVLNode* node = (AVLNode*)malloc(sizeof(AVLNode));
	node->key = key;
	node->left = node->right = NULL;
	return node;
}

AVLNode* insert(AVLNode* node, int key)
{
	if (node == NULL) //단말노드까지 와서 내가 더 이상 갈 곳이 없거나 아에 트리가 비어있는 경우
		return createNode(key);

	if (key < node->key)
		node->left = insert(node->left, key);
	else if (key > node->key)
		node->right = insert(node->right, key);
	else
		return node;

	int balance = getBalance(node);

	if (balance > 1 && key < node->left->key)	//LL타입인 경우이다.
		return rotateRight(node);

	if (balance > 1 && key > node->left->key)	//LR타입인 경우이다.
	{
		node->left = rotateLeft(node->left);
		return rotateRight(node);
	}

	if (balance < -1 && key >node->right->key)	//RR타입인 경우이다.
		return rotateLeft(node);

	if (balance <-1 && key < node->right->key)	//RL타입인 경우이다.
	{
		node->right = rotateRight(node->right);
		return rotateLeft(node);
	}

	return node;
}

void preOrder(AVLNode* root)
{
	if (root != NULL)
	{
		printf("[%d] ", root->key);
		preOrder(root->left);
		preOrder(root->right);
	}
}

int main()
{
	AVLNode* root = NULL;
	srand(time(NULL));

	for (int i = 0; i < 10; i++)
	{
		root = insert(root, rand() % 100 + 1);
		preOrder(root);
		printf("\n");
	}

}