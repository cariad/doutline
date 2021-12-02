from logging import basicConfig, getLogger

from pytest import mark, raises

from doutline import OutlineNode
from doutline.exceptions import LevelTooHighError, NoLevelError

basicConfig(level="DEBUG")
getLogger("doutline").setLevel("DEBUG")


def test_append() -> None:
    root = OutlineNode[str]()
    root.append(0, "0")
    assert root.children == [
        OutlineNode(0, "0"),
    ]


def test_append__too_high() -> None:
    root = OutlineNode[str](1, "root")
    with raises(LevelTooHighError) as ex:
        root.append(0, "0")
    expect = "Cannot add a level 0 node beneath level 1."
    assert str(ex.value) == expect


def test_append__last_has_no_level() -> None:
    root = OutlineNode[str](children=[OutlineNode[str]()])
    with raises(NoLevelError) as ex:
        root.append(0, "0")
    expect = "OutlineNode has no index: OutlineNode()"
    assert str(ex.value) == expect


def test_eq__children_mismatch() -> None:
    a = OutlineNode(0, "foo")
    b = OutlineNode(0, "foo")
    b.append(1, "child")
    assert a != b


def test_eq__data_mismatch() -> None:
    assert OutlineNode(0, "foo") != OutlineNode(0, "bar")


def test_eq__level_mismatch() -> None:
    assert OutlineNode(0, "foo") != OutlineNode(1, "foo")


def test_eq__type_mismatch() -> None:
    assert OutlineNode(0, "foo") != ""


def test_in_range() -> None:
    assert not OutlineNode().in_range(0, 6)


@mark.parametrize(
    "node, expect",
    [
        (OutlineNode[str](), "OutlineNode()"),
        (OutlineNode[str](level=0), "OutlineNode(0)"),
        (OutlineNode[str](data="foo"), 'OutlineNode("foo")'),
        (OutlineNode[str](level=0, data="foo"), 'OutlineNode(0, "foo")'),
        (
            OutlineNode[str](children=[OutlineNode[str](level=1, data="bar")]),
            'OutlineNode(children=[OutlineNode(1, "bar")])',
        ),
        (
            OutlineNode[str](
                level=0,
                data="foo",
                children=[OutlineNode[str](level=1, data="bar")],
            ),
            'OutlineNode(0, "foo", children=[OutlineNode(1, "bar")])',
        ),
    ],
)
def test_repr(node: OutlineNode[str], expect: str) -> None:
    assert repr(node) == expect
