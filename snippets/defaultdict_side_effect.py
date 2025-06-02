# 🚫 Before:
from collections import defaultdict

users_by_role = defaultdict(list)
snapshot = users_by_role
snapshot["admin"].append("ghost")

# ✅ After:
from collections import defaultdict

users_by_role = defaultdict(list)
snapshot = dict(users_by_role)
snapshot["admin"].append("ghost")

# 🧠 ➤ defaultdict mutates on access — even reads can add keys. Use dict() to avoid unintended side effects.
