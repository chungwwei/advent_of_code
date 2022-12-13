import unittest
import day_13

class Test(unittest.TestCase):

	def test_case_1(self):
		result = day_13.dfs([1,1,3,1,1], [1,1,5,1,1])
		expected = -1
		self.assertEqual(result, expected)


	def test_case_2(self):
		result = day_13.dfs([[1],[2,3,4]], [[1],4])
		expected = -1
		self.assertEqual(result, expected)


	def test_case_3(self):
		result = day_13.dfs([9], [[8, 7, 6]])
		expected = 1
		self.assertEqual(result, expected)
	

	def test_case_4(self):
		result = day_13.dfs([[4,4],4,4], [[4,4],4,4,4])
		expected = -1
		self.assertEqual(result, expected)


	def test_case_5(self):
		result = day_13.dfs([7, 7, 7, 7], [7, 7, 7])
		expected = 1
		self.assertEqual(result, expected)

	
	def test_case_6(self):
		result = day_13.dfs([], [3])
		expected = -1
		self.assertEqual(result, expected)
	

	def test_case_7(self):
		result = day_13.dfs([[[]]], [[]])
		expected = 1
		self.assertEqual(result, expected)

	
	def test_case_8(self):
		result = day_13.dfs([1,[2,[3,[4,[5,6,7]]]],8,9], [1,[2,[3,[4,[5,6,0]]]],8,9])
		expected = 1
		self.assertEqual(result, expected)


if __name__ == '__main__':
	unittest.main()

		