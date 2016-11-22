import sublime
import sublime_plugin
import itertools

from TodoToggle.TodoToggle import TodoHandler

class TodoToggleCommand(sublime_plugin.TextCommand):

    def run(self, edit): 
        handler = TodoHandler()
        regions = itertools.chain(*(reversed(self.view.lines(region)) for region in reversed(list(self.view.sel()))))
        for i, line in enumerate(regions):
            line_contents = self.view.substr(line).rstrip()  
            self.view.replace(edit, line, handler.toggle(line_contents))