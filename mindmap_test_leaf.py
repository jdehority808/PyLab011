from mindmap_leaf import MindMapLeaf
from mindmap_composite import MindMapComposite

if __name__ == '__main__':
    mindmap = MindMapComposite("mindmap", "circle")
    tools = MindMapComposite("Tools", "bang")
    tools.add(MindMapLeaf("Pen and paper", "rectangle"))
    tools.add(MindMapLeaf("mermaid", "rectangle"))
    mindmap.add(tools)
    origins = MindMapComposite("Origins", "square")
    origins.add(MindMapLeaf("Long history", "rectangle"))
    popularisation = MindMapComposite("Popularisation", "rectangle")
    popularisation.add(MindMapLeaf("British popular psychology author Tony Buzan", "rectangle"))

    origins.add(popularisation)
    mindmap.add(origins)

    mindmap.display()