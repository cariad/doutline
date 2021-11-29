from logging import getLogger
from typing import Any, Generic, List, Optional

from doutline.exceptions import LevelNotFoundError, LevelTooHighError, NoLevelIndexError
from doutline.types import TData


class Outline(Generic[TData]):
    """
    Represents a level of the document's hierarchy within a single branch.

    Arguments:
        index: Level index. Will be set automatically when appending items if
        omitted.

        items: Items to preload.
    """

    def __init__(
        self,
        index: Optional[int] = None,
        items: Optional[List["OutlineItem[TData]"]] = None,
    ) -> None:
        self._index = index
        self._items = items or []
        self._logger = getLogger("doutline")

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Outline):
            self._logger.debug("OutlineLevel equality failed: type mismatch.")
            return False

        any_other: Outline[Any] = other

        if any_other.index != self.index:
            self._logger.debug("OutlineLevel equality failed: index mismatch.")
            return False

        if any_other.items != self.items:
            self._logger.debug("OutlineLevel equality failed: items mismatch.")
            return False

        return True

    def append(self, level: int, data: TData) -> None:
        """
        Appends an item to the outline.

        Raises:
            ItemTooHighError: If the new item is too high in the hierarchy to be
            added in or beneath this level.
        """

        if self._index is None:
            self._index = level

        if level < self._index:
            raise LevelTooHighError(requested=level, host=self._index)

        if self._index == level:
            self._items.append(OutlineItem[TData](data=data, parent=self))
            return

        last = self._items[-1]
        last.append(level=level, data=data)

    @property
    def index(self) -> int:
        """
        Gets this level's index.

        Raises:
            NoLevelIndexError: If the index has not been set.
        """

        if self._index is None:
            raise NoLevelIndexError()

        return self._index

    @property
    def items(self) -> List["OutlineItem[TData]"]:
        """
        Gets this level's items
        """

        return self._items


class OutlineItem(Generic[TData]):
    """
    Represents an item and its children within an outline.

    Arguments:
        data:   Item data.

        levels: Child levels to preload.

        parent: Outline level that this item inhabits. `None` implies the
        document root.
    """

    def __init__(
        self,
        data: TData,
        levels: Optional[List[Outline[TData]]] = None,
        parent: Optional[Outline[TData]] = None,
    ) -> None:
        self._data = data
        self._levels = levels or []
        self._parent = parent
        self._logger = getLogger("doutline")

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, OutlineItem):
            self._logger.debug("OutlineItem equality failed: type mismatch.")
            return False

        any_other: OutlineItem[Any] = other

        if any_other.data != self.data:
            self._logger.debug("OutlineItem equality failed: data mismatch.")
            return False

        if any_other._levels != self._levels:
            self._logger.debug("OutlineItem equality failed: levels mismatch.")
            return False

        return True

    def append(self, level: int, data: TData) -> None:
        """
        Appends an item to the outline.

        Arguments:
            level: Level to add the item at.
            data:  Item data.
        """

        self.get_level(level, create=True).append(level, data)

    @property
    def data(self) -> TData:
        """
        Gets the meaningful data associated with this outline item.
        """

        return self._data

    def get_level(self, index: int, create: bool = False) -> Outline[TData]:
        """
        Gets a child outline level.

        Arguments:
            index:  Level index.
            create: Create the level if it doesn't exist.

        Raises:
            LevelNotFoundError: If the requested level does not exist and will
            not be created.

            LevelTooHighError: If the requested level is too high to possibly
            exist as a descendent of this item.
        """

        if self._parent and index < self._parent.index:
            raise LevelTooHighError(host=self._parent.index, requested=index)

        for level in self._levels:
            if level.index == index:
                return level

        if not create:
            raise LevelNotFoundError(index)

        level = Outline[TData](index=index)
        self._levels.append(level)
        return level
