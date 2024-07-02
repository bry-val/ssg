from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props):
        super().__init__(tag, value, props)

    def to_html(self):
        if self.value is None:
            raise ValueError
        if self.tag is None:
            return self.value
        return self.string_builder()

    def string_builder(self):
        if self.props is None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"
