from src.utils.node_functions import *
from src.classes.leafnode import LeafNode
from src.classes.parentnode import ParentNode

# CONSTANTS
BLOCK_TYPE_PARAGRAPH, BLOCK_TYPE_HEADING, BLOCK_TYPE_CODE, BLOCK_TYPE_QUOTE, BLOCK_TYPE_UNORDERED_LIST, BLOCK_TYPE_ORDERED_LIST = "paragraph", "heading", "code", "quote", "unordered_list", "ordered_list"


# HELPER FUNCTIONS
def check_quote(lines):
    for line in lines:
        if not line.startswith(">"):
            return False
    return True


def check_heading_type(block):
    if block.startswith("######"):
        return "h6", block[7:]
    elif block.startswith("#####"):
        return "h5", block[6:]
    elif block.startswith("####"):
        return "h4", block[5:]
    elif block.startswith("###"):
        return "h3", block[4:]
    elif block.startswith("##"):
        return "h2", block[3:]
    elif block.startswith("#"):
        return "h1", block[2:]
    else:
        raise ValueError("Not valid heading")


def check_ordered_list(block):
    counter = 1
    for line in block.splitlines():
        if not line.startswith(f"{counter}. "):
            return False
        counter += 1
    return True


def check_unordered_list(block):
    for line in block.splitlines():
        if line[0] == " ":
            continue
        # print(line)
        if not (line[0] == "-" or line[0] == "*"):
            return False
    return True


def paragraph_to_html(block):
    lines = block.splitlines()
    html_nodes = [
        "".join(
            text_node_to_html_node(node).to_html()
            for node in text_to_textnodes(line)
        )
        for line in lines
    ]

    return LeafNode(tag="p", value="\n".join(html_nodes)).to_html()


def heading_to_html(block):
    lines = block.splitlines()
    html_nodes = [
        "".join(
            text_node_to_html_node(node).to_html()
            for node in text_to_textnodes(line)
        )
        for line in lines
    ]
    tag, value = check_heading_type("".join(html_nodes))
    return LeafNode(tag=tag, value=value).to_html()


def code_to_html(block):
    children = [LeafNode(tag="code", value=block[4:-3])]
    return ParentNode(tag="pre", children=children).to_html()


def quote_to_html(block):
    words = []
    for line in block.split(">"):
        if line != "":
            words.append(line.strip())
    p_val = " ".join(words)
    children = [LeafNode(tag="p", value=p_val)]
    return ParentNode(tag="blockquote", children=children).to_html()


def ul_to_html(block):
    lines = block.split(f"{block[0]} ")
    html_nodes = [
        "".join(
            text_node_to_html_node(node).to_html()
            for node in text_to_textnodes(line)
        )
        for line in lines[1:]
    ]
    children = [
        LeafNode(tag="li", value=html) for html in html_nodes
    ]
    return ParentNode(tag="ul", children=children).to_html()


def ol_to_html(block):
    lines = block.splitlines()
    html_nodes = [
        "".join(
            text_node_to_html_node(node).to_html()
            for node in text_to_textnodes(line[3:])
        )
        for line in lines
    ]
    children = [
        LeafNode(tag="li", value=html) for html in html_nodes
    ]
    return ParentNode(tag="ol", children=children).to_html()


# BIG BOY FUNCTIONS
def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks


def block_to_block_type(block):
    lines = block.splitlines()
    first_line = lines[0]
    last_line = lines[-1]
    if first_line.startswith('#'):
        return BLOCK_TYPE_HEADING
    elif first_line.startswith("```") and last_line.endswith("```"):
        return BLOCK_TYPE_CODE
    elif check_quote(lines):
        return BLOCK_TYPE_QUOTE
    elif check_ordered_list(block):
        return BLOCK_TYPE_ORDERED_LIST
    elif check_unordered_list(block):
        return BLOCK_TYPE_UNORDERED_LIST
    else:
        return BLOCK_TYPE_PARAGRAPH


def block_to_html(block):
    block_type = block_to_block_type(block)
    if block_type == BLOCK_TYPE_UNORDERED_LIST:
        return ul_to_html(block)
    elif block_type == BLOCK_TYPE_QUOTE:
        return quote_to_html(block)
    elif block_type == BLOCK_TYPE_ORDERED_LIST:
        return ol_to_html(block)
    elif block_type == BLOCK_TYPE_PARAGRAPH:
        return paragraph_to_html(block)
    elif block_type == BLOCK_TYPE_CODE:
        return code_to_html(block)
    elif block_type == BLOCK_TYPE_HEADING:
        return heading_to_html(block)
