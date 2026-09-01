from __future__ import annotations

from typing import Any


class Pointer:
    def __init__(
        self,
        data: Any = None,
        left: Pointer | None = None,
        right: Pointer | None = None,
    ) -> None:
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        left = self.left.data if self.left else None
        right = self.right.data if self.right else None
        return f"Pointer({self.data!r}, left={left!r}, right={right!r})"
