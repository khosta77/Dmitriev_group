import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from scipy import signal
from pynput import keyboard

# Создаем 3д пространство
fig = plt.figure(figsize = (8,8))
ax = plt.axes(projection = '3d')

# Creating Dataset
#X = np.linspace(-100, 100, 51)

i = 0
j = 0
k = 0

X = np.array([-4, -3, -3, -3, -3, 5, -3, -3, -4, -3, 5, -3, -4])
Y = np.array([ 0, -2,  2,  2, -2, 0, -2, -2,  0,  2, 0,  2,  0])
Z = np.array([ 0,  2,  2, -2, -2, 0,  2, -2,  0, -2, 0,  2,  0])

x, y, z = X, Y, Z

mrk_move = 0
#ax.plot3D(x, a)

def on_press(key):
    try:
        global i, j, k, x, y, z, X, Y, Z, mrk_move          вЖц

        pushed_key = key.char
        # Перемещение
        if pushed_key == "w":
            i += 0.1
            print(f'\nУгол i = {i}')
        if pushed_key == "s":
            i -= 0.1
            print(f'\nУгол i = {i}')
        if pushed_key == "a":
            j += 0.1
            print(f'\nУгол j = {j}')
        if pushed_key == "d":
            j -= 0.1
            print(f'\nУгол j = {j}')
        if pushed_key == "q":
            k += 0.1
            print(f'\nУгол k = {k}')
        if pushed_key == "e":
            k -= 0.1
            print(f'\nУгол k = {k}')
        # Настройка
        if pushed_key == "r":
            x, y, z = X, Y, Z
            print(f'\nСброс координат')
        if pushed_key == "m":
            mrk_move = 1
            print(f'\nРежим движения {mrk_move}')
        if pushed_key == "n":
            mrk_move = 0
            print(f'\nРежим движения {mrk_move}')
    except AttributeError:
        pass
        #print('special key {0} pressed'.format(key))

def on_release(key):
    #print('{0} released'.format(key))
    if key == keyboard.Key.esc:
        print('Выход из программы')
        return False

listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()

phi = 0.7

def rotationX(x, y, z, p):
    _x = x
    _y = y * np.cos(p) + z * np.sin(p)
    _z = -y * np.sin(p) + z * np.cos(p)
    return _x, _y, _z

def rotationY(x, y, z, p):
    _x = x * np.cos(p) + z * np.sin(p)
    _y = y
    _z = -x * np.sin(p) + z * np.cos(p)
    return _x, _y, _z

def rotationZ(x, y, z, p):
    _x = x * np.cos(p) + y * np.sin(p)
    _y = -x * np.sin(p) + y * np.cos(p)
    _z = z
    return _x, _y, _z



while True:
    x, y, z = rotationX(x, y, z, i)
    i = 0
    x, y, z = rotationY(x, y, z, j)
    j = 0
    x, y, z = rotationZ(x, y, z, k)
    k = 0

    ax.cla()
    ax.plot3D(x, y, z)
    ax.set_xlim3d(left=-10, right=10)
    ax.set_ylim3d(bottom=-10, top=10)
    ax.set_zlim3d(bottom=-10, top=10)

    plt.draw()
    plt.pause(.001)

plt.show()
