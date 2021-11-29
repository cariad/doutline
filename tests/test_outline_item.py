from logging import basicConfig, getLogger

from pytest import raises

from doutline import Outline, OutlineItem
from doutline.exceptions import LevelNotFoundError, LevelTooHighError

basicConfig(level="DEBUG")
getLogger("doutline").setLevel("DEBUG")


def test_eq__data_mismatch() -> None:
    assert OutlineItem("foo") != OutlineItem("bar")


def test_eq__levels_mismatch() -> None:
    a = OutlineItem("foo")
    b = OutlineItem("foo")
    b.append(1, "child")
    assert a != b


def test_eq__type_mismatch() -> None:
    assert OutlineItem("item") != ""


def test_get_level__exists() -> None:
    level = Outline[str](index=1)
    item = OutlineItem[str]("item", levels=[level])
    assert item.get_level(1) is level


def test_get_level__no_create() -> None:
    item = OutlineItem[str]("item")
    with raises(LevelNotFoundError):
        item.get_level(1)


def test_get_level__too_high() -> None:
    level = Outline[str]()
    level.append(2, "item")
    with raises(LevelTooHighError) as ex:
        level.items[0].get_level(1)
    assert str(ex.value) == "An item at level 1 cannot be added at or beneath level 2."
