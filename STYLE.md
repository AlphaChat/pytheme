# Styling Rules

## General style

- Python code should not exceed 79 columns in 1 line.
- No spaces around parens or brackets
    - `[ this is not ok ]`
    - `func( "don't do this either" )`
    - `{"this is good"}`
- Use double quotes `""` where possible, and only use single quotes when inside
double quotes

## Functions and Methods

- Always use 2 new lines between separate functions and classes, and "constants". 1 line is ok
between methods

```python
SOME_CONSTANT = True
ANOTHER_CONSTANT = False


def foo():
    """ lorem ipsum ... """
    pass


def bar():
    """ dolor sit amet ... """
    pass
```

- Align function parameters to the opening paren. This applies to both function calls and definition.
```python
my_super_long_function(long_arg_1, long_arg_2, long_arg_3,
                       long_arg_4, long_arg_5, long_arg_6)
```

- Never more than 1 space between lines in the body of a function

## Comments
- Always use 2 spaces for inline comments `  # like this`
- Always use 1 `#` when writing comments
    - `## don't do this`
    - `# this is good`
- When using block style comments, use triple doube-quotes `""" like this """`
- When block stype comments span multiple lines, put the triple-quotes on their
own lines
```python
"""
Just
Like
This
"""
```


## Imports

- Never import multiple modules on one line
    - Bad: `import sys, os, re`
- Sorting (a "sort imports" extension that obeys PEP8 helps with this)
    - Import standard library modules first, then new line, then site-packages (3rd party stuff), then application modules.
```python
import os

from Flask import Blueprints, flash, redirect

from . import atheme
```
