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
class MovieTree:

    def __init__(self, initial_scene):
        self.root_scene = Scene(initial_scene, None)
        self.current_scene = self.root_scene

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
            print('not a valid next scene type')


    def __repr__(self):
        return MovieTree.inorder(self.root_scene)

    @staticmethod
    def inorder(scene):
        if scene:
            flashback = MovieTree.inorder(scene.left_scene)
            forward = MovieTree.inorder(scene.right_scene)
            return scene.scene_tag + ' ' + flashback + forward
        else:
            return ''
            
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
    mt = MovieTree('1')
    mt.next('flashback', '2')
    mt.next('forward', '3')
    mt.next('forward', '4')
    mt.next('flashback', '5')
    mt.next('return')
    mt.next('forward', '6')
    mt.next('flashback', '7')
    mt.next('forward', '8')
    mt.next('forward', '9')
    mt.next('return')
    mt.next('return')
    print(mt)
    print("done")
