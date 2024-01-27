import cv2

class Record:
    def __init__(self, filename):
        self.filename = filename
        self.fourcc = cv2.VideoWriter_fourcc(*'XVID')
        self.out = cv2.VideoWriter(self.filename, self.fourcc, 20.0, (640, 480))

    def write(self, frame):
        self.out.write(frame)

    def close(self):
        self.out.release()

