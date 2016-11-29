import sys

 # This gets the Qt stuff
import PyQt5
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import *
import json
import stopMotion
# This is our window from QtCreator
from mainwindow import Ui_MainWindow
import movie
import globals
# Only use picamera modules on the rpi
class StubCamera():
    name = "name"
    brightness = 50
    def capture(self, name='image.jpg'):
        print('stubcapture')
        try:
            from shutil import copyfile
            copyfile('image.jpg', name)
        except Exception as e:
            print('{}'.format(e))
        print('Img copied to {}'.format(name))
    
    def start_preview(self):
        print('started preview')
    def stop_preview(self):
        print('stopped preview')
if sys.platform == "linux":
    IS_RPI = True
    from picamera import PiCamera

else:
    IS_RPI = False
data = {}

# create class for our Raspberry Pi GUI
class MainWindow(QMainWindow, Ui_MainWindow):
    movie = movie.Movie()
    camera = None
    num_dial_notches = 0
    playing = False
    in_capture_loop = False

    def currentFrameChanged(self, value):
        if self.movie.set_cur_frame(value):
            self.currentFrame.setStyleSheet("color: black;")
            self.updateUI()
        else:
            self.currentFrame.setStyleSheet("color: red;")
    def updateUI(self):
        self.numFrames.setText(str(self.movie.frame_count))
        self.show_image(self.movie.get_filename_by_frame_no(self.movie.cur_frame))
        self.brightnessSlider.setValue(self.camera.brightness)
    def show_image(self, filename):
        img = PyQt5.QtGui.QPixmap(filename)
        self.imageView.setPixmap(img)
    
    def previewImage(self):
        import time
        self.in_capture_loop = True
        self.camera.start_preview(fullscreen=False, window=(0,0,500,500))

    def captureButtonPressed(self):
        import time
        self.camera.stop_preview()
        filename = self.movie.get_next_filename()
        
        try:
            self.camera.capture(filename)
        except:
            print('camera.capture({}) had a problem'.format(filename))
            return
        try:
            self.movie.add_frame(filename)
        except Exception as e:
            print('add_frame had a problem: {}'.format(e))
        print('Frame {} added'.format(filename))
        self.show_image(filename)
        self.updateUI()
        time.sleep(1)
        if self.in_capture_loop == True:
            self.camera.start_preview()

    def deleteButtonPressed(self):
        print('delete button pressed')
        self.movie.delete_frame(self.movie.cur_frame)
        self.updateUI()
    
    def frameRateChanged(self, value):
        self.movie.set_frame_rate(value)
        print('frame rate changed to {}'.format(value))

    def numPlaybackFramesChanged(self, value):
        self.movie.set_preview_count(value)
        
    def speedState(self, radio):
        """ Handle a radio button event """
        if radio.text() == "slow" and radio.isChecked() == True:
            self.frameRateChanged(5)
        elif radio.text() == "medium" and radio.isChecked() == True:
            self.frameRateChanged(15)
        else:
            self.frameRateChanged(30)
 
    def playPreview(self):
        from time import sleep
        self.movie.preview_count = self.movie.frame_count
        self.playing = not self.playing
        if self.playing == True:
            self.playButton.setText('Stop')
        else:
            self.playButton.setText('Play')
        while self.playing:
            for i in range(1, self.movie.preview_count + 1):
                self.currentFrame.setValue(i)
                self.show_image(self.movie.get_filename_by_frame_no(i))  
                self.currentFrame.setValue(i)
                sleep(1 / self.movie.frame_rate)
                QApplication.processEvents()
    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Space:
            print('space key')
            self.captureButtonPressed()
        elif e.key() == QtCore.Qt.Key_Escape:
            print('escape key')
            if self.in_capture_loop == True:
                self.in_capture_loop = False
                self.camera.stop_preview()
            else:
                self.close()
    def updateCamera(self):
        """ Update camera settings """
        import time
        self.camera.brightness = self.brightnessSlider.value()
        time.sleep(2)
        
    # access variables inside of the UI's file
    def __init__(self):
        super(self.__class__, self).__init__()
        self.num_dial_notches = globals.NUM_DIAL_NOTCHES
        
        self.movie = movie.Movie()
        self.setupUi(self) # gets defined in the UI file
        
        if IS_RPI:
            self.camera = PiCamera()
        else:
            self.camera = StubCamera()
        self.updateUI()
        self.captureButton.clicked.connect(lambda: self.previewImage())
        
        self.deleteButton.clicked.connect(lambda: self.deleteButtonPressed())
        self.currentFrame.valueChanged.connect(lambda: self.currentFrameChanged(self.currentFrame.value()))
        self.fullRadio.toggled.connect(
            lambda: self.speedState(self.fullRadio))
        self.mediumRadio.toggled.connect(
            lambda: self.speedState(self.mediumRadio))
        self.slowRadio.toggled.connect(
            lambda: self.speedState(self.slowRadio))
        self.applyButton.clicked.connect(lambda: self.updateCamera())
        
        self.playButton.clicked.connect(lambda: self.playPreview())
def main():
 
    # a new app instance
    app = QApplication(sys.argv)
    
    form = MainWindow()
    form.show()
    sys.exit(app.exec_())
                           
# python bit to figure how who started This
if __name__ == "__main__":
    main()
