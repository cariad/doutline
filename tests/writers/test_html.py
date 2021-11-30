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
    assert writer.getvalue() == '<nav class="toc"><ul><li>root</li></ul></nav>'


def test_render_html__root_sibling() -> None:
    outline = OutlineNode[str]()
    outline.append(0, "root")
    outline.append(0, "sibling")
    writer = StringIO()
    render_html(outline, writer)
    assert (
        writer.getvalue()
        == '<nav class="toc"><ul><li>root</li><li>sibling</li></ul></nav>'
    )


def test_render_html__root_child() -> None:
    outline = OutlineNode[str]()
    outline.append(0, "root")
    outline.append(1, "child")
    writer = StringIO()
    render_html(outline, writer)
    assert (
        writer.getvalue()
        == '<nav class="toc"><ul><li>root<ul><li>child</li></ul></li></ul></nav>'
    )


def test_render_html__root_child_hyperlinks() -> None:
    outline = OutlineNode[str]()
    outline.append(0, "root")
    outline.append(1, "child")
    writer = StringIO()
    render_html(outline, writer, hyperlinks=True)
    assert (
        writer.getvalue()
        == '<nav class="toc"><ul><li><a href="#root">root</a><ul><li><a href="#child">child</a></li></ul></li></ul></nav>'
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
        == '<nav class="toc"><ul><li>root<ul><li>child</li></ul></li><li>sibling</li></ul></nav>'
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
        == '<nav class="toc"><ul><li>child 1<ul><li>child 2</li><li>sibling 2</li></ul></li><li>sibling 1</li></ul></nav>'
    )
