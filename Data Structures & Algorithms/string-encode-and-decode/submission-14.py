class Solution:
    DELIMITER = "#"
    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += f"{len(s)}#{s}"
        print(result)
        return result
    def decode(self, s: str) -> List[str]:
        i = 0
        buffer = ""
        result = []
        jump_length = None 
        while i < len(s):
            char = s[i]
            print(char)
            if char != "#":
                buffer += s[i]
                print(f"extending buffer with {s[i]}, current buffer {buffer}")
            else:
                jump_length = int(buffer)
                string = s[i+1:i+jump_length+1]
                print(string, "str")
                result.append(string)
                buffer = ""
                i+= jump_length

            i += 1
        return result