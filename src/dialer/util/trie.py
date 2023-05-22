from __future__ import annotations

from typing import Generic, Optional, TypeVar

T = TypeVar("T")


class TrieNode(Generic[T]):
    def __init__(self):
        self.children: dict[str, TrieNode[T]] = {}
        self.is_end_of_prefix: bool = False
        self.value: Optional[T] = None


class Trie(Generic[T]):
    def __init__(self):
        self.root: TrieNode[T] = TrieNode()

    def insert(self, prefix: str, value: T) -> None:
        node = self.root
        for char in prefix:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_prefix = True
        node.value = value

    def longest_match(self, prefix: str) -> Optional[tuple[str, T]]:
        node = self.root
        longest = ""
        value = None
        for char in prefix:
            if char not in node.children:
                break
            node = node.children[char]
            longest += char
            if node.is_end_of_prefix:
                value = node.value
        if value:
            return longest, value
        return None
