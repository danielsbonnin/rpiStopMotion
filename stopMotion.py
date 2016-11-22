import sys

 # This gets the Qt stuff
import PyQt5
from PyQt5.QtWidgets import *
import json
# This is our window from QtCreator
import mainwindow
import movie
import globals
# Only use picamera modules on the rpi
class StubCamera():
    name = "name"
    def capture(self, name='image.jpg'):
        print('stubcapture')
        try:
            from shutil import copyfile
            copyfile('image.jpg', name)
        except Exception as e:
            print('{}'.format(e))
        print('Img copied to {}'.format(name))
if sys.platform == "linux":
    IS_RPI = True
    import picamera

else:
    IS_RPI = False


    
data = {}



# create class for our Raspberry Pi GUI
class MainWindow(QMainWindow, mainwindow.Ui_MainWindow):
    movie = movie.Movie()
    camera = None
    num_dial_notches = 0
    playing = False
    def scroll(self, value):
        old_value = (self.movie.cur_frame - 1) % self.num_dial_notches
        if value in [(old_value - 1), (old_value + self.num_dial_notches - 1)] and\
            (self.movie.cur_frame > 1):
            self.movie.cur_frame -= 1
        elif value in [(old_value + 1), (old_value - 9)] and\
            self.movie.cur_frame < self.movie.frame_count:
            self.movie.cur_frame += 1
        self.updateUI()
        print('dial value: {} old cur_frame mod 10: {} new cur_frame: {}'.format(str(value), str(old_value), str(self.movie.cur_frame)))
    def updateUI(self):
        self.numFrames.setText(str(self.movie.frame_count))
        self.currentFrame.setText(str(self.movie.cur_frame))
        self.frameRateSpinBox.setValue(self.movie.frame_rate)
        self.numFramesSpinBox.setMaximum(self.movie.cur_frame)
        if self.movie.preview_count <= self.movie.cur_frame:
            self.numFramesSpinBox.setValue(self.movie.preview_count)
        self.dial.setValue(self.movie.cur_frame % self.num_dial_notches + 1)
        self.show_image(self.movie.get_filename_by_frame_no(self.movie.cur_frame))
    def show_image(self, filename):
        img = PyQt5.QtGui.QPixmap(filename)
        self.imageView.setPixmap(img)
    def captureButtonPressed(self):
        
        print("captureButtonPressed")
        try:
            filename = self.movie.get_next_filename()
        except:
            print('get_next_filename() had a problem')
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
    
    def deleteButtonPressed(self):
        print('delete button pressed')
        self.movie.delete_frame(self.movie.cur_frame)
        self.updateUI()
    
    def frameRateChanged(self, value):
        self.movie.set_frame_rate(value)
    
    def numPlaybackFramesChanged(self, value):
        self.movie.set_preview_count(value)
    
    def playPreview(self):
        from time import sleep
        
        self.playing = not self.playing
        if self.playing == True:
            self.playButton.setText('Stop')
        else:
            self.playButton.setText('Play')
        while self.playing:
            for i in range(1, self.movie.preview_count + 1):
                self.currentFrame.setText(str(i))
                sleep(1 / self.movie.frame_rate)
                QApplication.processEvents()
    # access variables inside of the UI's file
    def __init__(self):
        super(self.__class__, self).__init__()
        self.num_dial_notches = globals.NUM_DIAL_NOTCHES
        self.setupUi(self) # gets defined in the UI file
        self.movie = movie.Movie()
        
        self.updateUI()
        if IS_RPI:
            self.camera = picamera.PiCamera()
        else:
            self.camera = StubCamera()
        self.captureButton.clicked.connect(lambda: self.captureButtonPressed())
        self.deleteButton.clicked.connect(lambda: self.deleteButtonPressed())
        self.dial.valueChanged.connect(lambda: self.scroll(self.dial.value()))
        self.frameRateSpinBox.valueChanged.connect(
            lambda: self.frameRateChanged(self.frameRateSpinBox.value()))
        self.numFramesSpinBox.valueChanged.connect(
            lambda: self.numPlaybackFramesChanged(self.numFramesSpinBox.value()))
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
