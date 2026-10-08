FLAG_WHITE = "\x1b[48;5;15m"
FLAG_RED = "\x1b[48;5;160m"

END = '\u001b[0m'

### Poland Flag
for i in range(6):
    if i < 3:
        print(f'{FLAG_WHITE}{" " * 30}{END}')
    else:
        print(f'{FLAG_RED}{" " * 30}{END}')

print('\n')

### Pattern d type
PATTERN_HEIGHT = 5
PATTERN_WIDTH = 9

PATTERN_WIDTH_MULT = 3

PATTERN_WHITE = '\033[47m'
PATTERN_BLACK = '\033[40m'

def printWhite(width: int):
    return f'{PATTERN_WHITE}{" " * width * PATTERN_WIDTH_MULT}'

def printBlack(width: int):
    return f'{PATTERN_BLACK}{" " * width * PATTERN_WIDTH_MULT}'

blackLine = printBlack(PATTERN_WIDTH) + END
evenLine = printWhite(4) + printBlack(1) + printWhite(4) + END
oddLine = printWhite(1) + printBlack(1) + printWhite(5) + printBlack(1) + printWhite(1) + END


for i in range(PATTERN_HEIGHT):
    if not (i % 2):
        print(blackLine)
    else:
        if not (i // 2) % 2:
            print(evenLine)
        else:
            print(oddLine)

print('\n')

### Func y=x^(0.5)
FUNC_HEIGHT = 8
FUNC_WIDTH = 25

FUNC_WHITE = '\033[47m'
FUNC_BLACK = '\033[40m'

for i in range(FUNC_HEIGHT):
    arr = []
    
    for j in range(FUNC_WIDTH):
        y = FUNC_HEIGHT - i - 1
        isVertical = ((y ** 2) >= j) & ((y ** 2 )<= (i + 1))
        isHorisontal = (j ** (1/2) >= y) & (j ** (1/2) <= (y + 1))
        if (isHorisontal | isVertical):
            arr.append(printBlack(1))
        else:
            arr.append(printWhite(1))
    
    print(''.join(arr) + END)