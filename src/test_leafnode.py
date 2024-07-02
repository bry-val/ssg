import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):

    def test_init(self):
        # LeafNode should not accept 4 args
        with self.assertRaises(TypeError):
            LeafNode('a', 'b', 'c', 'd')

        # LeafNode.value cannot be empty
        with self.assertRaises(AssertionError):
            LeafNode(tag=None, value=None, props=None)

    def test_to_html(self):
        node1 = LeafNode("p", "This is a paragraph of text.")
        node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        node3 = LeafNode("p", "This is nothing",
                         {"href": "https://www.google.com", "target": "_blank"})

        self.assertEqual(node1.to_html(), '<p>This is a paragraph of text.</p>')
        self.assertEqual(node2.to_html(), '<a href="https://www.google.com">Click me!</a>')
        self.assertEqual(node3.to_html(), '<p href="https://www.google.com" target="_blank">This is nothing</p>')


if __name__ == "__main__":
    unittest.main()
