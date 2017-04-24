This is a Python wrapper around the HTML Tidy library. Quick start example:

```python
from tidylib import Tidy
tidy = Tidy()
document, errors = tidy.tidy_document('<p>f&otilde;o <img src="bar.jpg">',
    options={'alt-text': 'baz'})
print(document)
print(errors)
```

For full documentation, see the docs/ directory or http://countergram.github.io/pytidylib/
