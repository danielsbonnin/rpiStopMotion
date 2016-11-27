""" testStopMotion.py """
import unittest
import stopMotion

class StopMotionTest(unittest.TestCase):
    def test_capture(self):
        ''' A new .jpg file exists with incremented name prefix '''
        pass

    def test_capture_handler(self):
        ''' increment frame count and current frame '''
        form = stopMotion.MainWindow()
        form.movie.capture_count = 100
        form.captureButtonPressed()
        self.assertEqual(101, form.movie.capture_count)
        self.assertTrue(os.path.exists('101.jpg'))
        form.destroy()
        
        pass
    
    def test_delete(self):
        ''' frame is removed from movie, associated img is deleted from disk '''
        pass

    def test_delete_handler(self):
        ''' decrement frame count and current frame '''
        pass
    
    def test_increment_cur_frame(self):
        ''' cur frame should increment unless >= num_frames '''
        pass
    
    def test_decrement_cur_frame(self):
        ''' cur frame should decrement unless <=1 '''
        pass
    
    def test_set_speed_slow(self):
        ''' frame rate should be set to FPS_SLOW '''
        pass
    
    def test_set_speed_med(self):
        ''' frame rate should be set to FPS_MED '''
        pass
    
    def test_set_speed_fast(self):
        ''' frame rate should be set to FPS_FAST '''
        pass
        

    
if __name__ == '__main__':
    unittest.main()
        
    