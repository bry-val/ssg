from src.classes.leafnode import LeafNode
from src.classes.textnode import TextNode
import re

TEXT_TYPE_TEXT, TEXT_TYPE_BOLD, TEXT_TYPE_ITALIC, TEXT_TYPE_CODE, TEXT_TYPE_LINK, TEXT_TYPE_IMAGE = "text", "bold", "italic", "code", "link", "image"


def text_node_to_html_node(text_node):
    match text_node.text_type.lower():
        case ('text'):
            return LeafNode(value=text_node.text)
        case ('bold'):
            return LeafNode(tag="b", value=text_node.text)
        case ('italic'):
            return LeafNode(tag="i", value=text_node.text)
        case ('code'):
            return LeafNode(tag="code", value=text_node.text)
        case ('link'):
            return LeafNode(tag="a", value=text_node.text, props={'href': text_node.url})
        case ('image'):
            return LeafNode(tag="img", value='', props={'src': text_node.url, 'alt': text_node.text})
        case _:
            raise ValueError("Text type is invalid")


# [TextNode(This is **text** with an *italic* word and a `code block` and an , text, None), TextNode(image, image, https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png), TextNode( and a , text, None), TextNode(link, link, https://boot.dev)]

def split_nodes_delimiter(old_nodes: list, delimiter: str, text_type: str) -> list:
    if not isinstance(old_nodes, list):
        assert TypeError("Old_nodes should be a list")
    new_nodes = []
    for oldnode in old_nodes:
        if oldnode.text_type != TEXT_TYPE_TEXT:
            new_nodes.append(oldnode)
            continue
        words = oldnode.text.split(delimiter)
        for i in range(len(words)):
            if i % 2 == 0:
                new_nodes.append(TextNode(words[i], TEXT_TYPE_TEXT))
            else:
                new_nodes.append(TextNode(words[i], text_type))
    return new_nodes


def extract_markdown_images(text):
    pattern = r"!\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern, text)
    return matches


def extract_markdown_links(text):
    pattern = r"\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern, text)
    return matches


link_node1 = TextNode(
    "1. This is text with an ![link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
    TEXT_TYPE_TEXT,
)

link_node2 = TextNode(
    "2. This is text with an ![third link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![fourth link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
    TEXT_TYPE_TEXT,
)

link_node3 = TextNode(
    "3. This is text with an ![fifth link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![sixth link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
    TEXT_TYPE_TEXT,
)

image_node = TextNode(
    "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) "
    "and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
    TEXT_TYPE_TEXT,
)


def split_nodes_image(old_nodes):
    new_nodes = []
    for oldnode in old_nodes:
        if oldnode.text_type != TEXT_TYPE_TEXT:
            new_nodes.append(oldnode)
            continue
        images = extract_markdown_images(oldnode.text)
        if not images:
            new_nodes.append(oldnode)
        original_text = oldnode.text
        for image in images:
            lister = original_text.split(f"![{image[0]}]({image[1]})", 1)
            new_nodes.append(TextNode(lister[0], TEXT_TYPE_TEXT))
            new_nodes.append(TextNode(image[0], TEXT_TYPE_IMAGE, image[1]))
            original_text = lister[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TEXT_TYPE_TEXT))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for oldnode in old_nodes:
        if oldnode.text_type != TEXT_TYPE_TEXT:
            new_nodes.append(oldnode)
            continue
        links = extract_markdown_links(oldnode.text)
        if len(links) == 0:
            new_nodes.append(oldnode)
            continue
        original_text = oldnode.text
        for link in links:
            lister = original_text.split(f'[{link[0]}]({link[1]})')
            new_nodes.append(TextNode(lister[0], TEXT_TYPE_TEXT))
            new_nodes.append(TextNode(link[0], TEXT_TYPE_LINK, link[1]))
            original_text = lister[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TEXT_TYPE_TEXT))
    return new_nodes


def text_to_textnodes(text):
    node = TextNode(text, TEXT_TYPE_TEXT)
    image_split = split_nodes_image([node])
    link_split = split_nodes_link(image_split)
    code_split = split_nodes_delimiter(link_split, '`', TEXT_TYPE_CODE)
    bold_split = split_nodes_delimiter(code_split, '**', TEXT_TYPE_BOLD)
    italic_split = split_nodes_delimiter(bold_split, '*', TEXT_TYPE_ITALIC)
    return italic_split


markdown = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"
print(text_to_textnodes(markdown) == [
    TextNode("This is ", TEXT_TYPE_TEXT),
    TextNode("text", TEXT_TYPE_BOLD),
    TextNode(" with an ", TEXT_TYPE_TEXT),
    TextNode("italic", TEXT_TYPE_ITALIC),
    TextNode(" word and a ", TEXT_TYPE_TEXT),
    TextNode("code block", TEXT_TYPE_CODE),
    TextNode(" and an ", TEXT_TYPE_TEXT),
    TextNode("image", TEXT_TYPE_IMAGE,
             "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
    TextNode(" and a ", TEXT_TYPE_TEXT),
    TextNode("link", TEXT_TYPE_LINK, "https://boot.dev"),
])
