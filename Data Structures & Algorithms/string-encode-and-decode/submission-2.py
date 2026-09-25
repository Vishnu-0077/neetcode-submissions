class Solution:

    def encode(self, strs: List[str]) -> str:
        return ' '.join(strs)

    def decode(self, s: str) -> List[str]:
        if s is not None:
            return list(s.split(' '))
        else:
            return []

