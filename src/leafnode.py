from htmlnode import HTMLNode
from enum import Enum

class tags(Enum):
    PARA = 'p'
    BOLD = 'b'
    ANCH = 'a'
    ITAL = 'i'
    HD1  = 'h1'
    HD2  = 'h2'
    HD3  = 'h3'
    HD4  = 'h4'
    HD5  = 'h5'
    IMG  = 'img'

class LeafNode(HTMLNode):


    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    def to_html(self):
        if self.value is None:
            raise ValueError('value is None')
        if self.tag is None:
            return str(self.value)
        match self.tag:
            case tags.ANCH:
                return f'<{self.tag} href={self.props['src']}>' + self.value + fr'</{self.tag}>'
            case tags.IMG:
                ret_str = f'<{self.tag}'
                if 'class' in self.props.keys():
                    ret_str += ' class=' + self.props['class']
                if 'src' in self.props.keys():
                    ret_str += ' src=' + self.props['src']
                else:
                    raise ValueError('image tag must have src in props dict')
                if 'alt' in self.props.keys():
                    ret_str += ' alt=' + self.props['alt']
                ret_str += ' />'
                return ret_str
                
            case _:
                return f'<{self.tag}>' + self.value + fr'</{self.tag}>'
