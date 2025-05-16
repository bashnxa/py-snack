# 🚫 Before:
original = [[1], [2], 3]
shallow = original.copy()
shallow[0][0] = 99
shallow[2] = 42
print(original)   # [[99], [2], 3]


# ✅ After
import copy
original = [[1], [2], 3]
deep = copy.deepcopy(original)
deep[0][0] = 99
deep[2] = 42
print(original)  # [[1], [2], 3]

# 🧠 ➤ .copy() only clones the top level — nested objects like [1] and [2] stay linked. Changing shallow[0][0] affects original, while shallow[2] = 42 is safe since 3 is immutable. Use deepcopy to avoid partial copy traps.





