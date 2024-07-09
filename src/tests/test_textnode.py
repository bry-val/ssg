import \
    unittest  # md_block = """- **Diverse Cultures and Languages**: Each race, from the noble Elves to the sturdy Dwarves, is endowed with its own
#   rich history, customs, and language. Tolkien, leveraging his expertise in philology, constructed languages such as
#   Quenya and Sindarin, each with its own grammar and lexicon.
# - **Geographical Realism**: The landscape of Middle-earth, from the Shire's pastoral hills to the shadowy depths of
#   Mordor, is depicted with such vividness that it feels as tangible as our own world.
# - **Historical Depth**: The legendarium is imbued with a sense of history, with ruins, artifacts, and lore that hint at
#   bygone eras, giving the world a lived-in, authentic feel."""
#
# md_ul_block = """- The resilience of the human (and hobbit) spirit in the face of overwhelming odds
# - The corrupting influence of power, epitomized by the One Ring
# - The importance of friendship, loyalty, and sacrifice"""
#
# not_ul = """These universal themes lend the series a profound philosophical depth, making it a beacon of wisdom and insight for
# generations of readers."""
#
# print("nested bold in UL:", ul_to_html(md_block))
# print("known ulblock:", ul_to_html(md_ul_block))
# print("not ulblock:", block_to_block_type(not_ul))
from src.classes.textnode import TextNode


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
