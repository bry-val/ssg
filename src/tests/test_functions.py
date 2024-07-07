from src.classes.textnode import TextNode
from src.utils.node_functions import *
import unittest


# [TextNode(This is **text** with an *italic* word and a `code block` and an , text, None), TextNode(image, image, https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png), TextNode( and a , text, None), TextNode(link, link, https://boot.dev)]


# link_node1 = TextNode(
#     "1. This is text with an ![link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
#     TEXT_TYPE_TEXT,
# )
#
# link_node2 = TextNode(
#     "2. This is text with an ![third link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![fourth link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
#     TEXT_TYPE_TEXT,
# )
#
# link_node3 = TextNode(
#     "3. This is text with an ![fifth link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![sixth link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
#     TEXT_TYPE_TEXT,
# )
#
# image_node = TextNode(
#     "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) "
#     "and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
#     TEXT_TYPE_TEXT,
# )

class test_functions(unittest.TestCase):
    def test_text_node_to_html_node(self):
        text_node_to_html_node(TextNode())

    def test_split_nodes_delimiter(self):
        pass

    def test_text_to_text_node(self):
        # markdown = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"
        # print(text_to_textnodes(markdown) == [
        #     TextNode("This is ", TEXT_TYPE_TEXT),
        #     TextNode("text", TEXT_TYPE_BOLD),
        #     TextNode(" with an ", TEXT_TYPE_TEXT),
        #     TextNode("italic", TEXT_TYPE_ITALIC),
        #     TextNode(" word and a ", TEXT_TYPE_TEXT),
        #     TextNode("code block", TEXT_TYPE_CODE),
        #     TextNode(" and an ", TEXT_TYPE_TEXT),
        #     TextNode("image", TEXT_TYPE_IMAGE,
        #              "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
        #     TextNode(" and a ", TEXT_TYPE_TEXT),
        #     TextNode("link", TEXT_TYPE_LINK, "https://boot.dev"),
        # ])
        pass

    def markdown_to_blocks(self):
        pass
