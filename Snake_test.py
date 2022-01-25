import Snake
from unittest.mock import patch
import pygame
import unittest

class Snaketests(unittest.TestCase):

@patch('pygame.ket.get_pressed')
    def test_exit_Snake(self,test_patch):

        test_patch.return.value = {pygame.K_ESCAPE : True}
        with self.assertRaises(SystemExit) as exit:
            Snake.maim()
        self.assertEqual(exit.exception.code, 1)






if __name__ == "__main__":
    unittest.main()