import re

class TodoHandler:
    def toggle(self, line_contents):
        match_todo_todo = re.match('^\s*-\s+\[\s+\]\s+(.*$)', line_contents)
        match_todo_done = re.match('^\s*-\s+\[\s*x\s*\]\s+(.*$)', line_contents)
        match_list_item = re.match('^\s*-\s+(.*$)', line_contents)
        match_empty     = re.match('^\s*$', line_contents)

        if match_todo_todo:
            #  Todo -> Done
            task = match_todo_todo.group(1).rstrip()
            return '- [x] %s' % (task)
        elif match_todo_done:
            # Done -> Other
            task = match_todo_done.group(1).rstrip()
            return task
        elif match_list_item:
            # List item -> Todo
            task = match_list_item.group(1).rstrip()
            return '- [ ] %s' % (task)
        elif match_empty:
            return line_contents.rstrip()
        else:
            # Other -> List item
            return '- %s' % (line_contents.rstrip().lstrip())