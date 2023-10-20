import unittest
from src.main import sum_of_depths, TreeNode

class TestSumOfDepths(unittest.TestCase):
    def test1(self):
        root = TreeNode(1)
        self.assertEqual(sum_of_depths(root), 0)

    def test2(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        self.assertEqual(sum_of_depths(root), 6)

    def test3(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.left.left = TreeNode(4)
        self.assertEqual(sum_of_depths(root), 6)

    def test4(self):
        self.assertEqual(sum_of_depths(None), 0)

