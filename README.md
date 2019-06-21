# TodoToggle README

## Overview

This is a first attempt at a simple TODO list handling in [Sublime Text 3](https://www.sublimetext.com/). The idea is to use plain files (e.g. markdown to store the TODO list and use conventions to manage the list.

Currently two functions are supported:

1. ```Toggle``` (mapped to 'ALT-T'): cycle the item through the lifecycle
2. ```Archive``` (mapped to 'SHIFT-ALT-T'): move 'done' items to the bottom of the file and tag as done with a timestamp.

## The TODO lifecycle

A TODO item is a list item. The ```Toggle``` function cycles selected lines through the following cycle:

```
Plain line
- List item line
- [ ] TODO item line
- [x] TODO item line that's marked as done
```

## Roadmap

- [ ] Tag filtering (e.g. @high)
- [ ] Prioritisation (e.g. order by @high, @med, @low)
- [ ] Grouping 
- [ ] Scanning other files for actions 

