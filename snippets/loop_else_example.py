# 🚫 Before:
found = False
for n in numbers:
    if n == 42:
        found = True
        break
if not found:
    handle_not_found()


# ✅ After:
for n in numbers:
    if n == 42:
        break
else:
    handle_not_found()

# 🧠 ➤ else after for runs only if no break — no flags, cleaner logic!
