import cv2


class Video:
    """Wrapper for cv2.VideoCapture, that provides convinient context manage,
    video frames iterator and video metadata.
    
    Note: Can't inherit directly from cv2.VideoCapture due to some OpenCV trickery -
    <Segmentation fault (core dumped)> in some cases without detailed exception description."""

    def __init__(self, *args, **kwargs):
        self.stream = cv2.VideoCapture(*args, **kwargs)

    @property
    def fps(self):
        return int(self.stream.get(cv2.CAP_PROP_FPS))

    @property
    def width(self):
        return int(self.stream.get(cv2.CAP_PROP_FRAME_WIDTH))

    @property
    def height(self):
        return int(self.stream.get(cv2.CAP_PROP_FRAME_HEIGHT))

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.stream.isOpened():
            self.stream.release()
        
        return True

    def frames(self):
        while True:
            success, frame = self.stream.read()

            if not success:
                return

            yield frame
