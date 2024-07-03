from src.classes.textnode import TextNode
from src.utils.functions import *
import unittest


class test_functions(unittest.TestCase):
    def test_text_node_to_html_node(self):
        text_node_to_html_node(TextNode())
