from __future__ import annotations
from typing import Callable, Tuple
from abc import abstractclassmethod

class MDBase:
    def __init__(self, txt: str = "", from_file: bool = False) -> None:
        pass
    @classmethod
    def load_from_file(cls, path: str) -> MDBase:
        pass
    def _next_block() -> bytes:
        pass
    def _left_rotate(val: int, shift: int) -> int:
        pass
    @abstractclassmethod
    def _next_properties() -> Tuple[Callable[[int, int, int], int], int, int, int]:
        pass
    @abstractclassmethod
    def _code() -> str:
        pass
    