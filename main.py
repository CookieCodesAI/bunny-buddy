from PySide6.QtWidgets import QApplication, QLabel, QWidget,QVBoxLayout
from PySide6.QtGui import QMovie
from PySide6.QtCore import Qt, QSize, QPropertyAnimation, QPoint
import sys
import random

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setFixedSize(QSize(80,75))

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        self.label = QLabel(self)
        layout.addWidget(self.label)
        self.label.setScaledContents(True)

        self.bunny = QMovie('gifs/BunnyRun.gif')
        self.label.setMovie(self.bunny)
        self.bunny.start()

        self.animation = QPropertyAnimation(self, b"pos")
        self.animation.setDuration(5000)
        self.animation.finished.connect(self.run)

        self.run()

    def run(self):
        x_start = self.x()
        y_start= self.y()
        x_end = random.randint(100,800)
        y_end = random.randint(100,800)
        self.animation.setStartValue(QPoint(x_start,y_start))
        self.animation.setEndValue(QPoint(x_end,y_end))
        self.animation.setLoopCount(1)
        self.animation.start()
        if (x_end-x_start<0):
            self.bunny.stop()
            self.bunny = QMovie("gifs/BunnyRun_flipped.gif")
            self.label.setMovie(self.bunny)
            self.bunny.start()
        else:
            self.bunny.stop()
            self.bunny = QMovie("gifs/BunnyRun.gif")
            self.label.setMovie(self.bunny)
            self.bunny.start()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec()