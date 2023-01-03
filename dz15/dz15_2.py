import pytest
from dz14 import Tree

my_tree = Tree(5)

def test_check_node_True():
    assert my_tree.check_node(5) == True

def test_check_node_False():
    assert my_tree.check_node(4) == False

def test_add_list_True():
    my_tree.add_list([1, 2, 10, 11])
    assert my_tree.check_node(1) and my_tree.check_node(2) and my_tree.check_node(10) and my_tree.check_node(11) == True

def test_add_list_False():
    my_tree.add_list([1, 2, 10, 11])
    assert my_tree.check_node(1) and my_tree.check_node(2) and my_tree.check_node(10) and my_tree.check_node(12) == False

def test_min_node_True():
    assert my_tree.min_node() == 1

def test_min_node_False():
    assert my_tree.min_node() != 2

def test_max_node_True():
    assert my_tree.max_node() == 11

def test_max_node_False():
    assert my_tree.max_node() != 10

def test_del_node():
    my_tree.del_node(10)
    assert my_tree.check_node(10) == False
