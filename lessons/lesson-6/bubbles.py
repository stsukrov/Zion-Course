# В первую очередь располагается импорты
# для этого соответствующая библиотека должна быть установлена в системе
# На текущий момент нам требуется две библиотеки pyglet, random
# random - является стандартной библиотекой в поставке питона
# чтобы установить pyglet необходимо вызвать следующую комманду (один раз)
# python -m pip install pyglet
import pyglet
from pyglet import shapes
import random


# две вспомогательные переменные определяющие размер экрана
FIELDWIDTH = 400
FIELDHEIGHT = 200

# с помощью библиотеки pyglet создаем новое пока пустое окно заданных размеров
# с названием Bubbles
window = pyglet.window.Window(FIELDWIDTH, FIELDHEIGHT, 'Bubbles')

# Инициализируем пустой список пузырьков
bubbles = []

# @ - обозначает аннотацию в данном случае аннотация говорит, что функция on_draw
# будет вызываться каждый раз когда система решить отрисовать наше созданное окно.
@window.event
def on_draw():
    # сначала мы наше окно чистим
    window.clear()
    # теперь проходимся по всем пузырькам и отрисовываем их
    # каждый пузырек это тупель (кортеж: координата x, координата y, радиус и 
    # цвет (задается тройкой Красный, Зеленый, Синий;
    # каждый канал может принимать значения от 0 до 255))
    for x, y, r, color in bubbles:
        # пузырек это шарик
        arc = shapes.Arc(x, y, r, color=color)
        # рисуем наш шарик
        arc.draw()

# это наша анимационная функция, она отвечает за изменение анимации нашей системы
# эту функцию мы вызываем ниже с частотой 24 кадра в секунду
def update(dt):
    global bubbles
    # проверяем, если на экране слишком мало пузырьков (<10) добавляем один
    if len(bubbles)<10:
        # append - добавляет новый элемент
        # элемент это тупель (кортеж) из 4 значений
        # random.randrange(0, FIELDWIDTH) - x координата, любое значение от 0 до ширины нашего окна
        # 0 - y координата, пузырек появляется всегда внизу окна
        # 3 - радиус, пузырек маленький
        # (random.randrange(0, 255), random.randrange(0, 255), 255)) - случайный оттенок синего
        bubbles.append((random.randrange(0, FIELDWIDTH), 0, 3, (random.randrange(0, 255), random.randrange(0, 255), 255)))
    # оставляем в обработке только пузырьки которые еще недостигли верха экрана y < FIELDHEIGHT
    # у каждого пузырька изменяем его y координату на 1
    bubbles = [(x, y+1, r, color) for x, y, r, color in bubbles if y < FIELDHEIGHT]

# говорим, что функцию update надо вызывать 24 раза в секунду
pyglet.clock.schedule_interval(update, 1.0/24.0)
# запускаем нашу программу
pyglet.app.run()

# чтобы запустить программу нужно вызвать python bubbles.py из деректории где лежить этот файл.