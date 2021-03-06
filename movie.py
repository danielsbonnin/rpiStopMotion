import pickle
import globals
class Frame:
    img_file = ""
    x_dim = -1
    y_dim = -1
    section = -1
    filter = ""
    def __init__(self, file_name):
        self.img_file = file_name

""" Data and methods for a stop motion movie """
class Movie:
    def __init__(self, max_frames=globals.MAX_FRAMES, data_file=globals.DATA_FILE):
        self.load_data(data_file)
    
    capture_count = 0    # Total number of pictures taken
    frame_count = 0  # Number frames currently in movie
    cur_frame = 1    # Frame currently displayed
    frame_rate = 15
    preview_count = 1   #Number frames to loop in preview
    data_file = "data.p"    #filename of save file
    frames = []
    
    def load_data(self, the_data_file=data_file):
        """ load meta data from pickle file """
        try:
            with open( the_data_file, "rb") as df:
                data = pickle.load(df)
        except:
            print('Error with loading data file. Trying to save some fresh data')
            self.new_save_data(the_data_file)
            return
        self.frame_count = data['frame_count']
        self.cur_frame = data['cur_frame']
        self.frame_rate = data['frame_rate']
        self.preview_count = data['preview_count']
        self.frames = data['frames']
        
        if self.cur_frame > self.frame_count:
            self.cur_frame = self.frame_count
    
    def new_save_data(self, the_data_file=data_file):
        """ save meta data to pickle file """
        data = {
            'frame_count' : 0,
            'cur_frame' : 1,
            'frame_rate' : 20,
            'preview_count' : 1,
            'frames' : [Frame] * globals.MAX_FRAMES,
            'data_file' : the_data_file
            }
        try:
            pickle.dump( data, open( the_data_file, "wb+" ))
        except Exception as e:
            print('Error saving data file{}: {}'.format(the_data_file, e))
    def save_data(self, the_data_file=data_file):
        """ save meta data to pickle file """
        data = {
            'frame_count' : self.frame_count,
            'cur_frame' : self.cur_frame,
            'frame_rate' : self.frame_rate,
            'preview_count' : self.preview_count,
            'frames' : self.frames,
            'data_file' : the_data_file
            }
        try:
            with open( the_data_file, 'wb+' ) as theDataFile:
                pickle.dump( data, theDataFile)
        except Exception as e:
            print('Error saving data file{}: {}'.format(the_data_file, e))
    
    def get_filename_by_frame_no(self, frameNo):
        assert(frameNo <= self.frame_count and frameNo >= 0)
        if frameNo == 0:
            return "image.jpg"
        return self.frames[frameNo - 1].img_file

    def get_next_filename(self, capture_num=None):
        if capture_num is None:
            capture_num = self.capture_count
        return str(capture_num + 1) + '.jpg'
        
    def add_frame(self, filename=None):
        if not filename:
            filename = self.get_next_filename()
        self.capture_count += 1
        self.frames[self.frame_count] = Frame(filename)
        self.frame_count += 1
        self.cur_frame = self.frame_count
        self.save_data(self.data_file)
    
    def delete_frame(self, frameNo):
        """ Delete frame from self.frames. ** frameNo is 1-indexed ** """
        assert(frameNo > 0 and frameNo <= self.frame_count)
        for i in range(frameNo, self.frame_count, 1):
            self.frames[i - 1] = self.frames[i]
        if self.frame_count > 0:
            self.frame_count -= 1
        if self.cur_frame > 1:
            self.cur_frame -= 1
        self.save_data(self.data_file)
    
    def set_frame_rate(self, frame_rate):
        assert(frame_rate <= globals.MAX_FRAME_RATE and frame_rate > 0)
        self.frame_rate = frame_rate
        self.save_data()
        print('New frame_rate: {}'.format(str(frame_rate)))
        
    def set_preview_count(self, preview_count):
        assert(preview_count <= self.frame_count)
        self.preview_count = preview_count
        self.save_data()
    
    def set_cur_frame(self, frameNo):
        """ Set cur_frame """
        if (frameNo < 1) or (frameNo > self.frame_count):
            print('frameNo: {:d} out of bounds'.format(frameNo))
            return None
        self.cur_frame = frameNo
        return frameNo
        
    def toString(self):
        return ('capture_count: {}\nframe_count: {}\ncur_frame:{}\npreview_count: {}\ndata_file: {}\n'.format(
            str(self.capture_count), str(self.frame_count),str(self.cur_frame),
            str(self.preview_count), self.data_file))