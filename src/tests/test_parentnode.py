import unittest
from src.classes.parentnode import ParentNode
from src.classes.leafnode import LeafNode


class TestParentNode(unittest.TestCase):

    def test_init(self):
        pass

    def test_to_html(self):
        node1 = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                ParentNode("p", [
                    LeafNode("b", "Bold text"),
                    LeafNode(None, "Normal text"),
                    LeafNode("i", "italic text"),
                    LeafNode(None, "Normal text")]),
                LeafNode(None, "Normal text")
            ],
        )
        node2 = ParentNode("p", [ParentNode("b", [LeafNode("b", "Bold text"), ParentNode('q', []), ParentNode("i",
                                                                                                              []),
                                                  ParentNode("p",
                                                             [LeafNode("b", "Bold text"), LeafNode(None, "Normal text"),
                                                              LeafNode("i", "italic text"),
                                                              LeafNode(None, "Normal text")]), ParentNode('q', []),
                                                  ParentNode("i", []), ParentNode('pad', [])])])

        test1 = "<p><b>Bold text</b>Normal text<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>Normal text</p>"
        test2 = "<p><b><b>Bold text</b><q></q><i></i><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p><q></q><i></i><pad></pad></b></p>"

        self.assertEqual(node1.to_html(), test1)
        self.assertEqual(node2.to_html(), test2)


if __name__ == "__main__":
    unittest.main()
