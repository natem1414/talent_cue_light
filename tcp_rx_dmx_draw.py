import socket
import select
import time

#Draw import
import pygame
import array
from ola.ClientWrapper import ClientWrapper

#DMX import
from ola.ClientWrapper import ClientWrapper
import array

test1="test1"

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set the socket to non-blocking mode
server_socket.setblocking(False)

# Bind the socket to an address and port
server_address = ('0.0.0.0', 1231)  # Replace with your desired address and port
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(5)

# Create a list of sockets to monitor for readability
inputs = [server_socket]




DMX_UNIVERSE = 1
wrapper = ClientWrapper()
client = wrapper.Client()


DMX_DATA = array.array('B', [0, 0, 0, 0])
client.SendDmx(DMX_UNIVERSE, DMX_DATA)


# Startup Draw
# Initialize Pygame
pygame.init()
# Set screen dimensions
screen_width = 1920
screen_height = 1080
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
screen.fill((0, 0, 0))  # Black background
# Set box size and position
box_x1 = 0
box_y1 = 0
box_width1 = 1500
box_height1 = 270
box_x2 = 0
box_y2 = 270
box_width2 = 1500
box_height2 = 270
box_x3 = 0
box_y3 = 540
box_width3 = 1500
box_height3 = 270
box_x4 = 0
box_y4 = 810
box_width4 = 1500
box_height4 = 270

box_color1 = (0, 0, 0)
box_color2 = (0, 0, 0)
box_color3 = (0, 0, 0)
box_color4 = (0, 0, 0)

pygame.draw.rect(screen, box_color1, (box_x1, box_y1, box_width1, box_height1))
pygame.draw.rect(screen, box_color2, (box_x2, box_y2, box_width2, box_height2))
pygame.draw.rect(screen, box_color3, (box_x3, box_y3, box_width3, box_height3))
pygame.draw.rect(screen, box_color4, (box_x4, box_y4, box_width4, box_height4))
pygame.display.flip()
print('screen blank boxes')
time.sleep(1)

box_color1 = (255, 0, 255)
box_color2 = (0, 255, 0)
box_color3 = (0, 0, 255)
box_color4 = (255, 255, 255)

print ('TESTING...')
pygame.draw.rect(screen, box_color1, (box_x1, box_y1, box_width1, box_height1))
DMX_DATA[0]=255
pygame.display.flip()
client.SendDmx(DMX_UNIVERSE, DMX_DATA)
time.sleep(.25)
pygame.draw.rect(screen, box_color2, (box_x2, box_y2, box_width2, box_height2))
DMX_DATA[1]=255
pygame.display.flip()
client.SendDmx(DMX_UNIVERSE, DMX_DATA)
time.sleep(.25)
pygame.draw.rect(screen, box_color3, (box_x3, box_y3, box_width3, box_height3))
DMX_DATA[2]=255
pygame.display.flip()
client.SendDmx(DMX_UNIVERSE, DMX_DATA)
time.sleep(.25)
pygame.draw.rect(screen, box_color4, (box_x4, box_y4, box_width4, box_height4))
DMX_DATA[3]=255
pygame.display.flip()
client.SendDmx(DMX_UNIVERSE, DMX_DATA)
time.sleep(.25)
pygame.display.flip()
time.sleep(.25)
box_color1 = (0, 0, 0)
DMX_DATA[0]=0
box_color2 = (0, 0, 0)
DMX_DATA[1]=0
box_color3 = (0, 0, 0)
DMX_DATA[2]=0
box_color4 = (0, 0, 0)
DMX_DATA[3]=0
pygame.draw.rect(screen, box_color1, (box_x1, box_y1, box_width1, box_height1))
pygame.draw.rect(screen, box_color2, (box_x2, box_y2, box_width2, box_height2))
pygame.draw.rect(screen, box_color3, (box_x3, box_y3, box_width3, box_height3))
pygame.draw.rect(screen, box_color4, (box_x4, box_y4, box_width4, box_height4))
client.SendDmx(DMX_UNIVERSE, DMX_DATA)
pygame.display.flip()
print ('TESTing Done')

def dmx_send(server_address, DMX_DATA, TYPE, LED, STATE, ACTIVEBGCOLORRGB, INACTIVEBGCOLORRGB):
  if TYPE == "LIGHT":
    if STATE == "ON":
      if LED == "LED1":
        DMX_DATA[0]=200
      if LED == "LED2":
        DMX_DATA[1]=200
      if LED == "LED3":
        DMX_DATA[2]=255
      if LED == "LED4":
        DMX_DATA[3]=100
    if STATE == "OFF":
      if LED == "LED1":
        DMX_DATA[0]=0
      if LED == "LED2":
        DMX_DATA[1]=0
      if LED == "LED3":
        DMX_DATA[2]=0
      if LED == "LED4":
        DMX_DATA[3]=0
    client.SendDmx(DMX_UNIVERSE, DMX_DATA)
    print('----Sent DMX')
  else:
    print('No DMX Sent')

def screen_draw(server_address, TYPE, LED, STATE, ACTIVETEXT, INACTIVETEXT, ACTIVETEXTCOLORRGB, INACTIVETEXTCOLORRGB, ACTIVEBGCOLORRGB,  INACTIVEBGCOLORRGB):
  if TYPE == "LIGHT":
    if STATE == "ON":
      if LED == "LED1":
        box_color1 = (255, 0, 255)
        pygame.draw.rect(screen, box_color1, (box_x1, box_y1, box_width1, box_height1))
      if LED == "LED2":
        box_color2 = (0, 255, 0)
        pygame.draw.rect(screen, box_color2, (box_x2, box_y2, box_width2, box_height2))
      if LED == "LED3":
        box_color3 = (0, 0, 255)
        pygame.draw.rect(screen, box_color3, (box_x3, box_y3, box_width3, box_height3))
      if LED == "LED4":
        box_color4 = (255, 255, 255)
        pygame.draw.rect(screen, box_color4, (box_x4, box_y4, box_width4, box_height4))
    if STATE == "OFF":
      if LED == "LED1":
        box_color1 = (0, 0, 0)
        pygame.draw.rect(screen, box_color1, (box_x1, box_y1, box_width1, box_height1))
      if LED == "LED2":
        box_color2 = (0, 0, 0)
        pygame.draw.rect(screen, box_color2, (box_x2, box_y2, box_width2, box_height2))
      if LED == "LED3":
        box_color3 = (0, 0, 0)
        pygame.draw.rect(screen, box_color3, (box_x3, box_y3, box_width3, box_height3))
      if LED == "LED4":
        box_color4 = (0, 0, 0)
        pygame.draw.rect(screen, box_color4, (box_x4, box_y4, box_width4, box_height4))
    pygame.display.flip()
    print('----Changed Screen')
  else:
    print('No Screen Chages')

while True:
   # Use select to wait for events on the sockets
  readable, _, _ = select.select(inputs, [], [])  # 1-second timeout
  print('Waiting For Connection at', server_address)

  # Process readable sockets
  for sock in readable:
    if sock is server_socket: # Accept new connection
      connection, client_address = sock.accept()
      print('New connection from', client_address)
      connection.setblocking(False)
      inputs.append(connection)
    else: # Receive data from the client
      try:
        data = sock.recv(1024)
        if data: # Process the received command
 #         print('Received:', data.decode()) # ... handle the command ...
          tcpstring=data.decode()
 #         print('tcpstring:', tcpstring)
          TCPLIST=data.decode().split(';')
          print('tcplist:', TCPLIST)
          TYPE=TCPLIST[0]
          LED=TCPLIST[1]
          STATE=TCPLIST[2]
          ACTIVETEXT=TCPLIST[3]
          INACTIVETEXT=TCPLIST[4]
          ACTIVETEXTCOLOR=TCPLIST[5]
          INACTIVETEXTCOLOR=TCPLIST[6]
          ACTIVEBGCOLOR=TCPLIST[7]
          INACTIVEBGCOLOR=TCPLIST[8]
          ACTIVETEXTCOLORRGB = tuple(int(ACTIVETEXTCOLOR[i:i+2], 16) for i in (0, 2, 4))
          INACTIVETEXTCOLORRGB = tuple(int(INACTIVETEXTCOLOR[i:i+2], 16) for i in (0, 2, 4))
          ACTIVEBGCOLORRGB = tuple(int(ACTIVEBGCOLOR[i:i+2], 16) for i in (0, 2, 4))
          INACTIVEBGCOLORRGB = tuple(int(INACTIVEBGCOLOR[i:i+2], 16) for i in (0, 2, 4))
#          print('ACTIVETEXTCOLOR =', tuple(int(ACTIVETEXTCOLORRGB[i:i+2], 16) for i in (0, 2, 4)))
#          print('INACTIVETEXTCOLOR =', tuple(int(INACTIVETEXTCOLORRGB[i:i+2], 16) for i in (0, 2, 4)))
#          print('ACTIVEBGCOLOR =', tuple(int(ACTIVEBGCOLORRGB[i:i+2], 16) for i in (0, 2, 4)))
#          print('INACTIVEBGCOLOR =', tuple(int(INACTIVEBGCOLORRGB[i:i+2], 16) for i in (0, 2, 4)))
#  print('-----INSIDE screen_draw')
#  print('TYPE:',TYPE )
#  print('LED:', LED)
#  print('STATE:', STATE)
#  print('ACTIVETEXT:', ACTIVETEXT)
#  print('INACTIVETEXT:', INACTIVETEXT)
#  print('ACTIVETEXTCOLOR:', ACTIVETEXTCOLORRGB)
#  print('INACTIVETEXTCOLOR:', INACTIVETEXTCOLORRGB)
#  print('ACTIVEBGCOLOR:', ACTIVEBGCOLORRGB)
#  print('INACTIVEBGCOLOR:', INACTIVEBGCOLORRGB)
#          print('TYPE:',TYPE )
#          print('LED:', LED)
#          print('STATE:', STATE)
#          print('ACTIVETEXT:', ACTIVETEXT)
#          print('INACTIVETEXT:', INACTIVETEXT)
#          print('ACTIVETEXTCOLOR:', ACTIVETEXTCOLOR, ' ', ACTIVETEXTCOLORRGB)
#          print('INACTIVETEXTCOLOR:', INACTIVETEXTCOLOR, ' ', INACTIVETEXTCOLORRGB)
#          print('ACTIVEBGCOLOR:', ACTIVEBGCOLOR, ' ', ACTIVEBGCOLORRGB)
#          print('INACTIVEBGCOLOR:', INACTIVEBGCOLOR, ' ', INACTIVEBGCOLORRGB)
          dmx_send(server_address, DMX_DATA, TYPE, LED, STATE, ACTIVEBGCOLORRGB, INACTIVEBGCOLORRGB)
#          print('-----EXITED dmx_send')
          screen_draw(server_address, TYPE, LED, STATE, ACTIVETEXT, INACTIVETEXT, ACTIVETEXTCOLORRGB, INACTIVETEXTCOLORRGB, ACTIVEBGCOLORRGB, INACTIVEBGCOLORRGB)
#          print('-----EXITED screen_draw')

          
        else: # Connection closed by client
          print('Closing connection from', sock.getpeername())
          inputs.remove(sock)
          sock.close()
      except BlockingIOError: # No data available, continue to the next socket
        pass
