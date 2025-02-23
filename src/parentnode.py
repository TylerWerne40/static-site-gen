from htmlnode import HTMLNode
from enum import Enum

class ParentTags(Enum):
    PARA = 'p'
    H1   = 'h1'
    H2   = 'h2'
    H3   = 'h3'
    H4   = 'h4'
    H5   = 'h5'
    BODY = 'body'
    CODE = 'code'
    ART  = 'article'
    HEAD = 'head'


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        self.super()

    def to_html(self):
        if self.tag is None:
            raise ValueError('no tag')
        if self.children is None:
            raise ValueError('no children')
        match self.tag:
            case _:
                ret_str = f'<{self.tag}>'
                for i in children:
                    ret_str += i.to_html()
                ret_str += f'</{self.tag}>'
                return ret_str
