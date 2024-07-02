import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        node3 = TextNode("This is a text node", "bold", "www.google.com")
        self.assertEqual(node == node2, True)
        self.assertNotEqual(node2, node3)

    def test_repr(self):
        node = TextNode("This is test", "italic")
        expected = "TextNode(This is test, italic, None)"
        expected2 = "TextNode(This is test, italic)"
        self.assertEqual(str(node), expected)
        self.assertNotEqual(str(node), expected2)


if __name__ == "__main__":
    unittest.main()
