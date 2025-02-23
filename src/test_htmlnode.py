import unittest
from htmlnode import HTMLNode

def test_HTMLNode():
    a = HTMLnode(tag= 'a')
    unittest.AssertEqual(a.tag, 'a')

def test_HTMLNodeREPR():
    b = HTMLNode('a', 'b', 'c', 'd')
    test_string = 'HTMLNode {\na\nb\nc\nd}'
    unittest.AssertEqual(repr(b), test_string)

def test_HTMLNodetag():
    c = HTMLNode('a', 'b', 'c', 'd')
    unittest.AssertEqual('c', c.children)



def main():
    unittest.main()

if '__main__' == __name__:
    main()
