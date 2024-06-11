from ursina import *
from ursina.prefabs.first_person_controller import *

def update():
    if held_keys['shift']:
        player.speed=10
    if player.y < -1:
        player.position = (16,0,-18)
    print(player.position)

def input(key):
    if key == 'shift':
        print("Shift Pressed")      
    if key == 'w' or key == 'a' or key == 'd' or key == 's':
        player.speed=20


app = Ursina()


maze = Entity(model = 'maze', texture='brick', scale=20, collider='mesh')
#firstEntity = Entity(model = 'cube',texture='brick',position=(0,0,0),rotation=(0,0,0),scale=2)
#secondEntity = Entity(model = 'among_us_obj\among us + turbosmooth 1.obj',position=(0,0,0),rotation=(0,0,0),scale=2)
#EditorCamera()

window.fullscreen = True
player = FirstPersonController(position=(16,0,-18))
player.jump_height = 10

#video = Entity(model='cube', texture='Green Screen - 2rgx_butterfly 720p.mp4', parent=camera.ui, scale=(1.79, 1, 0))

a = Animation('static\rgx_butterfly_knife_main.gif',parent=camera.ui)
a.scale /= 9
a.position = (0.0,0.0)

app.run()

