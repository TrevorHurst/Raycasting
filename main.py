import turtle, random, math
class Boundary:
    def __init__(s,x1,y1,x2,y2):
        s.x1 = x1
        s.x2 = x2
        s.y1 = y1
        s.y2 = y2
    def show(s):
        line(s.x1,s.y1,s.x2,s.y2)

class Ray:
    def __init__(s,pos,angle):
        s.x = pos[0]
        s.y = pos[1]
        s.dir = [math.cos(angle),math.sin(angle)]
    def show(s):
        s.x1 = s.x+s.dir[0]
        s.y1 = s.y+s.dir[1]
        line(s.x,s.y,s.x1,s.y1)
    def cast(s,wall):
        x1 = wall.x1
        y1 = wall.y1
        x2 = wall.x2
        y2 = wall.y2
        
        x3 = s.x
        y3 = s.y
        x4 = s.x + s.dir[0]
        y4 = s.y + s.dir[1]

        den = (x1-x2)*(y3-y4)-(y1-y2)*(x3-x4)
        if den == 0:
            return
        t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den
        u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / den
        if 1 >= t and t>=0 and u > 0:
            pt = []
            pt.append(x1 + t * (x2 - x1))
            pt.append(y1 + t * (y2 - y1))
            return pt
        else:
            return

class Particle:
    def __init__(s):
        s.pos = [0,0]
        s.rays = []
        for i in range(0,360,3):
            s.rays.append(Ray(s.pos,math.radians(i)))
    def show(s):
        ellipse(s.pos[0],s.pos[1],4)
    def look(s,walls):
        for ray in s.rays:
            ray.x = s.pos[0]
            ray.y = s.pos[1]
            closest = False
            record = float('inf')
            for wall in walls:
                pt = ray.cast(wall)
                if pt:
                    d = distance(s.pos,pt)
                    if d < record:
                        record = d
                        closest = pt
            if closest:
                line(s.pos[0],s.pos[1],closest[0],closest[1])
    def goto(s,x,y):
        s.pos[0] = x
        s.pos[1] = y
def distance(a,b):
    x1,y1 = a
    x2,y2 = b
    return math.sqrt(((x2-x1)**2+(y2-y1)**2))
def ellipse(x,y,r):
    turtle.pu()
    turtle.goto(x,y-r)
    turtle.pd()
    turtle.circle(r)

def line(x1,y1,x2,y2,color='black'):
    turtle.pu()
    turtle.color(color)
    turtle.goto(x1,y1)
    turtle.pd()
    turtle.goto(x2,y2)

bounds = []
w = 400
h = 200
for i in range(5):
    bpos = [random.randint(-w,w), random.randint(-h,h), random.randint(-w,w), random.randint(-h,h)]
    bounds.append(Boundary(bpos[0],bpos[1],bpos[2],bpos[3]))

bounds.append(Boundary(-w,h,-w,-h))
bounds.append(Boundary(w,h,w,-h))
bounds.append(Boundary(-w,h,w,h))
bounds.append(Boundary(w,-h,-w,-h))
particle = Particle()
screen = turtle.Screen()

def update(x,y):
    turtle.clear()
    turtle.tracer(0,0)
    turtle.ht()
    for bound in bounds:
        bound.show()
    particle.goto(x,y)
    particle.look(bounds)
    particle.show()
    turtle.update()

update(0,0)
while True:
    screen.onclick(update)
    