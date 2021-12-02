# 📑 Doutline

**Doutline** is a Python package for generating document outlines.

- [Installation](#installation)
- [Generating an outline](#generating-an-outline)
- [Writing an outline](#writing-an-outline)
  - [Writing HTML](#writing-html)
  - [Writing Markdown](#writing-markdown)
- [Project](#project)
  - [Contributing](#contributing)
  - [Licence](#licence)
  - [Author](#author)
  - [Acknowledgements](#acknowledgements)

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

<!--edition-exec as=markdown fence=backticks host=shell range=start-->

```text
- Title
  - First Heading
  - Second Heading
    - Child of Second Heading
  - Third Heading
    - Child of Third Heading
      - Grandchild of Third Heading
```

<!--edition-exec range=end-->

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

<!--edition-exec as=markdown fence=backticks host=shell range=start-->

```text
<nav class="toc"><li>Title<ol><li>First Heading</li><li>Second Heading<ol><li>Child of Second Heading</li></ol></li><li>Third Heading<ol><li>Child of Third Heading<ol><li>Grandchild of Third Heading</li></ol></li></ol></li></ol></li></nav>
```

<!--edition-exec range=end-->

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

<!--edition-exec as=markdown fence=backticks host=shell range=start-->

```text
<nav class="toc"><ol><li>First Heading</li><li>Second Heading<ol><li>Child of Second Heading</li></ol></li><li>Third Heading<ol><li>Child of Third Heading</li></ol></li></ol></nav>
```

<!--edition-exec range=end-->

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

<!--edition-exec as=markdown fence=backticks host=shell range=start-->

```text
<nav class="toc"><li><a href="#title">Title</a><ol><li><a href="#first-heading">First Heading</a></li><li><a href="#second-heading">Second Heading</a><ol><li><a href="#child-of-second-heading">Child of Second Heading</a></li></ol></li><li><a href="#third-heading">Third Heading</a><ol><li><a href="#child-of-third-heading">Child of Third Heading</a><ol><li><a href="#grandchild-of-third-heading">Grandchild of Third Heading</a></li></ol></li></ol></li></ol></li></nav>
```

<!--edition-exec range=end-->








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

<!--edition-exec as=markdown fence=backticks host=shell range=start-->

```text
- Title
  - First Heading
  - Second Heading
    - Child of Second Heading
  - Third Heading
    - Child of Third Heading
      - Grandchild of Third Heading
```

<!--edition-exec range=end-->

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

<!--edition-exec as=markdown fence=backticks host=shell range=start-->

```text
- First Heading
- Second Heading
  - Child of Second Heading
- Third Heading
  - Child of Third Heading
```

<!--edition-exec range=end-->

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

<!--edition-exec as=markdown fence=backticks host=shell range=start-->

```text
- [Title](#title)
  - [First Heading](#first-heading)
  - [Second Heading](#second-heading)
    - [Child of Second Heading](#child-of-second-heading)
  - [Third Heading](#third-heading)
    - [Child of Third Heading](#child-of-third-heading)
      - [Grandchild of Third Heading](#grandchild-of-third-heading)
```

<!--edition-exec range=end-->





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
