from io import StringIO

from pytest import mark

from doutline import OutlineNode
from doutline.writers import render_markdown
from doutline.writers.utils import make_anchor


@mark.parametrize(
    "value, expect",
    [
        ("foo", "foo"),
        ("🍕 Pizza", "-pizza"),
        ("gem _and_ gemmy", "gem-and-gemmy"),
    ],
)
def test_make_anchor(value: str, expect: str) -> None:
    assert make_anchor(value) == expect


def test_render_markdown_empty() -> None:
    outline = OutlineNode[str]()
    writer = StringIO()
    render_markdown(outline, writer)
    assert writer.getvalue() == ""


def test_render_markdown_one() -> None:
    outline = OutlineNode[str]()
    outline.append(0, "root")
    writer = StringIO()
    render_markdown(outline, writer)
    assert writer.getvalue() == "- root\n"


def test_render_markdown_root_sibling() -> None:
    outline = OutlineNode[str]()
    outline.append(0, "root")
    outline.append(0, "sibling")
    writer = StringIO()
    render_markdown(outline, writer)
    assert writer.getvalue() == "- root\n- sibling\n"


def test_render_markdown_root_child() -> None:
    outline = OutlineNode[str]()
    outline.append(0, "root")
    outline.append(1, "child")
    writer = StringIO()
    render_markdown(outline, writer)
    assert writer.getvalue() == "- root\n  - child\n"


def test_render_markdown_root_child_hyperlinks() -> None:
    outline = OutlineNode[str]()
    outline.append(0, "root")
    outline.append(1, "child")
    writer = StringIO()
    render_markdown(outline, writer, hyperlinks=True)
    assert writer.getvalue() == "- [root](#root)\n  - [child](#child)\n"


def test_render_markdown_root_child_and_sibling() -> None:
    outline = OutlineNode[str]()
    outline.append(0, "root")
    outline.append(1, "child")
    outline.append(0, "sibling")
    writer = StringIO()
    render_markdown(outline, writer)
    assert writer.getvalue() == "- root\n  - child\n- sibling\n"


def test_render_markdown_ranged() -> None:
    outline = OutlineNode[str]()
    outline.append(0, "root")
    outline.append(1, "child 1")
    outline.append(2, "child 2")
    outline.append(3, "child 3")
    outline.append(3, "sibling 3")
    outline.append(2, "sibling 2")
    outline.append(1, "sibling 1")
    outline.append(0, "sibling 0")
    writer = StringIO()
    render_markdown(outline, writer, hi=1, lo=2)
    assert (
        writer.getvalue()
        == """- child 1
  - child 2
  - sibling 2
- sibling 1
"""
    )
