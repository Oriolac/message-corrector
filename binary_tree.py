#!/usr/bin/env python3


""" Classe Binary Tree"""
class BinaryTree:

    class Node:
        def __init__(self, value, left, right):
            """ Inicialització """
            self.value = value
            self.left = left
            self.right = right

    def __init__(self, root):
        """ Inicialització """
        self.root = root

    def is_empty(self):
        """ Mirar si està buida """
        return self.root is None
    
    def get_code(self, value):
        return self.get_code_with_node(value, self.root, '')

    def get_code_with_node(self, value, node, string):
        if node is None:
            return string
        elif value == node.value:
            return string
        elif value > node.value:
            return self.get_code_with_node(value, node.right, string + '1')
        else:
            return self.get_code_with_node(value, node.left, string + '0')
    
    def put(self, value):
        if value is None:
            return self
        new_root = self.new_node_of_the_branch(value, self.root)
        return BinaryTree(new_root)
    
    def new_node_of_the_branch(self, value, node):
        if node is None:
            return self.Node(value, None, None)
        elif value == node.value:
            return self.Node(value, node.left, node.right)
        elif value > node.value:
            return self.Node(value, self.new_node_of_the_branch(value, node.left), node.right)
        else:
            return self.Node(value, node.left, self.new_node_of_the_branch(value, node.right))

    def to_string(self):
        string = ''
        line = [self.root.value]
        while line is []