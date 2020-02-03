from unittest import TestCase, main
from app.core.fibonacci import calculate_sequence

class TestCalculateSequence(TestCase):
    def test_limit_lt_0(self):
        self.assertRaises(ValueError, calculate_sequence, -1)
    
    def test_limit_gt_0(self):
        self.assertListEqual(calculate_sequence(0), [])
        self.assertListEqual(calculate_sequence(1), [0])
        self.assertListEqual(calculate_sequence(2), [0, 1])
        self.assertListEqual(calculate_sequence(3), [0, 1, 1])
        self.assertListEqual(calculate_sequence(4), [0, 1, 1, 2])
        self.assertListEqual(calculate_sequence(5), [0, 1, 1, 2, 3])
        self.assertListEqual(calculate_sequence(10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])

if __name__ == "__main__":            
    main()
