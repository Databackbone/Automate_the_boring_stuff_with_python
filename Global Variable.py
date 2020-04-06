

door = 'Weis' #global variable

def door_paint():
    global door #if you want to change the global variable this is necessary
    door = 'pink'
def local_scope():
    door = 'lila'
    print(door)

door_paint()
print(door)
local_scope()
