from logging import basicConfig, getLogger

from pytest import fixture, raises

from doutline import Outline, OutlineItem
from doutline.exceptions import LevelTooHighError, NoLevelIndexError

basicConfig(level="DEBUG")
getLogger("doutline").setLevel("DEBUG")


@fixture
def level() -> Outline[str]:
    return Outline[str]()


def test_append__lower_then_higher(level: Outline[str]) -> None:
    level.append(0, "initial")
    level.append(2, "lower")
    level.append(1, "higher")
    assert level.items == [
        OutlineItem(
            "initial",
            levels=[
                Outline(index=2, items=[OutlineItem("lower")]),
                Outline(index=1, items=[OutlineItem("higher")]),
            ],
        ),
    ]


def test_append__one(level: Outline[str]) -> None:
    level.append(0, data="first")
    assert level.index == 0
    assert level.items == [
        OutlineItem("first"),
    ]


def test_append__then_child(level: Outline[str]) -> None:
    level.append(0, "initial")
    level.append(1, "child")
    assert level.index == 0
    assert level.items == [
        OutlineItem(
            "initial",
            levels=[Outline(index=1, items=[OutlineItem("child")])],
        ),
    ]


def test_append__too_high(level: Outline[str]) -> None:
    level.append(1, "initial")
    with raises(LevelTooHighError) as ex:
        level.append(0, "too high")
    assert str(ex.value) == "An item at level 0 cannot be added at or beneath level 1."


def test_append__two(level: Outline[str]) -> None:
    level.append(0, data="first")
    level.append(0, data="second")
    assert level.index == 0
    assert level.items == [
        OutlineItem("first"),
        OutlineItem("second"),
    ]


def test_eq__index_mismatch() -> None:
    assert Outline[str](index=0) != Outline[str](index=1)


def test_eq__item_mismatch() -> None:
    a = Outline[str](index=0)
    b = Outline[str](index=0)
    b.append(0, "foo")
    assert a != b


def test_eq__type_mismatch(level: Outline[str]) -> None:
    assert level != ""


def test_index__empty(level: Outline[str]) -> None:
    with raises(NoLevelIndexError):
        level.index


def test_index__set_in_init() -> None:
    assert Outline[str](index=0).index == 0


def test_items__empty(level: Outline[str]) -> None:
    assert len(level.items) == 0
