# HImport
Import python files over http!

# Usage
```python
from himport import himport

h = himport("https://raw.githubusercontent.com/combogangreal/HImport/main/examples/test.py", "h")

h.test()
```

Output
```
This is a test!
```

# Install
Run ```pip install himport```

# Note
Files from github must be raw, and the code must be the only thing on the page. If it relies on dependiences that aren't included in python, or you have installed, you must add those too.

# License
[MIT](https://choosealicense.com/licenses/mit/)