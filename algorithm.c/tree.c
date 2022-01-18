#include <stdio.h>
#include <stdlib.h>

#define max(a,b) (((a) > (b)) ? (a) : (b))

typedef int element;

typedef struct TreeNode
{
    element key;
    struct TreeNode* left, * right;
}TreeNode;

TreeNode* insertNode(TreeNode* root, element key)
{
    if (root == NULL) //아에 root가 없을경우
    {
        TreeNode* node = (TreeNode*)malloc(sizeof(TreeNode));
        node->key = key;
        node->left = node->right = NULL; //이진탐색트리에서 삽입노드의 경우 단말노드이다.
        return node;
    }

    if (key < root->key)
        root->left = insertNode(root->left, key);
    else if (key > root->key)
        root->right = insertNode(root->right, key);

    return root;

}

void preOrder(TreeNode* root)
{
    if (root != NULL)
    {
        printf("[%d] ", root->key);
        preOrder(root->left);
        preOrder(root->right);
    }
}

void inOrder(TreeNode* root)
{
    if (root != NULL)
    {
        inOrder(root->left);
        printf("[%d] ", root->key);
        inOrder(root->right);
    }
}

void postOrder(TreeNode* root)
{
    if (root != NULL)
    {
        postOrder(root->left);
        postOrder(root->right);
        printf("[%d] ", root->key);
    }
}

int getnodeCount(TreeNode* root)
{
    int count = 0;
    if (root != NULL)
        count = 1 + getnodeCount(root->left) + getnodeCount(root->right);

    return count;
}

int getleafnodeCount(TreeNode* root)
{
    int count = 0;

    if (root != NULL)
    {
        if (root->left == NULL && root->right == NULL)
            return 1 ;
        else
            count = getleafnodeCount(root->left) + getleafnodeCount(root->right);
    }
    return count;
}

int getHeight(TreeNode* root)
{
    int height = 0;
    if (root != NULL)
        height = 1 + max(getHeight(root->left), getHeight(root->right));
    return height;
}

TreeNode* minValue(TreeNode* root)
{
    TreeNode *p = root;
    while(p->left != NULL)
        p = p->left;
    return p;
}
TreeNode* deleteNode(TreeNode* root, element key)
{
    if (root == NULL) //두가지의 의미 1.빈 루트를 전달 했거나 2.찾는 값이 없거나
        return root;

    if (key < root->key)
        root->left = deleteNode(root->left, key);
    else if (key > root->key)
        root->right = deleteNode(root->right, key);
    
    else
    {
        if (root->left == NULL)//여기서는 단말인 경우와 양쪽 중 한쪽이라도 있는 경우를 같은 경우라고 보는거 
        {                  //why? 오른쪽이 있으면 그냥 오른쪽 연결 오른쪽이 null이면 그냥 null연결 어차피 이진탐색트리는 공집합도 서브트리라고 여긴다.
            TreeNode* temp = root->right;
            free(root);
            return temp;
        }
        else if (root->right == NULL) //여기로 왔다는 것은 오른쪽이 있다는 말
        {
            TreeNode* temp = root->left;
            free(root);
            return temp;
        }
        else
        {
            TreeNode* temp = minValue(root->right);
            root->key = temp->key;
            root->right = deleteNode(root->right, temp->key);
        }
    }

    return root;
}
int main()
{
    TreeNode* root = NULL;
    
    root = insertNode(root, 35);
    root = insertNode(root, 68);
    root = insertNode(root, 99);
    root = insertNode(root, 18);
    root = insertNode(root, 7);
    root = insertNode(root, 3);
    root = insertNode(root, 12);
    root = insertNode(root, 26);
    root = insertNode(root, 22);
    root = insertNode(root, 30);

    preOrder(root); printf("\n");
    inOrder(root); printf("\n");
    postOrder(root); printf("\n");

    printf("%d %d %d\n", getnodeCount(root),getleafnodeCount(root),getHeight(root));
    
    root = deleteNode(root, 30); preOrder(root); printf("\n");
    root = deleteNode(root, 26); preOrder(root); printf("\n");
    root = deleteNode(root,18 ); preOrder(root); printf("\n");
    root = deleteNode(root, 35); preOrder(root); printf("\n");

    
    return 0;
}