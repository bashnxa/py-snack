# 🚫 Before:
if type(obj) == list:
    handle_list(obj)


# ✅ After
if isinstance(obj, list):
    handle_list(obj)

# 🧠 ➤ type(obj) == list checks for exact type only — won’t catch subclasses!
# ➤ isinstance considers inheritance — more correct and flexible.
# ➤ Use isinstance for type checks by default.
