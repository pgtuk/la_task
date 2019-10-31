import random

import cv2


MAX_RECTANGLES = 4
COLORS = (
    (0, 0, 0),
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
)


def add_rectangles(frame, rectangles_count):
    """Adds random number of rectangles between 0 and <rectangles_count> on frame."""
    _frame = frame.copy()
    f_height, f_width, _ = frame.shape

    for i in range(rectangles_count):
        rectangle = _make_rectangle(f_width, f_height)
        cv2.rectangle(_frame, rectangle[0], rectangle[1], COLORS[i])
    
    return _frame


def to_jpeg(frame):
    return cv2.imencode('.jpg', frame)[1]


def rectangles_count():
    return random.randint(0, MAX_RECTANGLES)


def _make_rectangle(max_width, max_height):
    """Returns tuple with coordinates of two opposite rectangle vertices.
    Can return rectangle with 0 area.
    
    :max_width int:
    :max_height int:
    :return tuple(tuple(int, int), tuple(int, int)): """
    return (
        # start vertex
        random.randint(0, max_width), random.randint(0, max_height)
    ), (
        # opposite vertex
        random.randint(0, max_width), random.randint(0, max_height)
    )
