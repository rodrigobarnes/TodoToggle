import sublime
import sublime_plugin
import itertools

from TodoToggle.TodoToggle import TodoHandler

class TodoToggleCommand(sublime_plugin.TextCommand):

    def run(self, edit): 
        print(self.view.sel())
        handler = TodoHandler()
        regions = itertools.chain(*(reversed(self.view.lines(region)) for region in reversed(list(self.view.sel()))))
        # regions = list(self.view.sel())
        for i, line in enumerate(regions):
            line_contents = self.view.substr(line).rstrip()
            print(i) 
            print(line_contents)
            print(handler.toggle(line_contents))            

# this is a test
"""

Item 1
- [ ] Item 1
- [x] Item 1

- Item 1
- Item 2
- Item 3
- Item 4
- [ ] TODO 1
- [ ] TODO 2
- [x] TODO 3

Some random text
"""