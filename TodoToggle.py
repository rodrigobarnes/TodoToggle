import re

class TodoHandler:
    def classify(self, line_contents):
        if re.match('^\s*-\s+\[\s+\]\s+(.*$)', line_contents):
            return 'TODO item - empty'
        elif re.match('^\s*-\s+\[\s*x\s*\]\s+(.*$)', line_contents):
            return 'TODO item - full'  
        elif re.match('^\s*-\s+(.*$)', line_contents):
            return 'List item'
        elif re.match('^\s*$', line_contents):
            return 'Empty line'
        else:
            return 'Other type'

    def toggle(self, line_contents):
        match_todo_empty    = re.match('^\s*-\s+\[\s+\]\s+(.*$)', line_contents)
        match_todo_full     = re.match('^\s*-\s+\[\s*x\s*\]\s+(.*$)', line_contents)
        match_list_item     = re.match('^\s*-\s+(.*$)', line_contents)
        match_empty         = re.match('^\s*$', line_contents)

        if match_todo_empty:
            task = match_todo_empty.group(1)
            return '- [x] %s' % (task)
        elif match_todo_full:
            task = match_todo_full.group(1)
            return '- [ ] %s' % (task) 
        elif match_list_item:
            task = match_list_item.group(1)
            return '- [ ] %s' % (task)
        elif match_empty:
            return line_contents
        else:
            return '- %s' % (line_contents)