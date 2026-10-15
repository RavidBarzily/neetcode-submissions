class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        encoded_string = ""
        for string in strs:
            encoded_string += 'א' + string
        print(encoded_string)
        return encoded_string
    def decode(self, s: str) -> List[str]:
        encoded_string = s.split('א')
        encoded_string.pop(0)
        return encoded_string