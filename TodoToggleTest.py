import unittest

from TodoToggle import TodoHandler

class TestTodoToggle(unittest.TestCase):

    def setUp(self):
        self.handler = TodoHandler()

    def test_list_items(self):
        self.assertEqual(self.handler.toggle('- Item 1'), '- [ ] Item 1')
        self.assertEqual(self.handler.toggle('   -     Item 1   '), '- [ ] Item 1')

    def test_todo_empty(self):
        self.assertEqual(self.handler.toggle('- [ ] TODO 1'), '- [-] TODO 1')
        self.assertEqual(self.handler.toggle('  - [ ] TODO 1'), '- [-] TODO 1')
        self.assertEqual(self.handler.toggle('- [    ]    TODO 1'), '- [-] TODO 1')


    def test_todo_inprogress(self):
        self.assertEqual(self.handler.toggle('- [-] TODO 1'), '- [x] TODO 1')
        self.assertEqual(self.handler.toggle('  - [-] TODO 1'), '- [x] TODO 1')
        self.assertEqual(self.handler.toggle('- [-]    TODO 1'), '- [x] TODO 1')


    def test_todo_full(self):
        self.assertEqual(self.handler.toggle('- [x] TODO 1'), 'TODO 1')
        self.assertEqual(self.handler.toggle('- [ x] TODO 1'), 'TODO 1')
        self.assertEqual(self.handler.toggle('- [x ] TODO 1'), 'TODO 1')
        self.assertEqual(self.handler.toggle('- [ x ] TODO 1'), 'TODO 1')
        self.assertEqual(self.handler.toggle('   - [x] TODO 1'), 'TODO 1')
        
    def test_empty(self):
        self.assertEqual(self.handler.toggle(''), '')
        self.assertEqual(self.handler.toggle('   '), '')
        self.assertEqual(self.handler.toggle('\t\t '), '')

    def test_other(self):
        self.assertEqual(self.handler.toggle('Some words and a - dash.'), '- Some words and a - dash.')
        self.assertEqual(self.handler.toggle('   Some words and a - dash.'), '- Some words and a - dash.')
        self.assertEqual(self.handler.toggle('01234567890'), '- 01234567890')

if __name__ == '__main__':
    unittest.main()