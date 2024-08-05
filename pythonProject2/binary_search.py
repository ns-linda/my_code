class newNode:

    # Construct to create a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


# Returns true if given tree is BST.
def isBST(root, l=None, r=None):
    # Base condition
    if (root == None):
        return True

    # if left node exist then check it has
    # correct data or not i.e. left node's data
    # should be less than root's data
    if (l != None and root.data <= l.data):
        return False

    # if right node exist then check it has
    # correct data or not i.e. right node's data
    # should be greater than root's data
    if (r != None and root.data >= r.data):
        return False

    # check recursively for every node.
    return isBST(root.left, l, root) and \
           isBST(root.right, root, r)


# Driver Code
if __name__ == '__main__':
    root = newNode(3)
    root.left = newNode(2)
    root.right = newNode(5)
    root.right.left = newNode(1)
    root.right.right = newNode(4)
    # root.right.left.left = newNode(40)
    if (isBST(root, None, None)):
        print("Is BST")
    else:
        print("Not a BST")

import sys


# A class to store a BST node
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


# Recursive function to insert a key into a BST
def insert(root, key):
    # if the root is None, create a new node and return it
    if root is None:
        return Node(key)

    # if the given key is less than the root node, recur for the left subtree
    if key < root.data:
        root.left = insert(root.left, key)

    # if the given key is more than the root node, recur for the right subtree
    else:
        root.right = insert(root.right, key)

    return root


# Function to determine whether a given binary tree is a BST by keeping a
# valid range (starting from [-INFINITY, INFINITY]) and keep shrinking
# it down for each node as we go down recursively
def isBST(node, minKey, maxKey):
    # base case
    if node is None:
        return True

    # if the node's value falls outside the valid range
    if node.data < minKey or node.data > maxKey:
        return False

    # recursively check left and right subtrees with an updated range
    return isBST(node.left, minKey, node.data) and \
           isBST(node.right, node.data, maxKey)


# Function to determine whether a given binary tree is a BST
def checkForBST(root):
    if isBST(root, -sys.maxsize, sys.maxsize):
        print('The tree is a BST.')
    else:
        print('The tree is not a BST')


def swap(root):
    left = root.left
    root.left = root.right
    root.right = left


if __name__ == '__main__':

    keys = [15, 10, 20, 8, 12, 16, 25]

    root = None
    for key in keys:
        root = insert(root, key)

    # swap left and right nodes
    swap(root)
    checkForBST(root)


