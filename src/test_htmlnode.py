from htmlnode import HTMLNode
import unittest

class TestHTMLNode(unittest.TestCase):
    def test_init(self):
        node = HTMLNode("div", "This is a div")
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "This is a div")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_init2(self):
        node = HTMLNode("div", "This is a div", props={"class": "my-class"})
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "This is a div")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, {"class": "my-class"})

    def test_init3(self):
        node = HTMLNode("div", "This is a div", children=[HTMLNode("span", "This is a span")])
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "This is a div")
        self.assertEqual(node.children[0].tag, "span")
        self.assertEqual(node.children[0].value, "This is a span")
        self.assertEqual(node.children[0].children, None)
        self.assertEqual(node.children[0].props, None)

    def test_props_to_html(self):
        node = HTMLNode("div", "This is a div", props={"class": "my-class"})
        self.assertEqual(node.props_to_html(), " class=\"my-class\"")

    def test_props_to_html2(self):
        node = HTMLNode("p", "This is a paragraph", props={"class": "my-class", "id": "my-id"})
        self.assertEqual(node.props_to_html(), " class=\"my-class\" id=\"my-id\"")

if __name__ == "__main__":
    unittest.main()

