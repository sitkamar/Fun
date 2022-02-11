from ursina import *
from ursina.prefabs.\
    first_person_controller \
    import FirstPersonController
app = Ursina()
Sky(texture='sky_sunset')
player = FirstPersonController()

boxes = []
for n in range(20):
    for k in range(20):
        box = Button(
            color=color.white,
            model='cube',
            position=(n, 0, k),
            texture='grass',
            parent=scene,
            origin_y=0.5
        )
        boxes.append(box)
sword = Entity(
    model='arrow',
    texture='cursor',
    rotation=(30, -40),
    position=(0.5, -0.6),
    parent=camera,
)
def input(key):
    for box in boxes:
        if box.hovered:
            if key == 'right mouse down':
                new = Button(
                    color=color.white,
                    model='cube',
                    position=box.position + mouse.normal,
                    texture='grass',
                    parent=scene,
                    origin_y=0.5
                )
                boxes.append(new)
            if key == 'left mouse down':
                boxes.remove(box)
                destroy(box)
app.run()
