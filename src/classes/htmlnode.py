class HTMLNode:

    # tag - A string representing the HTML tag name (e.g. "p", "a", "h1", etc.)
    # value - A string representing the value of the HTML tag (e.g. the text inside a paragraph)
    # children - A list of HTMLNode objects representing the children of this node
    # props - A dictionary of key-value pairs representing the attributes of the HTML tag.
    # For example, a link (<a> tag) might have {"href": "https://www.google.com"}

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        return f"Tag: {self.tag}\nValue: {self.value}\nChildren: {self.children}\nProperties: {self.props}"

    def to_html(self):
        raise NotImplementedError("Not implemented")

    def props_to_html(self):
        string = ""
        for key, val in self.props.items():
            string += f"{key}=\"{val}\" "
        return string.rstrip()
