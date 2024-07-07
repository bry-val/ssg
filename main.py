from src.classes.textnode import TextNode
from src.utils.node_functions import *


def main():
    # you dumbass. TextNode just takes a link. The function is
    # the one responsible for converting it into a dictionary.
    # you overcomplicated it. your code was working lmfao

    textnode1 = TextNode("Bold text!", "bold")
    textnode2 = TextNode("Plain text node!", "text")
    textnode3 = TextNode("Italics node!", "italic")
    textnode4 = TextNode("Code block?", "code")
    textnode5 = TextNode("Google.com", "link", 'https://www.google.com')
    textnode6 = TextNode("Facebook.com", "link", "https://www.facebook.com")
    textnode7 = TextNode("This is an apple", "image", "./img/apples.png")
    textnode8 = TextNode('this is an pear', "image", './img/pear.png')

    t_html_1 = text_node_to_html_node(textnode1)
    t_html_2 = text_node_to_html_node(textnode2)
    t_html_3 = text_node_to_html_node(textnode3)
    t_html_4 = text_node_to_html_node(textnode4)
    t_html_5 = text_node_to_html_node(textnode5)
    t_html_6 = text_node_to_html_node(textnode6)
    t_html_7 = text_node_to_html_node(textnode7)
    t_html_8 = text_node_to_html_node(textnode8)

    print(t_html_1.to_html())
    print(t_html_2.to_html())
    print(t_html_3.to_html())
    print(t_html_4.to_html())
    print(t_html_5.to_html())
    print(t_html_6.to_html())
    print(t_html_7.to_html())
    print(t_html_8.to_html())


if __name__ == "__main__":
    main()
