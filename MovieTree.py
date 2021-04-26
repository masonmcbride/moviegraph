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
import pickle 
import subprocess

class MovieTree:

    def __init__(self, initial_scene, print_type='preorder'):
        self.root_scene = Scene(initial_scene, None)
        self.current_scene = self.root_scene
        assert MovieTree.print_types[print_type] is not None
        self.print_function = self.print_types[print_type]

    def next(self, scene_type, scene_tag=None):
        if scene_type == 'flashback':
            assert scene_tag is not None
            self.current_scene.add_left(scene_tag)
            self.current_scene = self.current_scene.left_scene
        elif scene_type == 'forward':
            assert scene_tag is not None
            self.current_scene.add_right(scene_tag)
            self.current_scene = self.current_scene.right_scene
        elif scene_type == 'return':
            self.current_scene = self.current_scene.parent_scene
        else:
            print(f'type {scene_type} is not a valid next scene type')

    def print(self):
        self.print_function(self, self.root_scene)

    def preorder(self, scene):
        if scene:
            print(scene.scene_tag)
            self.preorder(scene.left_scene)
            self.preorder(scene.right_scene)

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


    print_types = {
            'inorder': inorder,
            'preorder': preorder, 
            'postorder': postorder
    }
            
class Scene:

    def __init__(self, scene_tag, parent_scene):
        self.scene_tag = scene_tag
        self.parent_scene = parent_scene
        self.left_scene = None
        self.right_scene = None

    def add_left(self, scene_tag):
        assert self.left_scene is None
        self.left_scene = Scene(scene_tag, self)

    def add_right(self, scene_tag):
        assert self.right_scene is None
        self.right_scene = Scene(scene_tag, self.parent_scene)

    def __str__(self):
        return f'description: {self.scene_tag}'

if __name__ == '__main__':

    mt = MovieTree('Rocket gets caught between Lil Z and police')
    mt.next('flashback', 'The Sixties')
    mt.next('forward', 'The story of the tender trio')
    mt.next('forward', 'Rocket is swimming at the lake')
    mt.next('forward', 'Lil Dice and the tender trio rob the love motel')
    mt.next('forward', 'The tender trio escape the move motel without Lil Dice')
    mt.next('forward', 'Shaggy meets Bernice and Clipper becomes Christian')
    mt.next('forward', 'Man kills his wife for adultry and Goose gets raided by the cops')
    mt.next('forward', 'Shaggy dies trying to hijack a car')
    mt.next('forward', 'The Seventies')
    mt.next('forward', 'Rocket tries to buy weed for Martha')
    mt.next('flashback', 'The story of the apartment')
    mt.next('return')
    mt.next('forward', 'Lil Z shoots the apartment dealer')
    mt.next('flashback', 'The story of Lil Z')
    mt.next('forward', 'Lil Dice kills Rocket\'s brother')
    mt.next('forward', 'Lil Z gains amulet and becomes big crime boss')
    mt.next('return')
    mt.next('forward', 'Lil Z starts selling drugs')
    mt.next('forward', 'Benny meets Tiago and becomes a playboy')
    mt.next('forward', 'Lil Z and Carrot beef in the club over the Runt\'s antics')
    mt.next('forward', 'Lil Z gives the runts a lesson')
    mt.next('forward', 'A sucker\'s life')
    mt.next('forward', 'Flirting with crime')
    mt.next('forward', 'Rocket fails at robbing the waitress and the man from Sao Paolo')
    mt.next('forward', '"You need a girlfriend Lil Z"')
    mt.next('forward', 'Benny\'s fairwell')
    mt.next('forward', 'Carrot kills Benny')
    mt.next('forward', 'Knockout Ned and Lil Z\'s inciting incident')
    mt.next('forward', 'The story of Knockout Ned')
    mt.next('forward', 'War breaks out')
    mt.next('forward', 'Rocket takes photos of Lil Z\'s gang')
    mt.next('forward', 'Rocket starts living with professional prohotographer')
    mt.next('forward', 'Lil Z gives the Runts guns')
    mt.next('forward', 'The Beginning of the End')
    mt.next('return')
    mt.next('forward', 'The final war begins and Rocket takes photos')
    mt.next('flashback', 'The story of otto')
    mt.next('return')
    mt.next('forward', 'Lil Z is arrested, Rocket takes photos')
    mt.next('forward', 'Lil Z is killed by the Runts, Rocket takes photos')
    mt.next('forward', 'Rocket gets an internship for his photogrpahy')
    print("\nPreorder(Original) story\n")
    mt.print()
    mt.set_print_function('inorder')
    print("\nInorder story\n")
    mt.print()
    mt.set_print_function('postorder')
    print("\nPostorder story\n")
    mt.print()
    # subprocess.call(["/usr/local/bin/dot","-Tpng","MovieTree.dot","-o","graph1.png"])
    

