import sublime
import sublime_plugin
import itertools
import re
import datetime

from TodoToggle.TodoToggle import TodoHandler

class TodoToggleCommand(sublime_plugin.TextCommand):

    def run(self, edit): 
        """
        A plugin function to process a set of selected lines and iterate through 
        the TODO life cycle (plain, list, todo, done).
        """
        handler = TodoHandler()
        regions = itertools.chain(*(reversed(self.view.lines(region)) for region in reversed(list(self.view.sel()))))
        for i, line in enumerate(regions):
            line_contents = self.view.substr(line).rstrip()  
            self.view.replace(edit, line, handler.toggle(line_contents))


class TodoArchiveCommand(sublime_plugin.TextCommand):
    def run(self, edit): 
        """
        A plugin function to scan selected lines for todo done (- [x]) lines 
        and move them to the bottom of the current file (the 'Archive area')

        The items remain 'done' but have a timestamp appended.
        """
        regions = itertools.chain(*(reversed(self.view.lines(region)) for region in reversed(list(self.view.sel()))))
        for i, line in enumerate(regions):
            line_contents = self.view.substr(line).rstrip() 

            match_todo_done = re.match('^\s*-\s+\[\s*x\s*\]\s+(.*$)', line_contents)
            if match_todo_done:
                # Add to the bottom of the file 
                ts = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
                archived_form = '\n%s - @done(%s)' % (line_contents, ts)
                self.view.insert(edit, self.view.size(), archived_form)
                # Remove the original *full_line* of the selection
                self.view.erase(edit, self.view.full_line(line))