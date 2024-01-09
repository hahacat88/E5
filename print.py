print('曾经有一段真挚的爱情摆在我眼前，')

print('我没有去珍惜等到失去了才后悔莫及。')

print('尘世间最痛苦的事莫过于此，')

print('如果上天能给我一个再来一次的机会，')

print('我希望能对那个女孩说我爱你，')

print('如果非要给这份爱加一个期限的话，')

print('我希望是一万年。')

print('')

print(' ***** *****')

print(' ******* *******')

print(' ******************')

print(' ****************')

print(' ************')

print(' ********')

print(' **')

画心 （color 颜色）

import turtle

def curvemove():

for i in range(200):

turtle.right(1)

turtle.forward(1)

turtle.color('red')

turtle.begin_fill()

turtle.left(140)

turtle.forward(111.65)

curvemove()

turtle.left(120)

curvemove()

turtle.forward(111.65)

turtle.end_fill()

turtle.penup()

turtle.goto(-40, -50)

turtle.pendown()

turtle.write('', font = ('SimHei', 15, 'bold'))

turtle.hideturtle()

画哆啦A梦

import turtle

# 创建哆啦A梦

doraemon = turtle.Turtle()

doraemon.speed(10)

def draw_eye_white_circle(x):

doraemon.goto(x, 80)

doraemon.pendown()

doraemon.color('black')

doraemon.begin_fill()

doraemon.circle(15)

doraemon.color('white')

doraemon.end_fill()

def draw_eye_black_circle(x):

doraemon.goto(x, 90)

doraemon.color('black')

doraemon.begin_fill()

doraemon.begin_fill()

doraemon.circle(6)

doraemon.end_fill()

doraemon.penup()

画花

import turtle as T

import random

import time

# 画樱花的躯干

def Tree(branch, t):

time.sleep(0.0005)

if branch > 3:

if 8 <= branch <= 12:

if random.randint(0, 2) == 0:

# 白色

t.color('snow')

else:

# 淡珊瑚色

t.color('lightcoral')

t.pensize(branch / 3)

elif branch < 8:

if random.randint(0, 1) == 0:

t.color('snow')

else:

t.color('lightcoral')

t.pensize(branch / 2)

else:

# 赭色

t.color('sienna')

t.pensize(branch / 10)

t.forward(branch)

a = 1.5 * random.random()

t.right(20 * a)

b = 1.5 * random.random()

Tree(branch - 10 * b, t)

t.left(40 * a)

Tree(branch - 10 * b, t)

t.right(20 * a)

t.up()

t.backward(branch)

t.down()

成绩趋势图

import pygal

line_chart = pygal.Line()

line_chart.title = '各科成绩趋势图'

line_chart.x_labels = map(str, range(1, 6))

line_chart.add('数学', [66, 58, 70, 72, 76, 78])

line_chart.add('语文', [88, 89, 90, 88, 86, 82])

line_chart.add('英语', [98, 99, 99, 96, 100, 98])

line_chart.render()

餐厅评分

import pygal

radar_chart = pygal.Radar()

radar_chart.title = '餐厅评分数据'

radar_chart.x_labels = ['味道', '卫生', '服务', '价格', '环境']

radar_chart.add('老王炸鸡', [9, 6, 6, 4, 7])

radar_chart.add('小明快餐', [7, 8, 9, 6, 8])

radar_chart.add('阿强烧烤', [10, 4, 6, 8, 4])

radar_chart.add('萌仔汉堡', [7, 6, 5, 4, 6])

radar_chart.add('萌仔1汉堡', [7, 6, 5, 4, 6])
