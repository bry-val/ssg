from src.classes.htmlnode import HTMLNode


class LeafNode(HTMLNode):
    # props is optional
    # value is required
    def __init__(self, tag=None, value=None, props=None):
        assert value is not None, "Value is required"
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError
        if self.tag is None:
            return self.value
        return self.string_builder()

    def string_builder(self):
        if self.props is None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        if self.tag == "img":
            return f"<{self.tag} {self.props_to_html()}>{self.value}"
        return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"
