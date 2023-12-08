import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from scipy import signal
from pynput import keyboard

def rotationX(x, y, z, p):
    _x = x
    _y = (y - y[0]) * np.cos(p) + (z - z[0]) * np.sin(p) + y[0]
    _z = (z - z[0]) * np.cos(p) - (y - y[0]) * np.sin(p) + z[0]
    return _x, _y, _z

def rotationY(x, y, z, p):
    _x = (x - x[0]) * np.cos(p) + (z - z[0]) * np.sin(p) + x[0]
    _y = y
    _z = (z - z[0]) * np.cos(p) - (x - x[0]) * np.sin(p) + z[0]
    return _x, _y, _z

def rotationZ(x, y, z, p):
    _x = (x - x[0]) * np.cos(p) + (y - y[0]) * np.sin(p) + x[0]
    _y = (y - y[0]) * np.cos(p) - (x - x[0]) * np.sin(p) + y[0]
    _z = z
    return _x, _y, _z

def AircraftMovemonent(x, y, z):
    global SPEED, I, ai, J, aj, K, ak
    if ai >= 0.0 and aj >= 0.0 and ak >= 0.0 :
        _x = x - SPEED * np.cos(K)
    
    else:
        _x = x + SPEED * np.cos(K)

    if ak >= 0.0:
        _y = y + SPEED * np.sin(K)
    else:
        _y = y - SPEED * np.sin(K)

    #if aj 
    #_z = z + SPEED * np.sin(I) + SPEED * np.cos(J)
    
    return _x, _y, z

L_LOCK_ROLL   = -720.0 # Предел по левому углу крена
R_LOCK_ROLL   =  720.0
L_LOCK_PITCH  = -720.0 # Предел по левому углу тангажа
R_LOCK_PITCH  =  720.0
L_LOCK_YAWING = -720.0 # Предел по левому углу рыскания
R_LOCK_YAWING =  720.0
# Создаем 3д пространство
fig = plt.figure(figsize = (8,8))
ax = plt.axes(projection = '3d')

i = 0; I = 0; ai = 0  # Угол крена
j = 0; J = 0; aj = 0  # Угол тангажа
k = 0; K = 0; ak = 0  # Угод рыскания

X = np.array([-1, -5, -3, -3, -3, -3, 5, -3, -3, -5, -3, 5, -3, -5, -1, -1, 1,  1, -1, -1, 5, 5, 3,  3,  5, 5, 5, 3])
Y = np.array([ 0,  0, -2,  2,  2, -2, 0, -2, -2,  0,  2, 0,  2,  0,  0,  7, 7, -7, -7,  0, 0, 4, 4, -4, -4, 0, 0, 0])
Z = np.array([ 0,  0,  2,  2, -2, -2, 0,  2, -2,  0, -2, 0,  2,  0,  0,  0, 0,  0,  0,  0, 0, 0, 0,  0,  0, 0, 3, 0])
#X, Y, Z = rotationZ(X, Y, Z, ((90.0 * np.pi) / 180.0))
x, y, z = X, Y, Z

mrk_move = 0
SPEED = 0.5

def fRadianstDegrees():
    global ai, I, aj, J, ak, K
    ai = (I * 180.0) / np.pi
    aj = (J * 180.0) / np.pi
    ak = (K * 180.0) / np.pi

def on_press(key):
    try:
        DEFLECTION_ANGLE = 0.1
        global i, j, k, I, J, K, x, y, z, X, Y, Z, mrk_move

        pushed_key = key.char
        # Перемещение
        if pushed_key == "d" and ai <= R_LOCK_ROLL:
            i += DEFLECTION_ANGLE
            I += DEFLECTION_ANGLE

        if pushed_key == "a" and ai >= L_LOCK_ROLL:
            i -= DEFLECTION_ANGLE
            I -= DEFLECTION_ANGLE

        if pushed_key == "w" and aj <= R_LOCK_PITCH:
            j += DEFLECTION_ANGLE
            J += DEFLECTION_ANGLE

        if pushed_key == "s" and aj >= L_LOCK_PITCH:
            j -= DEFLECTION_ANGLE
            J -= DEFLECTION_ANGLE

        if pushed_key == "q" and ak <= R_LOCK_YAWING:
            k -= DEFLECTION_ANGLE
            K -= DEFLECTION_ANGLE

        if pushed_key == "e" and ak >= L_LOCK_YAWING:
            k += DEFLECTION_ANGLE
            K += DEFLECTION_ANGLE
        fRadianstDegrees();

        if pushed_key == "c":
            #if pushed_key == "c" and (ak >= -22.5 and ak <= 22.5):
            #   x = x - SPEED
            x = x - SPEED * np.cos(((ak) * np.pi) / 180.0)
            y = y - SPEED * np.sin(((ak) * np.pi) / 180.0)
            z = z + SPEED * np.sin(J)

        if pushed_key == "x":
            x = x + SPEED * np.cos(K)
            y = y + SPEED * np.sin(K)
            z = z - SPEED * np.sin(J)

        # Настройка
        if pushed_key == "r":
            x, y, z = X, Y, Z
            I, J, K = 0, 0, 0
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



while True:

    print(f'\nУгол крена = {round(ai, 2)}\nУгол тангажа = {round(aj, 2)}\nУгол рыскания = {round(ak, 2)}\nКоординаты X = {x}')
    if ai >= L_LOCK_ROLL and ai <= R_LOCK_ROLL:
        x, y, z = rotationX(x, y, z, i)
        i = 0

    if aj >= L_LOCK_PITCH and aj <= R_LOCK_PITCH:
        x, y, z = rotationY(x, y, z, j)
        j = 0

    if ak >= L_LOCK_YAWING and ak <= R_LOCK_YAWING:
        x, y, z = rotationZ(x, y, z, k)
        k = 0

    x, y, z = AircraftMovemonent(x, y, z)

    ax.cla()
    ax.plot3D(x, y, z)
    ax.set_xlim3d(left=-100, right=100)
    ax.set_ylim3d(bottom=-100, top=100)
    ax.set_zlim3d(bottom=-100, top=100)

    plt.draw()
    plt.pause(.001)

plt.show()
