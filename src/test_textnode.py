import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_TT(self):
        node = TextNode('hi', TextType.BOLD)
        node2 = TextNode('none', 'bold', 'aklsdfjh')
        self.assertNotEqual(node.text_type, node2.text_type)
    def test_url_none(self):
        node = TextNode('hi', TextType.BOLD)
        node2 = TextNode('none', 'bold', 'aklsdfjh')
        self.assertEqual(node.url, None)
    def test_text(self):
        node = TextNode('test', TextType.BOLD)
        self.assertEqual(node.text, 'test')

if __name__ == "__main__":
    unittest.main()
