import unittest
from src.classes.htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):

    def test_repr(self):
        node = HTMLNode("p", "This is nothing", "content machine",
                        {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(str(node),
                         f"Tag: p\nValue: This is nothing\nChildren: content machine\nProperties: "
                         + "{'href': 'https://www.google.com', 'target': '_blank'}")

    def test_props_to_html(self):
        node = HTMLNode("p", "This is a paragraph", None, {"href": "https://www.google.com", "target": "_blank"})
        node1 = HTMLNode("p", "This is a paragraph", None,
                         {"href": "localhost:8080/index.html", "target": "_header", "src": "styles.css"})
        self.assertEqual(node.props_to_html(), 'href="https://www.google.com" target="_blank"')
        self.assertEqual(node1.props_to_html(), 'href="localhost:8080/index.html" target="_header" src="styles.css"')


if __name__ == "__main__":
    unittest.main()
