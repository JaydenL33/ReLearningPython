import sqlite3
import struct
from PIL import Image
import zlib
import pygame
import os
from z3 import *
from grid import GRID
from pygame.locals import *
#os.putenv ( "SDL_VIDEODRIVER" , "fbcon" )


DELAY = 0

H = 150
W = 150

offsetW = 0
offsetH = 0
roffsetW = 0
roffsetH = 0

c = sqlite3.connect('real/map.sqlite')


DRAW = True

def getBlockAsInteger(p):
    return int64(p[2]*16777216 + p[1]*4096 + p[0])

def int64(u):
    while u >= 2**63:
        u -= 2**64
    while u <= -2**63:
        u += 2**64
    return u

def getIntegerAsBlock(i):
    x = unsignedToSigned(i % 4096, 2048)
    i = int((i - x) / 4096)
    y = unsignedToSigned(i % 4096, 2048)
    i = int((i - y) / 4096)
    z = unsignedToSigned(i % 4096, 2048)
    return x,y,z

def unsignedToSigned(i, max_positive):
    if i < max_positive:
        return i
    else:
        return i - 2*max_positive

start = getBlockAsInteger([0,0,0])
end = getBlockAsInteger([1,1,1900])

# CREATE TABLE `blocks` (`pos` INT NOT NULL PRIMARY KEY,`data` BLOB);

"""
https://github.com/minetest/minetest/blob/master/doc/world_format.txt
u8 version
u8 flags
u16 lighting_complete
u8 content_width
u8 params_width
"""

def parse(blob):
    
    version, flags, lighting_complete,content_width,params_width = struct.unpack("BBHBB", blob[0:6])
    #print " ------ Block {}".format(pos)
    #print "version:", version
    #print "flags:", flags
    #print "lighting_complete:", lighting_complete
    #print "content_width:", content_width

    dec_o = zlib.decompressobj()
    (param0, param1, param2) = struct.unpack("8192s4096s4096s" ,dec_o.decompress(blob[6:]))
    len(param0)
    #print "param0:", param0
    #print "param1:", param1
    #print "param2:", param2
    tail = dec_o.unused_data
    dec_o = zlib.decompressobj()

    metadata = dec_o.decompress(tail)
    #print "metadata:", metadata.encode('hex')
    (static_version, static_count,timestamp,name_id_mapping_version,num_name_id_mappings) = struct.unpack(">BHIBH", dec_o.unused_data[0:10])
    start = 10
    id_to_name ={}
    ids = []
    for i in range(0, num_name_id_mappings):
        (node_id, name_len) = struct.unpack(">HH", dec_o.unused_data[start:start+4])
        (name,) = struct.unpack(">{}s".format(name_len), dec_o.unused_data[start+4:start+4+name_len])
        id_to_name[node_id] = name.decode('utf8')
        ids.append(name.decode('utf8'))
        #print node_id, name
        start=start+4+name_len
    ids.sort()
    #print id_to_name
    return ids, param0, param1, param2, id_to_name


#pygame.display.flip()
def flip():
    global DELAY
    DELAY += 1
    if DELAY%10==0:
        DELAY = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.flip()

GRID = []
for x in range(0,150*16):
    GRID.append(['']*200*16)

screen  = None
if DRAW:
    pygame.init()
    screen = pygame.display.set_mode(( 10*16*16 , 10*16*16 ))
    #screen = pygame.display.set_mode(( 600 , 600 ))

    color = (0, 0, 0)
    screen.fill(color)

def node(pos, ids, param0, param1, param2, id_to_name):
    global GRID
    w = 16
    x,y  = (pos[0]-roffsetW)*w, (pos[1]-roffsetH)*w
    """if any('air' in s for s in ids):
        pygame.draw.rect(screen, (150, 150, 255), pygame.Rect((offsetW*16*16)+x, y, w, w))
    if any('default:stone' in s for s in ids):
        pygame.draw.rect(screen, (150, 150, 150), pygame.Rect((offsetW*16*16)+x, y, w, w))
    if any('mesecons_insulated:insulated' in s for s in ids):
        pygame.draw.rect(screen, (0, 0, 255), pygame.Rect((offsetW*16*16)+x+w/2, y, 1, w))
    if any('mesecons_extrawires:corner' in s for s in ids):
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect((offsetW*16*16)+x, y+w/2, w/2, 1))
    if any('mesecons_extrawires:crossover' in s for s in ids):
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect((offsetW*16*16)+x, y+w/2, w, 1))
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect((offsetW*16*16)+x+w/2, y, 1, w))
    if any('mesecons_gates:' in s for s in ids):
        pygame.draw.rect(screen, (250, 250, 0), pygame.Rect((offsetW*16*16)+x+2, y+2, w-4, w-4))"""


    """
    0   z
    1   x
    2   -z
    3   -x
    """
    for i in range(0,16):
        for j in range(0,16):
            for e in range(2,3):
                p0 = param0[j*2+(e*16*2)+i*(16*16*2):j*2+(e*16*2)+i*(16*16*2)+2]
                #print p0.encode('hex')
                asd = struct.unpack(">H", p0)[0]
                asd_ = ord(param0[j+(e*16)+i*(16*16)])
                asd1 = ord(param1[j+(e*16)+i*(16*16)])
                asd2 = ord(param2[j+(e*16)+i*(16*16)])
                
                if 'mesecons_insulated:insulated' in id_to_name[asd]:
                    #screen.set_at(((offsetW*16*16)+(x+i)*w, (y+j)*w), col)
                    if asd2%4 == 0:  # top-bottom
                        GRID[x+i][y+j] = '|'
                        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect((offsetW*16*16)+(x+i)*w+w/2, (y+j)*w+(offsetH*16*16), 1, w))
                    else: #left-right
                        #print x+i,y+j
                        GRID[x+i][y+j] = '-'
                        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect((offsetW*16*16)+(x+i)*w, (y+j)*w+w/2+(offsetH*16*16), w, 1))
                elif 'mesecons_extrawires:crossover' in id_to_name[asd]:
                    GRID[x+i][y+j] = '+'
                    pygame.draw.rect(screen, (150, 150, 150), pygame.Rect((offsetW*16*16)+(x+i)*w, (y+j)*w+w/2+(offsetH*16*16), w, 1))
                    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect((offsetW*16*16)+(x+i)*w+w/2, (y+j)*w+(offsetH*16*16), 1, w))
                elif 'mesecons_extrawires:corner' in id_to_name[asd]:
                    if asd2%4 == 3: # left-bottom
                        GRID[x+i][y+j] = ','
                        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect((offsetW*16*16)+(x+i)*w+w/2, (y+j)*w+w/2+(offsetH*16*16),   1, w/2))
                        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect((offsetW*16*16)+(x+i)*w,     (y+j)*w+w/2+(offsetH*16*16), w/2, 1))
                    if asd2%4 == 2: # right-bottom
                        GRID[x+i][y+j] = '.'
                        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect((offsetW*16*16)+(x+i)*w+w/2, (y+j)*w+w/2+(offsetH*16*16),   1, w/2))
                        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect((offsetW*16*16)+(x+i)*w+w/2, (y+j)*w+w/2+(offsetH*16*16), w/2, 1))
                    if asd2%4 == 1: # right-top
                        GRID[x+i][y+j] = '"'
                        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect((offsetW*16*16)+(x+i)*w+w/2, (y+j)*w+(offsetH*16*16),       1, w/2))
                        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect((offsetW*16*16)+(x+i)*w+w/2, (y+j)*w+w/2+(offsetH*16*16), w/2, 1))
                    if asd2%4 == 0: # left-top
                        GRID[x+i][y+j] = '`'
                        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect((offsetW*16*16)+(x+i)*w+w/2,     (y+j)*w+(offsetH*16*16),   1, w/2))
                        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect((offsetW*16*16)+(x+i)*w,     (y+j)*w+w/2+(offsetH*16*16), w/2, 1))
                elif 'mesecons_extrawires:tjunction' in id_to_name[asd]:
                    if asd2%4 == 3: # left-right-bottom
                        GRID[x+i][y+j] = 'T'
                        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect((offsetW*16*16)+(x+i)*w+w/2, (y+j)*w+w/2+(offsetH*16*16),   1, w/2))
                        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect((offsetW*16*16)+(x+i)*w,     (y+j)*w+w/2+(offsetH*16*16), w, 1))
                    if asd2%4 == 2: 
                        print('tjunction not implemented')
                        exit(0)
                        pygame.draw.rect(screen, (0, 0, 255), pygame.Rect((offsetW*16*16)+(x+i)*w+w/2, (y+j)*w+w/2+(offsetH*16*16),   1, w/2))
                        pygame.draw.rect(screen, (0, 0, 255), pygame.Rect((offsetW*16*16)+(x+i)*w+w/2, (y+j)*w+w/2+(offsetH*16*16), w/2, 1))
                    if asd2%4 == 1: # left-right-top
                        GRID[x+i][y+j] = '^'
                        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect((offsetW*16*16)+(x+i)*w+w/2, (y+j)*w+(offsetH*16*16),       1, w/2))
                        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect((offsetW*16*16)+(x+i)*w, (y+j)*w+w/2+(offsetH*16*16), w, 1))
                    if asd2%4 == 0: 
                        print('tjunction not implemented')
                        exit(0)
                        pygame.draw.rect(screen, (0, 0, 255), pygame.Rect((offsetW*16*16)+(x+i)*w+w/2,     (y+j)*w+(offsetH*16*16),   1, w/2))
                        pygame.draw.rect(screen, (0, 0, 255), pygame.Rect((offsetW*16*16)+(x+i)*w,     (y+j)*w+w/2+(offsetH*16*16), w/2, 1))
                elif 'mesecons_walllever:wall_lever_off' in id_to_name[asd]:
                    GRID[x+i][y+j] = '@'
                    print "lever: {}/{}".format(x+i,y+j)
                    pygame.draw.rect(screen, (250, 50, 50), pygame.Rect((offsetW*16*16)+(x+i)*w+2, (y+j)*w+2+(offsetH*16*16), w-4, w-4))
                elif 'mesecons_gates:and' in id_to_name[asd]:
                    GRID[x+i][y+j] = 'A'
                    pygame.draw.rect(screen, (200, 200, 200), pygame.Rect((offsetW*16*16)+(x+i)*w+2, (y+j)*w+2+(offsetH*16*16), w-4, w-4))
                   
                    
                    screen.set_at(((offsetW*16*16)+(x+i)*w+w/2-2, (y+j)*w+w/2-2+(offsetH*16*16)),(0,0,0))
                    screen.set_at(((offsetW*16*16)+(x+i)*w+w/2-2, (y+j)*w+w/2-1+(offsetH*16*16)),(0,0,0))
                    screen.set_at(((offsetW*16*16)+(x+i)*w+w/2-2, (y+j)*w+w/2+(offsetH*16*16)),(0,0,0))
                    screen.set_at(((offsetW*16*16)+(x+i)*w+w/2-2, (y+j)*w+w/2+1+(offsetH*16*16)),(0,0,0))
                    screen.set_at(((offsetW*16*16)+(x+i)*w+w/2-2, (y+j)*w+w/2+2+(offsetH*16*16)),(0,0,0))

                    screen.set_at(((offsetW*16*16)+(x+i)*w+w/2-1, (y+j)*w+w/2-2+(offsetH*16*16)),(0,0,0))
                    screen.set_at(((offsetW*16*16)+(x+i)*w+w/2,   (y+j)*w+w/2-2+(offsetH*16*16)),(0,0,0))
                    screen.set_at(((offsetW*16*16)+(x+i)*w+w/2+1, (y+j)*w+w/2-1+(offsetH*16*16)),(0,0,0))
                    screen.set_at(((offsetW*16*16)+(x+i)*w+w/2+1, (y+j)*w+w/2+(offsetH*16*16)),(0,0,0))
                    screen.set_at(((offsetW*16*16)+(x+i)*w+w/2+1, (y+j)*w+w/2+1+(offsetH*16*16)),(0,0,0))
                    screen.set_at(((offsetW*16*16)+(x+i)*w+w/2,   (y+j)*w+w/2+2+(offsetH*16*16)),(0,0,0))
                    screen.set_at(((offsetW*16*16)+(x+i)*w+w/2-1, (y+j)*w+w/2+2+(offsetH*16*16)),(0,0,0))


                elif 'mesecons_gates:or' in id_to_name[asd]:
                    GRID[x+i][y+j] = 'O'
                    pygame.draw.rect(screen, (200, 200, 200), pygame.Rect((offsetW*16*16)+(x+i)*w+2, (y+j)*w+2+(offsetH*16*16), w-4, w-4))
                    
                    screen.set_at(((offsetW*16*16)+(x+i)*w+w/2-2, (y+j)*w+w/2-2+(offsetH*16*16)),(0,0,0))
                    screen.set_at(((offsetW*16*16)+(x+i)*w+w/2-2, (y+j)*w+w/2-1+(offsetH*16*16)),(0,0,0))
                    screen.set_at(((offsetW*16*16)+(x+i)*w+w/2-1, (y+j)*w+w/2+(offsetH*16*16)),(0,0,0))
                    screen.set_at(((offsetW*16*16)+(x+i)*w+w/2-2, (y+j)*w+w/2+1+(offsetH*16*16)),(0,0,0))
                    screen.set_at(((offsetW*16*16)+(x+i)*w+w/2-2, (y+j)*w+w/2+2+(offsetH*16*16)),(0,0,0))

                    screen.set_at(((offsetW*16*16)+(x+i)*w+w/2-1, (y+j)*w+w/2-2+(offsetH*16*16)),(0,0,0))
                    screen.set_at(((offsetW*16*16)+(x+i)*w+w/2,   (y+j)*w+w/2-2+(offsetH*16*16)),(0,0,0))
                    screen.set_at(((offsetW*16*16)+(x+i)*w+w/2+1, (y+j)*w+w/2-1+(offsetH*16*16)),(0,0,0))
                    screen.set_at(((offsetW*16*16)+(x+i)*w+w/2+2, (y+j)*w+w/2+(offsetH*16*16)),(0,0,0))
                    screen.set_at(((offsetW*16*16)+(x+i)*w+w/2+1, (y+j)*w+w/2+1+(offsetH*16*16)),(0,0,0))
                    screen.set_at(((offsetW*16*16)+(x+i)*w+w/2,   (y+j)*w+w/2+2+(offsetH*16*16)),(0,0,0))
                    screen.set_at(((offsetW*16*16)+(x+i)*w+w/2-1, (y+j)*w+w/2+2+(offsetH*16*16)),(0,0,0))

                elif 'mesecons_gates:xor' in id_to_name[asd]:
                    GRID[x+i][y+j] = 'X'
                    pygame.draw.rect(screen, (200, 200, 200), pygame.Rect((offsetW*16*16)+(x+i)*w+2, (y+j)*w+2+(offsetH*16*16), w-4, w-4))
                    screen.set_at(((offsetW*16*16)+(x+i)*w+w/2-2, (y+j)*w+w/2-2+(offsetH*16*16)),(0,0,0))
                    screen.set_at(((offsetW*16*16)+(x+i)*w+w/2-2, (y+j)*w+w/2-1+(offsetH*16*16)),(0,0,0))
                    screen.set_at(((offsetW*16*16)+(x+i)*w+w/2-1, (y+j)*w+w/2+(offsetH*16*16)),(0,0,0))
                    screen.set_at(((offsetW*16*16)+(x+i)*w+w/2-2, (y+j)*w+w/2+1+(offsetH*16*16)),(0,0,0))
                    screen.set_at(((offsetW*16*16)+(x+i)*w+w/2-2, (y+j)*w+w/2+2+(offsetH*16*16)),(0,0,0))

                    screen.set_at(((offsetW*16*16)+(x+i)*w+w/2-1, (y+j)*w+w/2-2+(offsetH*16*16)),(0,0,0))
                    screen.set_at(((offsetW*16*16)+(x+i)*w+w/2,   (y+j)*w+w/2-2+(offsetH*16*16)),(0,0,0))
                    screen.set_at(((offsetW*16*16)+(x+i)*w+w/2+1, (y+j)*w+w/2-1+(offsetH*16*16)),(0,0,0))
                    screen.set_at(((offsetW*16*16)+(x+i)*w+w/2+2, (y+j)*w+w/2+(offsetH*16*16)),(0,0,0))
                    screen.set_at(((offsetW*16*16)+(x+i)*w+w/2+1, (y+j)*w+w/2+1+(offsetH*16*16)),(0,0,0))
                    screen.set_at(((offsetW*16*16)+(x+i)*w+w/2,   (y+j)*w+w/2+2+(offsetH*16*16)),(0,0,0))
                    screen.set_at(((offsetW*16*16)+(x+i)*w+w/2-1, (y+j)*w+w/2+2+(offsetH*16*16)),(0,0,0))

                    screen.set_at(((offsetW*16*16)+(x+i)*w+w/2+3, (y+j)*w+w/2+(offsetH*16*16)),(0,0,0))
                    screen.set_at(((offsetW*16*16)+(x+i)*w+w/2+4, (y+j)*w+w/2-1+(offsetH*16*16)),(0,0,0))
                    screen.set_at(((offsetW*16*16)+(x+i)*w+w/2+4, (y+j)*w+w/2+(offsetH*16*16)),(0,0,0))
                    screen.set_at(((offsetW*16*16)+(x+i)*w+w/2+4, (y+j)*w+w/2+1+(offsetH*16*16)),(0,0,0))
                    screen.set_at(((offsetW*16*16)+(x+i)*w+w/2+5, (y+j)*w+w/2+(offsetH*16*16)),(0,0,0))

                elif 'mesecons_gates:not' in id_to_name[asd]:
                    GRID[x+i][y+j] = 'N'
                    screen.set_at(((offsetW*16*16)+(x+i)*w+w/2-2, (y+j)*w+w/2-3+(offsetH*16*16)),(0,0,0))
                    screen.set_at(((offsetW*16*16)+(x+i)*w+w/2-2, (y+j)*w+w/2-2+(offsetH*16*16)),(0,0,0))
                    screen.set_at(((offsetW*16*16)+(x+i)*w+w/2-2, (y+j)*w+w/2-1+(offsetH*16*16)),(0,0,0))
                    screen.set_at(((offsetW*16*16)+(x+i)*w+w/2-2, (y+j)*w+w/2+(offsetH*16*16)),(0,0,0))
                    screen.set_at(((offsetW*16*16)+(x+i)*w+w/2-2, (y+j)*w+w/2+1+(offsetH*16*16)),(0,0,0))
                    screen.set_at(((offsetW*16*16)+(x+i)*w+w/2-2, (y+j)*w+w/2+2+(offsetH*16*16)),(0,0,0))
                    screen.set_at(((offsetW*16*16)+(x+i)*w+w/2-2, (y+j)*w+w/2+3+(offsetH*16*16)),(0,0,0))

                    screen.set_at(((offsetW*16*16)+(x+i)*w+w/2-1, (y+j)*w+w/2-2+(offsetH*16*16)),(0,0,0))
                    screen.set_at(((offsetW*16*16)+(x+i)*w+w/2,   (y+j)*w+w/2-1+(offsetH*16*16)),(0,0,0))
                    screen.set_at(((offsetW*16*16)+(x+i)*w+w/2+1, (y+j)*w+w/2+(offsetH*16*16)),(0,0,0))
                    screen.set_at(((offsetW*16*16)+(x+i)*w+w/2,   (y+j)*w+w/2+1+(offsetH*16*16)),(0,0,0))
                    screen.set_at(((offsetW*16*16)+(x+i)*w+w/2-1, (y+j)*w+w/2+2+(offsetH*16*16)),(0,0,0))

                    screen.set_at(((offsetW*16*16)+(x+i)*w+w/2+2, (y+j)*w+w/2+(offsetH*16*16)),(0,0,0))
                    screen.set_at(((offsetW*16*16)+(x+i)*w+w/2+3, (y+j)*w+w/2-1+(offsetH*16*16)),(0,0,0))
                    screen.set_at(((offsetW*16*16)+(x+i)*w+w/2+3, (y+j)*w+w/2+(offsetH*16*16)),(0,0,0))
                    screen.set_at(((offsetW*16*16)+(x+i)*w+w/2+3, (y+j)*w+w/2+1+(offsetH*16*16)),(0,0,0))
                    screen.set_at(((offsetW*16*16)+(x+i)*w+w/2+4, (y+j)*w+w/2+(offsetH*16*16)),(0,0,0))
                    #pygame.draw.rect(screen, (200, 200, 200), pygame.Rect((offsetW*16*16)+(x+i)*w+2, (y+j)*w+2, w-4, w-4))
                    screen.set_at(((offsetW*16*16)+(x+i)*w+w/2, (y+j)*w+w/2+(offsetH*16*16)),(0,0,0))
                elif 'air' in id_to_name[asd] or 'stone' in id_to_name[asd] or 'ignore' in id_to_name[asd]:
                    pass
                else:
                    print "{} unkown".format(id_to_name[asd])
    #screen.set_at(((offsetW*16*16)+x,y+(offsetH*16*16)),(0,0,0))


if DRAW:
    for x in range(roffsetH,roffsetH+H):
        #print x,'/',H
        for z in range(roffsetW,roffsetW+W):
            #print x,'/',H,' | ',z,'/',W
            for a in c.execute('SELECT * from blocks where pos = {}'.format(getBlockAsInteger([x,0,z]))):
                x,y,z = getIntegerAsBlock(a[0])
                ids, param0, param1, param2, id_to_name = parse(a[1])
                    
                #draw((z+2, x+2), ids, param2, id_to_name,2)
                node((z, x), ids, param0,param1,param2, id_to_name)
                #pygame.display.update((x,z,x+1,z+1))
                    
        # if x%1 == 0:
        #    flip()

flip()
print("done drawing. save")
#pygame.image.save(screen, 'map_{}_{}.png'.format(roffsetW, roffsetH))

with open('grid.py', 'w') as f:
    f.write(str(GRID))


exit(0) # remove me

if DRAW:
    while True:
        flip()

