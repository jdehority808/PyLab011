import os

class MindMapComposite(object):

    def __init__(self, name, shape):
        self.name = name
        self.shape = shape
        self.children = []

    def add(self, child):
        self.children.append(child)

    def remove(self, child):
        self.children.remove(child)

    @staticmethod
    def get_shape_representation(shape:str):
        shape_d = {
            "circle": "((({)))",
            "oval": "({})",
            "square": "[{}]",
            "cloud": "){}(",
            "hexagon": "{{{{{}}}}}",
            "bang": ")){}(("
        }
        return shape_d.get(shape)

    def display(self, indent=0):
        print(" " * indent + str(self))
        for child in self.children:
            child.display(indent + 2)

    def __str__(self):
        shape_representation = (
            MindMapComposite.get_shape_representation(self.shape))
        return shape_representation.format(self.name)