# HImport
Import python files over http!

# Usage
```python
from himport import himport

h = himport("https://raw.githubusercontent.com/BlackIQ/Hello-World/main/Python/examples/python.py", "h")
```

# Install
Run ```pip install himport```

# Note
Files from github must be raw, and the code must be the only thing on the page. If it relies on dependiences that aren't included in python, or you have installed, you must add those too.

# License
[MIT](https://choosealicense.com/licenses/mit/)