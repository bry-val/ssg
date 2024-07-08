from node_functions import *
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


def check_unordered_list(lines):
    for line in lines:
        if not (line.startswith("*") or line.startswith("-")):
            return False
    return True


def check_ordered_list(lines):
    counter = 1
    for line in lines:
        if not line.startswith("{counter}. "):
            return False
        counter += 1
    return True


def paragraph_to_html(block):
    return LeafNode(tag="p", value=block).to_html()


def heading_to_html(block):
    node = LeafNode(value="")
    if block.startswith("######"):
        node = LeafNode(tag="h6", value=block[6:])
    elif block.startswith("#####"):
        node = LeafNode(tag="h5", value=block[5:])
    elif block.startswith("####"):
        node = LeafNode(tag="h4", value=block[4:])
    elif block.startswith("###"):
        node = LeafNode(tag="h3", value=block[3:])
    elif block.startswith("##"):
        node = LeafNode(tag="h2", value=block[2:])
    elif block.startswith("#"):
        node = LeafNode(tag="h1", value=block[1:])
    return node.to_html()


def code_to_html(block):
    children = [LeafNode(tag="code", value=block[3:-3])]
    return ParentNode(tag="pre", children=children).to_html()


def quote_to_html(block):
    lines = block.splitlines()
    children = []
    for line in lines:
        children.append(LeafNode(tag="p", value=line[1:]))
    return ParentNode(tag="blockquote", children=children).to_html()


def ul_to_html(block):
    lines = block.splitlines()
    children = []
    for line in lines:
        children.append(LeafNode(tag="li", value=line))
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
    elif check_ordered_list(lines):
        return BLOCK_TYPE_ORDERED_LIST
    elif check_unordered_list(lines):
        return BLOCK_TYPE_UNORDERED_LIST
    else:
        return BLOCK_TYPE_PARAGRAPH


md = """ This is **bolded** paragraph

>This is another paragraph with *italic* text and `code` here
>This is the same paragraph on a new line

* This is a list
* with items

1. This is another paragraph with *italic* text and `code` here
2. This is the same paragraph on a new line

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

```
for i in range(3):
    print(i)
```

###This is the same paragraph on a new line

"""

ul_block = markdown_to_blocks(md)[2]
quote_block = markdown_to_blocks(md)[1]
ol_block = markdown_to_blocks(md)[3]
p_block = markdown_to_blocks(md)[4]
code_block = markdown_to_blocks(md)[5]
heading_block = markdown_to_blocks(md)[6]


# TODO: Inline block parsing of markdown.
def block_to_html(block, block_type):
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


# print(block_to_html(ul_block, BLOCK_TYPE_UNORDERED_LIST))
# print(block_to_html(quote_block, BLOCK_TYPE_QUOTE))
print(block_to_html(ol_block, BLOCK_TYPE_ORDERED_LIST))
# print(block_to_html(p_block, BLOCK_TYPE_PARAGRAPH))
# print(block_to_html(code_block, BLOCK_TYPE_CODE))
# print(block_to_html(heading_block, BLOCK_TYPE_HEADING))
