# 🚫 Before:
results = []
for item in data:
    if complex_condition(item):
        processed = expensive_operation(item)
        results.append(processed)

# ✅ After:
results = [
    processed
    for item in data
    if complex_condition(item)
    and (processed := expensive_operation(item))
]

# 🧠 ➤ The walrus operator (:=) lets you assign values mid-expression while evaluating conditions,
# enabling value reuse and avoiding redundant computations—all in one go!