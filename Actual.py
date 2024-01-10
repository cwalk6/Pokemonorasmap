#Start pygame
import pygame
from heapq import heapify, heappop, heappush
pygame.init()

#Graphs
towns = {"Littleroot": (365,665), "Oldale": (363,578), "Petalburg": (231,577),"Rustboro": (186,359), "Fallarbor": (319, 138), 'Verdanturf': (363,402), "Lavaridge": (411,312), "Dewford": (274,797), "Slateport": (538,619), "Mauville": (539,399), "Fortree": (714,136), "Lilycove": (1022,267), "Pacifidlog":(980,621), "Sootopolis": (1133,503), "Mossdeep": (1241,335), "Ever Grande":(1375,575), "Pokemon League":(1375,478)}
specials = {"Petalburg Woods":(177,484), "Meteor Falls":(210,229), "Rusturf Tunnel":(364,358), "New Mauville":(589,450), "Granite Cave":(229,801), "Sea Mauville":(472,752), "Fiery Path":(477,270),"Jagged Pass":(434,266),"Mt Chimney":(434,223),"Safari Zone":(872,225),"Mt Pyre":(927,348),"Shoal Cave":(1322,280),"Victory Road":(1379,529),"Cave of Origin":(1070,444),"Secret Isle":(1068,505),"Sky Pillar":(1082,575),"Secret Meadow":(1152,574),"Seafloor Cavern":(1253,576),"Secret Shore":(1329,667)}
connections = {'Littleroot Route 101': [[(383,687),(383,645)]],
               'Oldale Route 101': [[(383,645),(383,594)]],
               'Oldale Route 102': [[(383,599),(313,599)]],
               'Oldale Route 103': [[(383,599),(383,548)]],
               'Petalburg Route 102': [[(313,599),(251,599)]],
               'Route 103 Route 110': [[(383,548),(559,548)]],
               'Petalburg Route 104': [[(251,599),(204,599)]],
               'Petalburg Woods Route 104': [[(204,505),(197,505)]],
               'Route 104 Rustboro': [[(204,599),(204,374)]],
               'Route 104 Route 105': [[(204,599),(204,721)]],
               'Route 116 Rustboro': [[(204,374),(331,374)]],
               'Route 115 Rustboro': [[(204,374),(204,246)]],
               'Route 116 Rusturf Tunnel': [[(381,374),(206,374)]],
               'Rusturf Tunnel Verdanturf': [[(381,374),(381,419)]],
               'Route 105 Route 106': [[(204,721),(204,771)],[(204,771),(293,771)]],
               'Dewford Route 106': [[(293,771),(293,814)]],
               'Dewford Route 107': [[(293,814),(383,814)]],
               'Dewford Granite Cave': [[(293,814),(247,814)]],
               'Route 107 Route 108': [[(383,814),(490,814)]],
               'Route 108 Sea Mauville': [[(490,814),(490,772)]],
               'Route 108 Route 109': [[(490,814),(559,814)]],
               'Route 109 Slateport': [[(559,814),(559,641)]],
               'Route 110 Slateport': [[(559,641),(559,548)]],
               'Route 134 Slateport': [[(559,641),(635,641)]],
               'Mauville Route 110': [[(559,548),(559,419)]],
               'New Mauville Route 110': [[(559,471),(609,471)],[(559,471),(559,548)]],
               'Mauville Route 117': [[(559,419),(445,419)]],
               'Mauville Route 111': [[(559,419),(559,332)]],
               'Mauville Route 118': [[(559,419),(690,419)]],
               'Route 117 Verdanturf': [[(381,419),(445,419)]],
               'Route 111 Route 112': [[(559,332),(496,332)]],
               'Route 111 Route 113': [[(559,332),(559,156)],[(559,156),(448,156)]],
               'Jagged Pass Route 112': [[(496,332),(453,288)]],
               'Lavaridge Route 112': [[(496,332),(431,332)]],
               'Fiery Path Route 112': [[(496,332),(496,289)]],
               'Jagged Pass Mt Chimney': [[(453,288),(453,243)]],
               'Fallarbor Route 113': [[(448,156),(339,156)]],
               'Fallarbor Route 114': [[(339,156),(275,156)]],
               'Meteor Falls Route 114': [[(275,156),(275,246)],[(275,246),(229,246)]],
               'Meteor Falls Route 115': [[(229,246),(204,246)]],
               'Route 118 Route 119': [[(688,419),(688,156)]],
               'Route 118 Route 123': [[(688,419),(893,419)]],
               'Fortree Route 119': [[(688,156),(734,156)]],
               'Fortree Route 120': [[(734,156),(778,156)],[(778,156),(778,285)]],
               'Route 120 Route 121': [[(778,285),(893,285)]],
               'Route 121 Route 122': [[(893,285),(893,364)]],
               'Lilycove Route 121': [[(893,285),(1042,285)]],
               'Route 121 Safari Zone': [[(893,247),(893,285)]],
               'Route 122 Route 123': [[(893,364),(893,419)]],
               'Mt Pyre Route 122': [[(893,364),(945,364)]],
               'Lilycove Route 124': [[(1042,285),(1151,285)],[(1151,285),(1151,355)],[(1151,355),(1205,355)]],
               'Mossdeep Route 124': [[(1205,355),(1261,355)]],
               'Route 124 Route 126': [[(1205,355),(1205,529)]],
               'Route 126 Sootopolis': [[(1205,529),(1154,529)]],
               'Route 126 Route 127': [[(1205,529),(1345,529)]],
               'Route 126 Secret Isle': [[(1205,529),(1089,529)]],
               'Cave of Origin Sootopolis': [[(1154,529),(1087,463)]],
               'Mossdeep Route 127': [[(1261,355),(1345,355)],[(1345,355),(1345,529)]],
               'Mossdeep Route 125': [[(1261,355),(1261,295)]],
               'Route 125 Shoal Cave': [[(1340,295),(1261,295)]],
               'Route 127 Route 128': [[(1345,529),(1345,596)]],
               'Route 128 Route 129': [[(1345,596),(1345,641)]],
               'Ever Grande Route 128': [[(1345,596),(1395,596)]],
               'Route 128 Seafloor Cavern': [[(1345,596),(1272,596)]],
               'Ever Grande Victory Road': [[(1395,596),(1395,543)]],
               'Pokemon League Victory Road': [[(1395,543),(1395,496)]],
               'Route 129 Secret Shore': [[(1345,641),(1345,685)]],
               'Route 129 Route 130': [[(1345,641),(1172,641)]],
               'Route 130 Route 131': [[(1172,641),(1097,641)]],
               'Route 130 Secret Meadow': [[(1172,641),(1172,594)]],
               'Route 131 Sky Pillar': [[(1097,641),(1097,594)]],
               'Pacifidlog Route 131': [[(1097,641),(998,641)]],
               'Pacifidlog Route 132': [[(998,641),(909,641)]],
               'Route 132 Route 133': [[(909,641),(776,641)]],
               'Route 133 Route 134': [[(776,641),(635,641)]]}
graph = {"Littleroot": [(4, "Route 101")],
         "Route 101": [(4, "Littleroot"), (6, "Oldale")],
         "Oldale": [(6, "Route 101"), (13, "Route 102"), (8, "Route 103")],
         "Route 102": [(13,"Oldale"), (5,"Petalburg")],
         "Route 103": [(8,"Oldale"), (18,"Route 110")],
         "Petalburg": [(5,"Route 102"), (4, "Route 104")],
         "Route 104": [(4, "Petalburg"), (2, "Petalburg Woods"),(25, "Rustboro"), (12, "Route 105")],
         "Petalburg Woods": [(2, "Route 104")],
         "Rustboro": [(25, "Route 104"), (14,"Route 116"), (19, "Route 115")],
         "Route 116": [(14, "Rustboro"), (5, "Rusturf Tunnel")],
         "Rusturf Tunnel": [(5, "Route 116"), (21, "Verdanturf")],
         "Route 105": [(12, "Route 104"), (21,"Route 106")],
         "Route 106": [(21, "Route 105"), (14, "Dewford")],
         "Dewford": [(14, "Route 106"), (15, "Route 107"), (9, "Granite Cave")],
         "Granite Cave": [(9, "Dewford")],
         "Route 107": [(15, "Dewford"), (23, "Route 108")],
         "Route 108": [(23, "Route 107"), (11, "Sea Mauville"), (17, "Route 109")],
         "Sea Mauville": [(11, "Route 108")],
         "Route 109": [(17, "Route 108"), (12, "Slateport")],
         "Slateport": [(12,"Route 109"), (24,"Route 110"),(27,"Route 134")],
         "Route 110": [(24, "Slateport"), (18, "Route 103"), (16, "Mauville"), (7, "New Mauville")],
         "New Mauville": [(7, "Route 110")],
         "Mauville": [(16, "Route 110"), (9, "Route 117"), (35, "Route 111"), (8,"Route 118")],
         "Route 117": [(9, "Mauville"), (4, "Verdanturf")],
         "Verdanturf": [(4, "Route 117"), (21,"Rusturf Tunnel")],
         "Route 111": [(35, "Mauville"), (12, "Route 112"), (18, "Route 113")],
         "Route 112": [(12, "Route 111"), (24, "Jagged Pass"),(11, "Lavaridge"), (31, "Fiery Path")],
         "Lavaridge": [(11, "Route 112")],
         "Fiery Path": [(31, "Route 112")],
         "Jagged Pass": [(24, "Route 112"), (16, "Mt Chimney")],
         "Mt Chimney": [(16, "Jagged Pass")],
         "Route 113": [(17, "Fallarbor"), (18, "Route 111")],
         "Fallarbor": [(17, "Route 113"), (17, "Route 114")],
         "Route 114": [(17, "Fallarbor"), (26, "Meteor Falls")],
         "Meteor Falls": [(26, "Route 114"), (19, "Route 115")],
         "Route 115": [(19, "Meteor Falls"), (19, "Rustboro")],
         "Route 118": [(8, "Mauville"), (19, "Route 119"), (11, "Route 123")],
         "Route 119": [(19, "Route 118"), (27, "Fortree")],
         "Fortree": [(27, "Route 119"), (21, "Route 120")],
         "Route 120": [(21, "Fortree"), (9, "Route 121")],
         "Route 121": [(9, "Route 120"), (10, "Route 122"), (15, "Lilycove"), (4, "Safari Zone")],
         "Safari Zone": [(4, "Route 121")],
         "Route 122": [(10, "Route 121"), (15, "Route 123"), (5, "Mt Pyre")],
         "Mt Pyre": [(5, "Route 122")],
         "Route 123": [(15, "Route 122"), (11, "Route 118")],
         "Lilycove": [(15, "Route 121"), (17, "Route 124")],
         "Route 124": [(17, "Lilycove"), (26, "Mossdeep"), (14, "Route 126")],
         "Route 126": [(14, "Route 124"), (10, "Sootopolis"), (24, "Route 127"), (13, "Secret Isle")],
         "Sootopolis": [(10, "Route 126"), (3, "Cave of Origin")],
         "Secret Isle": [(13, "Route 126")],
         "Cave of Origin": [(3, "Sootopolis")],
         "Mossdeep": [(26, "Route 124"), (18, "Route 127"), (12,"Route 125")],
         "Route 125": [(22, "Shoal Cave"), (12, "Mossdeep")],
         "Shoal Cave": [(22, "Route 125")],
         "Route 127": [(18, "Mossdeep"), (24, "Route 126"), (13, "Route 128")],
         "Route 128": [(13, "Route 127"), (23, "Route 129"), (19, "Ever Grande"), (18, "Seafloor Cavern")],
         "Seafloor Cavern": [(18, "Route 128")],
         "Ever Grande": [(19, "Route 128"), (45, "Victory Road")],
         "Victory Road": [(45, "Ever Grande"), (31, "Pokemon League")],
         "Pokemon League": [(31, "Victory Road")],
         "Route 129": [(23,"Route 128"), (19, "Secret Shore"), (14, "Route 130")],
         "Secret Shore": [(19, "Route 129")],
         "Route 130": [(14, "Route 129"),(24, "Route 131"), (31, "Secret Meadow")],
         "Secret Meadow": [(31, "Route 130")],
         "Route 131": [(24, "Route 130"), (18, "Sky Pillar"), (15, "Pacifidlog")],
         "Sky Pillar": [(18, "Route 131")],
         "Pacifidlog": [(15, "Route 131"), (21, "Route 132")],
         "Route 132": [(21, "Pacifidlog"), (18, "Route 133")],
         "Route 133": [(18, "Route 132"), (24, "Route 134")],
         "Route 134": [(24, "Route 133"), (27, "Slateport")]}


#Functions
def hijkstra(G,s):
    '''return dictionary of lengths of the shortest distance to each node from s length to s is 0'''
    explored = {s}
    dist = {s:0}
    listy = []
    path = {s:[s]}
    for value in G[s]:
        listy.append((value[0], [s, value[1]]))
    heapify(listy)
    while len(explored) < len(G):
        short = heappop(listy)
        pathy = short[1]
        node = pathy[-1]
        if node in explored:
            continue
        else:
            explored.add(node)
            dist[node] = short[0]
            path[node] = pathy
            for edge in G[node]:
                if edge[1] not in explored:
                    newpathy = pathy + [edge[1]]
                    tuppy = (dist[node] + edge[0], newpathy)
                    heappush(listy,tuppy)
    return dist, path

def line_draw(route):
    routelines = []
    for i in range(1,len(route)):
        line = [str(route[i-1]),str(route[i])]
        sortline = sorted(line)
        linedict = f"{sortline[0]} {sortline[1]}"
        for connection in connections[linedict]:
            routelines.append(connection)
    for showline in routelines:
        pygame.draw.line(screen,(0,0,0),showline[0],showline[1],4)


#Button Class
class Button():
    def __init__(self, x, y, image, scale,name):
        self.name = name
        self.width = image.get_width()
        self.height = image.get_height()
        self.x = x
        self.y = y
        self.png = image
        self.image = pygame.transform.scale(image, (int(self.width * scale), int(self.height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x,self.y)
        self.clicked = False
    def draw(self):
        action = False
        screen.blit(self.image, (self.rect.x, self.rect.y))
        pos = pygame.mouse.get_pos() #Pos is xy coordinate
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
        return action

    def rescale(self,scale):
        self.image = pygame.transform.scale(self.png, (int(self.width * scale), int(self.height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x-8,self.y-8)



#Window
screenwidth = 1650
screenheight = 950
screen = pygame.display.set_mode((screenwidth,screenheight)) #Makes window
pygame.display.set_caption("Poke Maps") #Sets tab name on window
clock = pygame.time.Clock()
map = pygame.image.load('Map.png')
title = pygame.font.SysFont('bahnschrift', 20).render("Pokemon ORAS Map",True,'black')
title_rect = title.get_rect(center=(screenwidth/2,50))

#Button Making
#start_button = Button(100,200,start_img, 0.5)
house_img = pygame.image.load('House.png').convert_alpha()
star_img = pygame.image.load('star.png').convert_alpha()
undo_img = pygame.image.load('Undo.png').convert_alpha()
buttons = []
for house in towns:
    housee = Button(towns[house][0],towns[house][1],house_img,0.1,house)
    buttons.append(housee)
for place in specials:
    placee = Button(specials[place][0],specials[place][1],star_img,0.015,place)
    buttons.append(placee)
undo = Button(1575,875,undo_img,0.1,"Undo")
def calc(begin,end,buttons):
    buttons.remove(end)
    if end.png == house_img:
        end.rescale(0.15)
    else:
        end.rescale(0.025)
    total_dist, path = hijkstra(graph,begin.name)

    run3 = True
    while run3:
        clock.tick(60)/1000
        screen.fill('white')
        screen.blit(map,(125,50))
        #Title text
        titletext = pygame.font.SysFont('bahnschrift', 50).render("Pokemon ORAS Map", True, 'black')
        title_rect = titletext.get_rect(center=(screenwidth / 2, 25))
        screen.blit(titletext, title_rect)
        #Estimated time
        esttime = pygame.font.SysFont('bahnschrift', 50).render(f"Estimated time of travel: {total_dist[end.name]} seconds", True, 'black')
        esttimerect = esttime.get_rect(center = (1100,850))
        screen.blit(esttime,esttimerect)
        #Directions
        directiontitle = pygame.font.SysFont('bahnschrift', 30).render("Directions",True,'black')
        directiontitlerect = directiontitle.get_rect(center=(62,50))
        screen.blit(directiontitle,directiontitlerect)
        actpath = path[end.name]
        for i in range(len(actpath)):
            directions = pygame.font.SysFont('bahnschrift',20).render(str(actpath[i]),True,'black')
            directionsrect = directions.get_rect(center=(62,100+35*i))
            screen.blit(directions,directionsrect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        for button in buttons:
            button.draw()
        begin.draw()
        end.draw()
        if undo.draw():
            buttons = []
            for house in towns:
                housee = Button(towns[house][0], towns[house][1], house_img, 0.1, house)
                buttons.append(housee)
            for place in specials:
                placee = Button(specials[place][0], specials[place][1], star_img, 0.015, place)
                buttons.append(placee)
            title(buttons)     #Reset selection
        line_draw(path[end.name])
        pygame.display.update()

def end_node(start,buttons):
    run2 = True
    buttons.remove(start)
    if start.png == house_img:
        start.rescale(0.15)
    else:
        start.rescale(0.025)
    while run2:
        clock.tick(60)/1000
        screen.fill('white')
        screen.blit(map, (125,50))
        titletext = pygame.font.SysFont('bahnschrift', 50).render("Pokemon ORAS Map", True, 'black')
        title_rect = titletext.get_rect(center=(screenwidth / 2, 25))
        screen.blit(titletext, title_rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        #if pygame.mouse.get_pressed()[0] == 1:
            #print(pygame.mouse.get_pos())
        start.draw()
        for button in buttons:
            if button.draw():
                calc(start,button,buttons)
                #run2 = False
        pygame.display.update()
def title(buttons):
    run = True
    while run:
        clock.tick(60)/1000
        screen.fill('white')
        screen.blit(map, (125, 50))
        titletext = pygame.font.SysFont('bahnschrift', 50).render("Pokemon ORAS Map", True, 'black')
        title_rect = titletext.get_rect(center=(screenwidth / 2, 25))
        screen.blit(titletext, title_rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        if pygame.mouse.get_pressed()[0] == 1:
            print(pygame.mouse.get_pos())
        for button in buttons:
            if button.draw():
                end_node(button,buttons)
        pygame.display.update()

title(buttons)
