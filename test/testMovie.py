''' testMovie.py '''
import unittest
import movie
import pickle

def exampleMovie():
    testMovie = movie.Movie()
    testMovie.capture_count = 100
    testMovie.frame_count = 0
    testMovie.cur_frame = 1
    testMovie.preview_count = 20
    testMovie.data_file = "testData.p"
    return testMovie
class movieTest(unittest.TestCase):
    
    def test_save_and_load_data(self):
        ''' values identical after loading from save file '''
        exMovie = exampleMovie();
        with open('testData.p', 'wb+') as testDataFile:
            testDataFile = pickle.dump(exMovie, testDataFile)
        
        with open('testData.p', 'rb') as testDataFile:
            r = pickle.load(testDataFile)
        self.assertEqual(exMovie.capture_count, r.capture_count)
        self.assertEqual(exMovie.frame_count, r.frame_count)
        self.assertEqual(exMovie.cur_frame, r.cur_frame)
        self.assertEqual(exMovie.preview_count, r.preview_count)
        self.assertEqual(exMovie.data_file, r.data_file)
        
    
    def test_add_frame(self):
        ''' frame_count and capture_count are incremented, 
            frame is in right idx,
        '''
        exMovie = exampleMovie()
        num_frames_to_add = 20
        for i in range(num_frames_to_add):
            exMovie.add_frame(str(i) + '.jpg')
        
        for i in range(num_frames_to_add):
            self.assertEqual(exMovie.frames[i].img_file, str(i) + '.jpg')
        self.assertEqual(exMovie.frame_count, num_frames_to_add)
        self.assertEqual(exMovie.cur_frame, num_frames_to_add)
        self.assertEqual(exMovie.capture_count, 100 + num_frames_to_add)

    def test_delete_frame(self):
        ''' frame is removed from correct idx, higher frames shifted down '''
        exMovie = exampleMovie()
        num_frames_to_add = 20
        for i in range(num_frames_to_add):
            exMovie.add_frame(str(i) + '.jpg')
        
        import random
        for i in range(num_frames_to_add):
            # delete_frame takes a 1-indexed frameNo, hence increment below.
            randFrame = random.randrange(1, num_frames_to_add + 1 - i)   
            exMovie.delete_frame(randFrame)
            self.assertEqual(exMovie.frame_count, num_frames_to_add - 1 - i)
    
    def test_get_next_filename(self):
        ''' returns <capture_num> + 1.jpg '''
        import random
        exMovie = exampleMovie()
        num_iters = 20
        
        # with default parameter
        for i in range(num_iters):
            current_capture_count = random.randint(0, 100)
            exMovie.capture_count = current_capture_count
            nextFN = exMovie.get_next_filename()
            self.assertEqual(str(current_capture_count + 1) + '.jpg', nextFN)
        
        # with explicit parameter
        exMovie.capture_count = 100
        for i in range(num_iters):
            current_capture_count = random.randint(0, 100)
            nextFN = exMovie.get_next_filename(current_capture_count)
            self.assertEqual(str(current_capture_count + 1) + '.jpg', nextFN)

    def test_set_frame_rate(self):
        ''' new frame rate is correct '''
        pass
    
    def test_set_preview_count(self):
        ''' new preview_count is correct '''
        pass
    
if __name__ == '__main__':
    unittest.main()

