import pgzrun
import imgui
from imgui.integrations.pygame import PygameRenderer
import pygame
from OpenGL.GL import *

WIDTH = 800
HEIGHT = 600

# Initialize ImGui context and PygameRenderer
imgui.create_context()
renderer = None
initialized = False

# Create a Pygame clock to track FPS
clock = pygame.time.Clock()

def init():
    global renderer, initialized
    pygame.display.set_mode((WIDTH, HEIGHT), pygame.OPENGL | pygame.DOUBLEBUF)
    renderer = PygameRenderer()
    if not glGetString(GL_VERSION):
        raise RuntimeError("OpenGL context creation failed")
    print("OpenGL Version:", glGetString(GL_VERSION).decode('utf-8'))
    initialized = True

def update():
    if not initialized:
        init()
    # Limit the frame rate to 60 FPS
    clock.tick(60)

def draw():
    if not initialized:
        init()
    screen.clear()
    screen.fill((0, 0, 0))
    render_imgui()

def render_imgui():
    io = imgui.get_io()
    io.display_size = (WIDTH, HEIGHT)  # Set the display size

    imgui.new_frame()

    imgui.begin("Hello, ImGui!", True)
    imgui.text("This is a simple integration of Pygame Zero with ImGui.")
    imgui.text("FPS: {:.2f}".format(clock.get_fps()))
    imgui.end()

    glClearColor(0.1, 0.1, 0.1, 1)
    glClear(GL_COLOR_BUFFER_BIT)

    imgui.render()
    draw_data = imgui.get_draw_data()
    draw_data.scale_clip_rects(1.0,1.0)  # Properly scale the clip rects
    renderer.render(draw_data)
    imgui.end_frame()

pgzrun.go()
