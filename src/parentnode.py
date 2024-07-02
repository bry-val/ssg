from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props):
        super().__init__(tag=tag, children=children, props=props)
