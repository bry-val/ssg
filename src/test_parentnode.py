import unittest

from parentnode import ParentNode


class TestParentNode(unittest.TestCase):

    def test_init(self):
        pass

    def test_to_html(self):
        pass
    # --- TODO --
    # implement Test for below cases
    # node1 = ParentNode(
    #     "p",
    #     [
    #         LeafNode("b", "Bold text"),
    #         LeafNode(None, "Normal text"),
    #         ParentNode("p", [
    #             LeafNode("b", "Bold text"),
    #             LeafNode(None, "Normal text"),
    #             LeafNode("i", "italic text"),
    #             LeafNode(None, "Normal text")]),
    #         LeafNode(None, "Normal text")
    #     ],
    # )
    # # <p><b>Bold text</b>Normal text<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>Normal text</p>
    #
    # node = ParentNode( "p", [ ParentNode("b", [ LeafNode("b", "Bold text"), ParentNode('q', []), ParentNode("i",
    # []), ParentNode("p", [ LeafNode("b", "Bold text"), LeafNode(None, "Normal text"), LeafNode("i", "italic text"),
    # LeafNode(None, "Normal text")]), ParentNode('q', []), ParentNode("i", []), ParentNode('pad', [])])]) #
    # <p><b><b>Bold text</b><q></q><i></i><p><b>Bold text</b>Normal text<i>italic text</i>Normal
    # text</p><q></q><i></i><pad></pad></b></p>


if __name__ == "__main__":
    unittest.main()
