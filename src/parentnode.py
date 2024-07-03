from htmlnode import HTMLNode
from leafnode import LeafNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Tag cannot be none")
        if self.children is None:
            raise ValueError("Children cannot be none")

        inner = ""

        for leaf in self.children:
            if isinstance(leaf, ParentNode):
                leaf.to_html()
            inner += leaf.to_html()

        return f"<{self.tag}>{inner}</{self.tag}>"
