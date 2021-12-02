---
author: Cariad Eccleston
favicon-emoji: 📑
title: Doutline
---

# 📑 Doutline

**Doutline** is a Python package for generating document outlines.

<edition value="toc" hi="2" />

## Installation

Doutline requires Python 3.8 or later.

Install Doutline via pip:

```bash
pip install doutline
```

## Generating an outline

```python
from doutline import OutlineNode, render_markdown
from io import StringIO

root = OutlineNode(0, "Title")
root.append(1, "First Heading")
root.append(1, "Second Heading")
root.append(2, "Child of Second Heading")
root.append(1, "Third Heading")
root.append(2, "Child of Third Heading")
root.append(3, "Grandchild of Third Heading")

writer = StringIO()
render_markdown(root, writer)
print(writer.getvalue())
```

<!--edition-exec-->

## Writing an outline


### Writing HTML

```python
from doutline import OutlineNode, render_html
from io import StringIO

root = OutlineNode(0, "Title")
root.append(1, "First Heading")
root.append(1, "Second Heading")
root.append(2, "Child of Second Heading")
root.append(1, "Third Heading")
root.append(2, "Child of Third Heading")
root.append(3, "Grandchild of Third Heading")

writer = StringIO()
render_html(root, writer)
print(writer.getvalue())
```

<!--edition-exec-->

You can restrict the outline to a range by setting the `hi` and `lo` arguments:

```python
from doutline import OutlineNode, render_html
from io import StringIO

root = OutlineNode(0, "Title")
root.append(1, "First Heading")
root.append(1, "Second Heading")
root.append(2, "Child of Second Heading")
root.append(1, "Third Heading")
root.append(2, "Child of Third Heading")
root.append(3, "Grandchild of Third Heading")

writer = StringIO()
render_html(root, writer, hi=1, lo=2)
print(writer.getvalue())
```

<!--edition-exec-->

The renderer can also emit hyperlinks when enabled:

```python
from doutline import OutlineNode, render_html
from io import StringIO

root = OutlineNode(0, "Title")
root.append(1, "First Heading")
root.append(1, "Second Heading")
root.append(2, "Child of Second Heading")
root.append(1, "Third Heading")
root.append(2, "Child of Third Heading")
root.append(3, "Grandchild of Third Heading")

writer = StringIO()
render_html(root, writer, hyperlinks=True)
print(writer.getvalue())
```

<!--edition-exec-->








### Writing Markdown

```python
from doutline import OutlineNode, render_markdown
from io import StringIO

root = OutlineNode(0, "Title")
root.append(1, "First Heading")
root.append(1, "Second Heading")
root.append(2, "Child of Second Heading")
root.append(1, "Third Heading")
root.append(2, "Child of Third Heading")
root.append(3, "Grandchild of Third Heading")

writer = StringIO()
render_markdown(root, writer)
print(writer.getvalue())
```

<!--edition-exec-->

You can restrict the outline to a range by setting the `hi` and `lo` arguments:

```python
from doutline import OutlineNode, render_markdown
from io import StringIO

root = OutlineNode(0, "Title")
root.append(1, "First Heading")
root.append(1, "Second Heading")
root.append(2, "Child of Second Heading")
root.append(1, "Third Heading")
root.append(2, "Child of Third Heading")
root.append(3, "Grandchild of Third Heading")

writer = StringIO()
render_markdown(root, writer, hi=1, lo=2)
print(writer.getvalue())
```

<!--edition-exec-->

The renderer can also emit hyperlinks when enabled:

```python
from doutline import OutlineNode, render_markdown
from io import StringIO

root = OutlineNode(0, "Title")
root.append(1, "First Heading")
root.append(1, "Second Heading")
root.append(2, "Child of Second Heading")
root.append(1, "Third Heading")
root.append(2, "Child of Third Heading")
root.append(3, "Grandchild of Third Heading")

writer = StringIO()
render_markdown(root, writer, hyperlinks=True)
print(writer.getvalue())
```

<!--edition-exec-->





## Project

### Contributing

To contribute a bug report, enhancement or feature request, please raise an issue at [github.com/cariad/doutline/issues](https://github.com/cariad/doutline/issues).

If you want to contribute a code change, please raise an issue first so we can chat about the direction you want to take.

### Licence

Doutline is released at [github.com/cariad/doutline](https://github.com/cariad/doutline) under the MIT Licence.

See [LICENSE](https://github.com/cariad/doutline/blob/main/LICENSE) for more information.

### Author

Hello! 👋 I'm **Cariad Eccleston** and I'm a freelance DevOps and backend engineer. My contact details are available on my personal wiki at [cariad.earth](https://cariad.earth).

Please consider supporting my open source projects by [sponsoring me on GitHub](https://github.com/sponsors/cariad/).

### Acknowledgements

- This documentation was pressed by [Edition](https://github.com/cariad/edition).
