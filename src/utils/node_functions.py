from src.classes.leafnode import LeafNode
from src.classes.textnode import TextNode
import re

# CONSTANTS
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
