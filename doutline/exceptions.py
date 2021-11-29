class LevelNotFoundError(Exception):
    """
    Raised when a level is not found.

    Arguments:
        index: Index of the missing level.
    """

    def __init__(self, index: int) -> None:
        super().__init__(f"No level with index {index}.")


class LevelTooHighError(Exception):
    """
    Raised when a requested level is too high to possibly exist as a descendent
    of the item hosting the request.

    Arguments:
        host:      Host level index.
        requested: Requested level index.
    """

    def __init__(self, host: int, requested: int) -> None:
        super().__init__(
            f"An item at level {requested} cannot be added at or beneath level {host}."
        )


class NoLevelIndexError(Exception):
    """
    Raised when a level's index is read before it has been set.
    """

    def __init__(self) -> None:
        super().__init__("Level has no index.")
