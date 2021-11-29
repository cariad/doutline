from typing import IO, Optional

from doutline.outline import OutlineNode


def render_markdown(
    outline: OutlineNode[str],
    writer: IO[str],
    hi: Optional[int] = None,
    indent: int = 0,
) -> None:

    prefix = " " * indent

    if outline.data and (
        hi is None or (outline.level is not None and outline.level >= hi)
    ):
        line = f"{prefix}- {outline.data}\n"
        writer.write(line)
        indent += 2

    for child in outline.children:
        render_markdown(outline=child, writer=writer, hi=hi, indent=indent)
