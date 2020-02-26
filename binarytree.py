#!python
from queue import LinkedQueue
from stack import Stack
""" 
    O(1)constant time
    O(n) looping
    O(n^2) nested for loop, exponentially increasing
"""


class BinaryTreeNode(object):
    def __init__(self, data):
        """Initialize this binary tree node with the given data."""
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        """Return a string representation of this binary tree node."""
        return 'BinaryTreeNode({!r})'.format(self.data)

    def is_leaf(self):
        """Return True if this node is a leaf (has no children)."""
        return self.left is None and self.right is None

    def is_branch(self):
        """Return True if this node is a branch (has at least one child)."""
        return self.left is not None or self.right is not None

    def height(self, node='empty'):
        """Return the height of this node (the number of edges on the longest
        downward path from this node to a descendant leaf node).
        TODO: Best and worst case running time: ??? under what conditions?"""
        # for first loop
        if node == 'empty':
            if self.data is not None:
                node = self
            elif self.is_leaf():
                return 1
            else:
                # self (root Node) is empty!
                return 0
        left_edges = 0
        right_edges = 0
        # recursively add 1 to the height of node's left & right if they're not empty
        if node.left is not None:
            left_edges = self.height(node.left) + 1
        if node.right is not None:
            right_edges = self.height(node.right) + 1
        # Find the longer edge and return it
        if left_edges > right_edges:
            return left_edges
        else:
            return right_edges


class BinarySearchTree(object):
    def __init__(self, items=None):
        """Initialize this binary search tree and insert the given items."""
        self.root = None
        self.size = 0
        if items is not None:
            for item in items:
                self.insert(item)

    def __repr__(self):
        """Return a string representation of this binary search tree."""
        return 'BinarySearchTree({} nodes)'.format(self.size)

    def is_empty(self):
        """Return True if this binary search tree is empty (has no nodes)."""
        return self.root is None

    def height(self):
        """Return the height of this tree (the number of edges on the longest
        downward path from this tree's root node to a descendant leaf node).
        TODO: Best and worst case running time: ??? under what conditions?"""
        if self.root is not None:
            return self.root.height()

    def get_size(self, node):
        """Return the total number of Nodes including and below the given node"""
        if node is None:
            return 0
        else:
            return self.get_size(node.left) + self.get_size(node.right) + 1

    def contains(self, item):
        """Return True if this binary search tree contains the given item.
        Best case running time: O(log(n)) if the tree is balanced
        Worst case running time: O(n) if it's one sided and you have to check every single node"""
        # Find a node with the given item, if any
        node = self._find_node_recursive(item, self.root)
        # Return True if a node was found, or False
        return node is not None

    def search(self, item):
        """Return an item in this binary search tree matching the given item,
        or None if the given item is not found.
        Best case running time: O(log(n)) if the tree is balanced
        Worst case running time: O(n) if it's one sided and you have to check every single node"""
        # Find a node with the given item, if any
        node = self._find_node_recursive(item, self.root)
        if node is not None:
            return node.data
        return None

    def insert(self, item):
        """Insert the given item in order into this binary search tree.
        Best case running time: O(log(n)) if the tree is balanced or O(1) for the first insertion
        Worst case running time: O(n) if it's one sided and you have to check every single node to find the parent"""
        # Handle the case where the tree is empty
        if self.is_empty():
            self.root = BinaryTreeNode(item)
            self.size += 1
            return None
        # Find the parent node of where the given item should be inserted
        parent = self._find_parent_node_recursive(item, self.root)
        # item isn't inserted & self.size isn't updated if it's already in the tree
        if parent is not None and self._find_node_recursive(item, parent) is None:
            if parent.data > item:
                parent.left = BinaryTreeNode(item)
            else:
                parent.right = BinaryTreeNode(item)
            self.size += 1

    def _find_node_iterative(self, item):
        """Return the node containing the given item in this binary search tree,
        or None if the given item is not found. Search is performed iteratively
        starting from the root node.
        Best case running time: O(log(n)) if the tree is balanced or O(1) if it's empty
        Worst case running time: O(n) if it's one sided and you have to check every node to find the item"""
        # Start with the root node
        node = self.root
        # Loop until we descend past the closest leaf node
        while node is not None:
            if node.data == item:
                # Return the found node
                return node
            elif node.data > item:
                node = node.left
            elif node.data < item:
                node = node.right
        # Not found
        return None

    def _find_node_recursive(self, item, node):
        """Return the node containing the given item in this binary search tree,
        or None if the given item is not found. Search is performed recursively
        starting from the given node (give the root node to start recursion).
        Best case running time: O(log(n)) if the tree is balanced or O(1) if it's empty
        Worst case running time: O(n) if it's one sided and you have to check every node to find the item"""
        # Check if starting node exists
        if node is None:
            # Not found (base case)
            return None
        elif node.data == item:
            # Return the found node
            return node
        elif node.data > item:
            if node.left is not None:
                return self._find_node_recursive(item, node.left)
        elif node.data < item:
            if node.right is not None:
                return self._find_node_recursive(item, node.right)

    def _find_parent_node_iterative(self, item):
        """Return the parent node of the node containing the given item
        (or the parent node of where the given item would be if inserted)
        in this tree, or None if this tree is empty or has only a root node.
        Search is performed iteratively starting from the root node.
        Best case running time: O(log(n)) if the tree is balanced or O(1) if the root is a leaf or the tree is empty
        Worst case running time: O(n) if it's one sided and you have to check every node to find the item"""
        # Start with the root node and keep track of its parent
        node = self.root
        parent = None
        # Loop until we descend past the closest leaf node
        while node is not None:
            if item == node.data:
                # Return the parent of the found node
                return parent
            elif item < node.data:
                parent = node
                node = node.left
            elif item > node.data:
                parent = node
                node = node.right
        # Not found
        return parent

    def _find_parent_node_recursive(self, item, node, parent=None):
        """Return the parent node of the node containing the given item
        (or the parent node of where the given item would be if inserted)
        in this tree, or None if this tree is empty or has only a root node.
        Search is performed recursively starting from the given node
        (give the root node to start recursion)."""
        # Check if starting node exists
        if node is None:
            # Not found (base case)
            return None
        if node.data == item:
            # Return the parent of the found node
            return parent
        elif item < node.data:
            if node.left is not None:
                return self._find_parent_node_recursive(item, node.left, node)
            # node is the parent
            return node
        elif item > node.data:
            if node.right is not None:
                return self._find_parent_node_recursive(item, node.right, node)
            # node is the parent
            return node

    def delete(self, item):
        """Remove given item from this tree, if present, or raise ValueError.
        Best case running time: O(log(n)) if the tree is balanced or O(1) if the root is a leaf or the tree is empty
        Worst case running time: O(n) worst would be if the tree is unbalanced and the node being deleted has 2 children"""

        node = self._find_node_recursive(item, self.root)
        # item not found
        if node is None:
            raise ValueError(f"{item} does not exist.")

        parent = self._find_parent_node_recursive(item, self.root)
        # no children
        if node.is_leaf():
            # node is root
            if parent is None:
                self.root.data = None
            # node is on the left
            elif parent.left == node:
                parent.left = None
            # node is on the right
            else:
                parent.right = None
            self.size -= 1
        # node has one child
        elif node.left is None or node.right is None:
            # node is root
            if parent is None:
                if node.left is None:
                    self.root = node.right
                else:
                    self.root = node.left
            elif node.left is None:
                if parent.left == node:
                    parent.left = node.right
                else:
                    parent.right = node.right
            else:
                if parent.left == node:
                    parent.left = node.right
                else:
                    parent.right = node.right
            self.size -= 1
        # node has two children
        else:
            # Starting search at node's right child
            replacement = node.right
            while replacement.left is not None:
                replacement = replacement.left
            replacement_data = replacement.data
            self.delete(replacement_data)
            node.data = replacement_data

    def items_in_order(self):
        """Return an in-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree in-order from root, appending each node's item
            self._traverse_in_order_recursive(self.root, items.append)
        # Return in-order list of all items in tree
        return items

    def _traverse_in_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive in-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        Running time: O(n) because every node is visited once
        TODO: Memory usage: ??? Why and under what conditions?"""
        # print(f"node: {node.data}")
        if node.left is not None:
            # print(f"\ttraverse node.left ({node.left.data})")
            self._traverse_in_order_recursive(node.left, visit)
        # print(f"\titems.append({node.data})")
        visit(node.data)
        if node.right is not None:
            # print(f"\ttraverse node.right ({node.right.data})")
            self._traverse_in_order_recursive(node.right, visit)

    def _traverse_in_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative in-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        Running time: O(n) because every node is visited once
        TODO: Memory usage: ??? Why and under what conditions?"""
        # TODO: Traverse in-order without using recursion (stretch challenge)
        pass

    def items_pre_order(self):
        """Return a pre-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree pre-order from root, appending each node's item
            self._traverse_pre_order_recursive(self.root, items.append)
        # Return pre-order list of all items in tree
        return items

    def _traverse_pre_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive pre-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        Running time: O(n) because every node is visited once
        TODO: Memory usage: ??? Why and under what conditions?"""
        visit(node.data)
        if node.left is not None:
            self._traverse_pre_order_recursive(node.left, visit)
        if node.right is not None:
            self._traverse_pre_order_recursive(node.right, visit)

    def _traverse_pre_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative pre-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        Running time: O(n) because every node is visited once
        TODO: Memory usage: ??? Why and under what conditions?"""
        # TODO: Traverse pre-order without using recursion (stretch challenge)
        pass

    def items_post_order(self):
        """Return a post-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree post-order from root, appending each node's item
            self._traverse_post_order_recursive(self.root, items.append)
        # Return post-order list of all items in tree
        return items

    def _traverse_post_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive post-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        Running time: O(n) because every node is visited once
        TODO: Memory usage: ??? Why and under what conditions?"""
        # TODO: Traverse left subtree, if it exists
        if node.left is not None:
            self._traverse_post_order_recursive(node.left, visit)
        # TODO: Traverse right subtree, if it exists
        if node.right is not None:
            self._traverse_post_order_recursive(node.right, visit)
        # TODO: Visit this node's data with given function
        visit(node.data)


    def _traverse_post_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative post-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        Running time: O(n) because every node is visited once
        TODO: Memory usage: ??? Why and under what conditions?"""
        # TODO: Traverse post-order without using recursion (stretch challenge)
        pass

    def items_level_order(self):
        """Return a level-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree level-order from root, appending each node's item
            self._traverse_level_order_iterative(self.root, items.append)
        # Return level-order list of all items in tree
        return items

    def _traverse_level_order_iterative(self, start_node, visit):
        """Traverse this binary tree with iterative level-order traversal (BFS).
        Start at the given node and visit each node with the given function.
        Running time: O(n) because every node is visited once
        TODO: Memory usage: ??? Why and under what conditions?"""
        queue = LinkedQueue()
        queue.enqueue(start_node)

        while not queue.is_empty():
            node = queue.dequeue()
            visit(node.data)
            if node.left is not None:
                queue.enqueue(node.left)
            if node.right is not None:
                queue.enqueue(node.right)


def test_binary_search_tree():
    # Create a complete binary search tree of 3, 7, or 15 items in level-order
    # items = [2, 1, 3]
    # items = [4, 2, 6, 1, 3, 5, 7]
    items = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
    # delete = [11, 12]
    print('items: {}'.format(items))

    tree = BinarySearchTree()
    print('tree: {}'.format(tree))
    print('root: {}'.format(tree.root))

    print('\nInserting items:')
    for item in items:
        tree.insert(item)
        print('insert({}), size: {}'.format(item, tree.size))
    print('root: {}'.format(tree.root))

    tree.insert(12)
    print(f'insert(12), size: {tree.size}')


    # print(f"\nDeleting Items:")
    # print(f'tree: {tree}')
    # for item in delete:
    #     tree.delete(item)
    #     print(f"delete({item})")
    #     print(f'tree: {tree}')

    print('\nSearching for items:')
    for item in items:
        result = tree.search(item)
        print('search({}): {}'.format(item, result))
    item = 123
    result = tree.search(item)
    print('search({}): {}'.format(item, result))

    print('\nTraversing items:')
    print('items in-order:    {}'.format(tree.items_in_order()))
    print('items pre-order:   {}'.format(tree.items_pre_order()))
    print('items post-order:  {}'.format(tree.items_post_order()))
    print('items level-order: {}'.format(tree.items_level_order()))

    items = [2, 1, 3]
    tree = BinarySearchTree(items)
    tree.delete(2)
    print(tree.root.data is None)
    print(tree.root.left.data)
    print(tree.root.right.data)


if __name__ == '__main__':
    test_binary_search_tree()
