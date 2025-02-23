import unittest
from leafnode import LeafNode

def test_anchor():
    a = LeafNode('My Link', 'a', {'src': 'https://google.com'})
    unittest.AssertEqual('<a href=https://google.com> My Link </a.', a.to_html())

def main():
    unittest.main()

if __name__ == '__main__':
    main()
