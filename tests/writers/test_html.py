from io import StringIO

from doutline import OutlineNode
from doutline.writers.html import render_html


def test_render_html__empty() -> None:
    outline = OutlineNode[str]()
    writer = StringIO()
    render_html(outline, writer)
    assert writer.getvalue() == ""


def test_render_html__one() -> None:
    outline = OutlineNode[str]()
    outline.append(0, "root")
    writer = StringIO()
    render_html(outline, writer)
    assert writer.getvalue() == '<nav class="toc"><ol><li>root</li></ol></nav>'


def test_render_html__root_sibling() -> None:
    outline = OutlineNode[str]()
    outline.append(0, "root")
    outline.append(0, "sibling")
    writer = StringIO()
    render_html(outline, writer)
    assert (
        writer.getvalue()
        == '<nav class="toc"><ol><li>root</li><li>sibling</li></ol></nav>'
    )


def test_render_html__root_child() -> None:
    outline = OutlineNode[str]()
    outline.append(0, "root")
    outline.append(1, "child")
    writer = StringIO()
    render_html(outline, writer)
    assert (
        writer.getvalue()
        == '<nav class="toc"><ol><li>root<ol><li>child</li></ol></li></ol></nav>'
    )


def test_render_html__root_child_hyperlinks() -> None:
    outline = OutlineNode[str]()
    outline.append(0, "root")
    outline.append(1, "child")
    writer = StringIO()
    render_html(outline, writer, hyperlinks=True)
    assert (
        writer.getvalue()
        == '<nav class="toc"><ol><li><a href="#root">root</a><ol><li><a href="#child">child</a></li></ol></li></ol></nav>'
    )


def test_render_html__root_child_and_sibling() -> None:
    outline = OutlineNode[str]()
    outline.append(0, "root")
    outline.append(1, "child")
    outline.append(0, "sibling")
    writer = StringIO()
    render_html(outline, writer)
    assert (
        writer.getvalue()
        == '<nav class="toc"><ol><li>root<ol><li>child</li></ol></li><li>sibling</li></ol></nav>'
    )


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
    render_html(outline, writer, hi=1, lo=2)
    assert (
        writer.getvalue()
        == '<nav class="toc"><ol><li>child 1<ol><li>child 2</li><li>sibling 2</li></ol></li><li>sibling 1</li></ol></nav>'
    )
