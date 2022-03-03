import sys
sys.setrecursionlimit(100000)

class Node:
    def __init__ (self,root,left,right):
        self.value = root
        self.left = left
        self.right = right

def findIdx(arr,idx,item):
    while True:
        if arr[idx] == item:
            return idx
        idx +=1

def calc(in_order,postorder,iStart,pStart,sz):
    if sz <=0:
        return None
    root = postorder[pStart +sz -1] #루트는 post의 맨 마지막
    rIdx = findIdx(in_order, iStart,root)
    leftSize = rIdx - iStart
    rightSize = sz - leftSize -1
    left = calc(in_order,postorder,iStart,pStart ,leftSize)
    right = calc(in_order,postorder,rIdx+1 ,pStart+leftSize,rightSize)
    tree = Node(root,left,right)
    return tree

def prePrint(tree):
    if tree == None:
        return
    print(tree.value,end = ' ')
    prePrint(tree.left)
    prePrint(tree.right)

def solve():
    n = int(input())
    in_order = [int(x) for x in input().split()]
    postorder = [int(x) for x in input().split()]
    tree = calc(in_order,postorder,0,0,n)
    prePrint(tree)

solve()
