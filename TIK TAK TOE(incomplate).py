graph = [['1','2','3'],['4','5','6'],['7','8','9']]
def draw():
	print(graph[0])
	print(graph[1])
	print(graph[2])
draw()
print("THIS IS THE GRAPH. ENTER THE VALUE OF COLLUMN TO PLAY YOUR TURN. \n")
def X():
	x = int(input('Valur : '))
	if x == 1:
		graph[0][0] = 'X'
		draw()
		O()
	if x == 2:
		graph[0][1] = 'X'
		draw()
		O()
	if x == 3:
		graph[0][2] = 'X'
		draw()
		O()
	if x == 4:
		graph[1][0] = 'X'
		draw()
		O()
	if x == 5:
		graph[1][1] = 'X'
		draw()
		O()
	if x == 6:
		graph[1][2] = 'X'
		draw()
		O()
	if x == 7:
		graph[2][0] = 'X'
		draw()
		O()
	if x == 8:
		graph[2][1] = 'X'
		draw()
		O()
	if x == 9:
		graph[2][2] = 'X'
		draw()
		O()
def O():
	o = int(input('Valur : '))
	if 0 == 1:
		graph[0][0] = 'O'
		draw()
		X()
	if o == 2:
		graph[0][1] = 'O'
		draw()
		X()
	if o == 3:
		graph[0][2] = 'O'
		draw()
		X()
	if o == 4:
		graph[1][0] = 'O'
		draw()
		X()
	if o == 5:
		graph[1][1] = 'O'
		draw()
		X()
	if o == 6:
		graph[1][2] = 'O'
		draw()
		X()
	if o == 7:
		graph[2][0] = 'O'
		draw()
		X()
	if o == 8:
		graph[2][1] = 'O'
		draw()
		X()
	if o == 9:
		graph[2][2] = 'O'
		draw()
		X()

X()