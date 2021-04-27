"""
This is the mathematical object I will use to chart a Movie

It will be similar to a binary search tree where
the next scene s+1 of scene s will either be the 
left or right child depending on if the scene happened 
in the past or in the future

Then I will have a current_scene pointer that keeps track
of the current seeds location and each new scene 
If the scene comes from the past and reeturns 
"""

"""
I think each Node will have with params

The node has a left and right leaf which go to the next scene
left: the next scene goes to the left leaf is the scene goes back in timne
right: the next scene goes to the right leaf if the scene goes forward in time
parent: the parent node that a node can return to from a flashback
scene_tag: a brief description that describes the scene

"""
import subprocess
from graphviz import Digraph
from rb_tree import RedBlackTree, Node, BLACK, RED, NIL
NIL_LEAF = Node(value=None, color=NIL, parent=None)

class MovieTree:

    s = {}

    def __init__(self, initial_scene, root_id, print_type='preorder'):
        self.root_scene = Scene(initial_scene, None, root_id)
        self.root_id = str(root_id)
        self.current_scene = self.root_scene
        self.s[self.root_id] = self.root_scene
        assert MovieTree.print_types[print_type] is not None
        self.print_function = self.print_types[print_type]
        self.scenes = 1

    def next(self, scene_type, scene_tag=None, scene_id=None):
        if scene_type == 'flashback':
            assert scene_tag is not None
            self.current_scene.add_left(scene_tag, scene_id)
            self.current_scene = self.current_scene.left_scene
            self.s[self.current_scene.scene_id] = self.current_scene
            self.scenes += 1
        elif scene_type == 'forward':
            assert scene_tag is not None
            self.current_scene.add_right(scene_tag, scene_id)
            self.current_scene = self.current_scene.right_scene
            self.s[self.current_scene.scene_id] = self.current_scene
            self.scenes += 1
        elif scene_type == 'return':
            self.current_scene = self.current_scene.parent_scene

        else:
            print(f'type {scene_type} is not a valid next scene type')

    def print(self):
        self.print_function(self, self.root_scene)

    def preorder(self, scene):
        if scene:
            v = scene.scene_id
            l = self.preorder(scene.left_scene)
            r = self.preorder(scene.right_scene)
            return v + ' ' + l + r
        else:
            return ''

    def inorder(self, scene):
        if scene:
            self.inorder(scene.left_scene)
            print(scene.scene_tag)
            self.inorder(scene.right_scene)

    def postorder(self, scene):
        if scene:
            self.postorder(scene.left_scene)
            self.postorder(scene.right_scene)
            print(scene.scene_tag)

    def set_print_function(self, print_f):
        self.print_function = self.print_types[print_f]

    @property
    def size(self):
        return self.scenes

    print_types = {
            'inorder': inorder,
            'preorder': preorder, 
            'postorder': postorder}
            
class Scene:

    def __init__(self, scene_tag, parent_scene, scene_id):
        self.scene_tag = scene_tag
        self.parent_scene = parent_scene
        self.left_scene = None
        self.right_scene = None
        self.scene_id = str(scene_id)

    def add_left(self, scene_tag, scene_id):
        assert self.left_scene is None
        self.left_scene = Scene(scene_tag, self, scene_id)

    def add_right(self, scene_tag, scene_id):
        assert self.right_scene is None
        self.right_scene = Scene(scene_tag, self.parent_scene, scene_id)

    def __str__(self):
        return f'description: {self.scene_tag}'

def add_nodes(dg, node):
    if node != rb_tree.NIL_LEAF:
        add_nodes(dg, node.left)
        dg.node(node.value, mt.s[node.value].scene_tag)
        add_nodes(dg, node.right)

def add_edges(dg, node):
    if node != rb_tree.NIL_LEAF:
        if node.left != rb_tree.NIL_LEAF:
            dg.edge(node.value, node.left.value)
        if node.right != rb_tree.NIL_LEAF:
            dg.edge(node.value, node.right.value)
        add_edges(dg, node.left)
        add_edges(dg, node.right)

def DotTree(t):
    tree = Digraph()
    add_nodes(tree, t.root)
    add_edges(tree, t.root)
    return tree


if __name__ == '__main__':

    mt = MovieTree('Rocket gets caught between Lil Z and police', 50) # 50
    mt.next('flashback', 'The Sixties', 20)  # 20
    mt.next('forward', 'The Story of the Tender Trio', 21) # 21 
    mt.next('forward', 'Lil Dice and the tender trio rob the love motel', 22) #22
    mt.next('forward', 'The tender trio escape the love motel without Lil Dice', 23) #23
    mt.next('forward', 'Man kills his wife for adultry and Goose gets raided by the cops', 24) # 24
    mt.next('forward', 'Shaggy dies trying to hijack a car', 25) # 25
    mt.next('forward', 'The Seventies', 26) # 26
    mt.next('forward', 'Rocket tries to buy weed for Martha', 28) # 28 
    mt.next('flashback', 'The story of the apartment', 27) # 27
    mt.next('return')
    mt.next('forward', 'Lil Z shoots the apartment dealer', 33) # 33
    mt.next('flashback', 'The story of Lil Z', 30) # 30 
    mt.next('forward', 'Lil Dice kills Rocket\'s brother', 31) # 31 
    mt.next('forward', 'Lil Z gains amulet and becomes big crime boss', 32) # 32
    mt.next('return')
    mt.next('forward', 'Lil Z starts selling drugs', 34) # 34 
    mt.next('forward', 'Benny meets Tiago and becomes a playboy', 35) # 35
    mt.next('forward', 'Lil Z and Carrot and Lil Z vs the Runts', 36) # 36
    mt.next('forward', 'A sucker\'s life', 37) #37
    mt.next('forward', 'Flirting with crime', 38) #38
    mt.next('forward', 'Rocket fails at robbing the waitress and the man from Sao Paolo', 39) #39
    mt.next('forward', '"You need a girlfriend Lil Z"', 40) #40
    mt.next('forward', 'Benny\'s farewell', 41) #41
    mt.next('forward', 'Knockout Ned and Lil Z\'s inciting incident', 42) #42
    mt.next('forward', 'The story of Knockout Ned', 43) #43
    mt.next('forward', 'War breaks out: Lil Z vs Carrot and Ned', 44) #44
    mt.next('forward', 'Rocket takes photos of Lil Z\'s gang', 45 ) #45 
    mt.next('forward', 'Rocket starts living with professional prohotographer', 46) #46
    mt.next('forward', 'Lil Z gives the Runts guns', 47) #47
    mt.next('forward', 'The Beginning of the End', 48) #48
    mt.next('return')
    mt.next('forward', 'The final war begins and Rocket takes photos', 51) # 51 
    mt.next('forward', 'Knockout Ned is killed by Otto', 54) # 54
    mt.next('flashback', 'The Story of Otto', 52) # 52
    mt.next('return')
    mt.next('forward', 'Lil Z is arrested, Rocket takes photos', 55) # 55
    mt.next('forward', 'Lil Z is killed by the Runts, Rocket takes photos', 56) # 56
    mt.next('forward', 'Rocket gets an internship for his photogrpahy', 57) #57
    s = mt.preorder(mt.root_scene)
    s = s.split()
    """
    print(f"no. of scenes: {mt.size}")
    print("\nPreorder(Original) story\n")
    mt.print()
    mt.set_print_function('inorder')
    print("\nInorder story\n")
    mt.print()
    mt.set_print_function('postorder')
    print("\nPostorder story\n")
    mt.print()
    dot = DotTree(mt)
    """
    rb_tree = RedBlackTree()
    for item in s:
        rb_tree.add(item)
    rb_dot = DotTree(rb_tree)

    #print(rb_dot.source)
    subprocess.call(["/usr/local/bin/dot","-Tpng","MovieTree.dot","-o","rbgraph.png"])
    

