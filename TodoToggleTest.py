import unittest

from TodoToggle import TodoHandler

class TestTodoToggle(unittest.TestCase):

    def setUp(self):
        self.handler = TodoHandler()

    def test_list_items(self):
        self.assertEqual(self.handler.classify('- Item 1'), 'List item')
        self.assertEqual(self.handler.classify('   -     Item 1   '), 'List item')

    def test_todo_empty(self):
        self.assertEqual(self.handler.classify('- [ ] TODO 1'), 'TODO item - empty')
        self.assertEqual(self.handler.classify('  - [ ] TODO 1'), 'TODO item - empty')
        self.assertEqual(self.handler.classify('- [    ]    TODO 1'), 'TODO item - empty')

    def test_todo_full(self):
        self.assertEqual(self.handler.classify('- [x] TODO 1'), 'TODO item - full')
        self.assertEqual(self.handler.classify('- [ x] TODO 1'), 'TODO item - full')
        self.assertEqual(self.handler.classify('- [x ] TODO 1'), 'TODO item - full')
        self.assertEqual(self.handler.classify('- [ x ] TODO 1'), 'TODO item - full')
        self.assertEqual(self.handler.classify('   - [x] TODO 1'), 'TODO item - full')
        
    def test_empty(self):
        self.assertEqual(self.handler.classify(''), 'Empty line')
        self.assertEqual(self.handler.classify('   '), 'Empty line')
        self.assertEqual(self.handler.classify('\t\t '), 'Empty line')

    def test_other(self):
        self.assertEqual(self.handler.classify('Some words and a - dash.'), 'Other type')
        self.assertEqual(self.handler.classify('   Some words and a - dash.'), 'Other type')
        self.assertEqual(self.handler.classify('01234567890'), 'Other type')

if __name__ == '__main__':
    unittest.main()