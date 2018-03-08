import random, pygame, sys

# Frame Height and Width 
Frame = [400,300]
flag = True

# Main list having 1 to 8 numbers and a blank string
main_list = [x for x in range(1,9)]
main_list.append(' ')

# copy of main list
shuffle = [x for x in main_list]

# List for Position of Text or Numbers to write/display
pos = [[20,10],[120,10],[220,10],[20,110],[120,110],[220,110],[20,210],[120,210],[220,210]]

# Draw rectangular box 
rectlist = [[0,0,99,99],[100,0,99,99],[200,0,99,99],[0,100,99,99],[100,100,99,99],[200,100,99,99],[0,200,99,99],[100,200,99,99],[200,200,99,99],[300,130,100,40]]

# Block or rectangle selected (Rectangle xmin,ymin,xmax,ymax)
block = []

# top-left and bottom-right co-ordinate for the rectangle
for i in range(1,4):
	l = []
	for j in range(3):
		l.append([j*100,(i*100)-100,(j+1)*100,i*100])

	block.extend(l)

def text(string,style="monospace",size=80,width=1,color=(255,140,0)):
    ''' Text for display it on the screen, as string cannot be '''
    pygame.font.init()
    myfont = pygame.font.SysFont(style, size)
    # render text
    label = myfont.render(string, size, color)
    return label

def new():
	""" New Game, Shuffle the list """
	global shuffle, flag
	flag = True
	random.shuffle(shuffle)

def draw():
	""" Main Draw 
		click the block, it will shift to blank block.
	"""
	global event, running, shuffle, flag
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				running = False

	if event.type == pygame.MOUSEBUTTONDOWN:
		mousepress = pygame.mouse.get_pos()

		if 300 < mousepress[0] < 400 and 130 < mousepress[1] < 160:
			new()

		for dimension in block:
			if dimension[0] < mousepress[0] < dimension[2] and dimension[1] < mousepress[1] < dimension[3]:
				blank = shuffle.index(' ')
				press = block.index(dimension)
				if (blank % 3, blank // 3) == (press % 3, (press+3) // 3) or (blank % 3, blank // 3) == (press % 3, (press-3) // 3) or (blank , blank // 3) == (press - 1, press // 3) or (blank , blank // 3) == (press + 1, press // 3): 
					shuffle[blank], shuffle[press] = shuffle[press], shuffle[blank]
	
	if main_list == shuffle:
		flag = False

	for i in range(len(rectlist)):
		pygame.draw.rect(screen, (255,255,0), rectlist[i])
	
	if flag:
		for i in range(9):
			screen.blit(text(str(shuffle[i])),pos[i])
	else:
		screen.blit(text(str('Win'),size=100),(40,90))

	screen.blit(text(str('New Game'),size=15),(320,135))

new()

pygame.init()
running = True
screen = pygame.display.set_mode(Frame)
clock = pygame.time.Clock()

if __name__ == "__main__":
	while running:
		draw()
		pygame.display.update()
		clock.tick(30)
		
	pygame.quit()
	sys.stdout.flush()
	sys.exit()