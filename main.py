from PySide6.QtWidgets import QApplication, QLabel, QWidget,QVBoxLayout
from PySide6.QtGui import QMovie
from PySide6.QtCore import Qt, QSize, QPropertyAnimation, QPoint, QElapsedTimer, QTimer
import sys
import random

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.hoverTime = QElapsedTimer()
        self.hovering=False
        self.checkTimer = QTimer(self)
        self.checkTimer.setInterval(100)
        self.checkTimer.timeout.connect(self.checkSleeping)

        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setAttribute(Qt.WA_Hover)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setFixedSize(QSize(90,80))
        self.setMouseTracking(True)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        self.label = QLabel(self)
        layout.addWidget(self.label)
        self.label.setScaledContents(True)

        self.bunny_run = QMovie('gifs/BunnyRun.gif')
        self.bunny_sleep = QMovie("gifs/BunnySleep.gif")
        self.bunny_sit = QMovie("gifs/BunnySitting.gif")
        self.bunny_liedown = QMovie('gifs/BunnyLieDown.gif')
        self.bunny_idle = QMovie("gifs/BunnyIdle.gif")
        self.bunny_run_flipped = QMovie("gifs/BunnyRun_flipped.gif")

        self.label.setMovie(self.bunny_run)
        self.bunny_run.start()

        self.animation = QPropertyAnimation(self, b"pos")
        self.animation.setDuration(5000)
        self.animation.finished.connect(self.run)

        self.run()

    def enterEvent(self, event):
        self.hoverTime.start()
        self.hovering = True
        self.show_bunny(self.bunny_liedown)
        self.animation.stop()
        self.checkTimer.start()
        
    def leaveEvent(self, event):
        self.hovering = False
        self.checkTimer.stop()
        self.run()

    def checkSleeping(self):
        if not self.hovering:
            return
        if self.hoverTime.elapsed() > 5000:
            self.show_bunny(self.bunny_sleep)
            self.checkTimer.stop()
            

    def show_bunny(self,movie):
        if self.label.movie() != movie:
            self.label.setMovie(movie)
            movie.start()

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
            self.label.setMovie(self.bunny_run_flipped)
            self.bunny_run_flipped.start()
        else:
            self.label.setMovie(self.bunny_run)
            self.bunny_run.start()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec()