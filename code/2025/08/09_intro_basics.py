"""
Day 1 — Intro to Python
Goal: say hello, keep it friendly.
cat << 'EOF' > code/2025/08/09_intro_basics.py
'EOF' > code/2025/08/09_intro_basics.py
"""
Day 1 — Intro to Python
Goal: say hello, keep it friendly.
"""
'EOF' > code/2025/08/09_intro_basics.py
# Ensure folder structure exists
mkdir -p code/2025/08

# Create Day 1 file
cat << 'EOF' > code/2025/08/09_intro_basics.py
"""
Day 1 — Intro to Python
Goal: say hello, keep it friendly.
"""

# The classic first step
print("Hello, world!")

# A tiny variation using a variable + f-string
greeting = "Hello"
target = "Python"
print(f"{greeting}, {target}!")

# Notes:
# - Strings go in quotes.
# - print(...) sends text to the console.
