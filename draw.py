import pygame
import array
from ola.ClientWrapper import ClientWrapper

#OLA web UI: http://192.168.0.251:9090/ola.html

# Initialize Pygame
pygame.init()

# Set screen dimensions
screen_width = 1920
screen_height = 1080
screen = pygame.display.set_mode((screen_width, screen_height))

# Set box properties
box_color1 = (255, 0, 0)  # Red
box_x1 = 0
box_y1 = 0
box_width1 = 1500
box_height1 = 270

box_color2 = (0, 255, 0)  # Red
box_x2 = 0
box_y2 = 270
box_width2 = 1500
box_height2 = 270

box_color3 = (0, 0, 255)  # Red
box_x3 = 0
box_y3 = 540
box_width3 = 1500
box_height3 = 270

box_color4 = (220, 220, 220)  # Red
box_x4 = 0
box_y4 = 810
box_width4 = 1500
box_height4 = 270

DMX_UNIVERSE = 1
wrapper = ClientWrapper()
client = wrapper.Client()


def DmxSent(state):
  print('DmxSent')
#  wrapper.Stop()


DMX_DATA = array.array('B', [255, 255, 255, 255])



#client.SendDmx(DMX_UNIVERSE, DMX_DATA, DmxSent)
client.SendDmx(DMX_UNIVERSE, DMX_DATA)

#wrapper.Run()



# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))  # Black background

    # Draw the box
    pygame.draw.rect(screen, box_color1, (box_x1, box_y1, box_width1, box_height1))
    pygame.draw.rect(screen, box_color2, (box_x2, box_y2, box_width2, box_height2))
    pygame.draw.rect(screen, box_color3, (box_x3, box_y3, box_width3, box_height3))
    pygame.draw.rect(screen, box_color4, (box_x4, box_y4, box_width4, box_height4))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
