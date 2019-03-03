COLOR_BLACK  = 0
COLOR_RED    = 1
COLOR_GREEN  = 2
COLOR_YELLOW = 3
COLOR_BLUE   = 4
COLOR_MAGENTA= 5
COLOR_CYAN   = 6
COLOR_WHITE  = 7

ATTR_NORMAL   = 0
ATTR_BOLD     = 1
ATTR_UNDERLINE= 4
ATTR_BLINK    = 5
ATTR_REVRESE  = 7
ATTR_INVISIBLE= 8

DIRECTIONS = {
	"up": 1,
	"down": 2,
	"right": 3,
	"left": 4
}

SCREEN_40x25_BLACK_WHITE = '40x25 b/w'
SCREEN_40x25_COLOR       = '40x25 color'
SCREEN_80x25_BLACK_WHITE = '80x25 b/w'
SCREEN_80x25_COLOR       = '80x25 color'
SCREEN_320x200_


def resetScreen():
	"""
	Resets the current terminal by using
	ESC[0m (change colors back to default) and
	ESC[2J (clear the screen)
	"""
	print('\x1b[0m\x1b[2J')

def setColors(foreground, background, attr=ATTR_NORMAL):
	"""
	Sets the terminal colors by printing
	ESC[ {FOREGROUND+30};{ATTR}m - sets the f/g color and
	ESC[ {BACKGROUND+40};{ATTR}m - sets the b/g color
	"""
	print('\x1b[' + str(40 + background) + ';' + str(attr) + 'm' +
		  '\x1b[' + str(30 + foreground) + ';' + str(attr) + 'm')

def clearScreen():
	"""Clears the terminal screen"""
	print('\x1b[2J')

def moveCursorTo(x, y):
	print('\x1b[' + str(x) + ';' + str(y) + 'H')

def moveCursor(points, direction):
	dir = ''
	if direction == DIRECTIONS['up']:
		dir = 'A'
	elif direction == DIRECTIONS['down']:
		dir = 'B'
	elif direction == DIRECTIONS['right']:
		dir = 'C'
	elif direction == DIRECTIONS['left']:
		dir = 'D'
	else:
		return

	print('\x1b[' + str(points) + dir)

def saveCursorPos():
	print('\x1b[s')
def restoreCursorPos():
	print('\x1b[u')

def clearLine():
	print('\x1b[K')

def screenMode(mode):
