from ursina import *

app = Ursina()
gif = 'animation.gif'
a = Animation(gif, parent=camera.ui)
a.scale /= 5 # adjust right size to your needs
a.position = (0.0, 0.0) # lower right of the screen
app.run()