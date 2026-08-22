class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}  # Pasangan kurung
        
        for char in s:
            if char in mapping:  # Kalau ketemu tanda tutup
                top_element = stack.pop() if stack else "#"  # Ambil dari stack
                if mapping[char] != top_element:  # Cek apakah pasangan sesuai
                    return False
            else:
                stack.append(char)  # Kalau kurung buka, tambahkan ke stack

        return not stack  # Kalau stack kosong, berarti valid
