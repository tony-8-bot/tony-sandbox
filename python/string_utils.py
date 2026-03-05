"""String manipulation helpers for tony-sandbox."""

import re

def reverse(s: str) -> str:
    """Return the reversed string."""
    return s[::-1]

def is_palindrome(s: str) -> bool:
    """Check if a string is a palindrome (case-insensitive, ignoring spaces)."""
    cleaned = s.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

def word_count(s: str) -> int:
    """Return the number of words in a string."""
    return len(s.split()) if s.strip() else 0

def capitalize_words(s: str) -> str:
    """Capitalize the first letter of each word."""
    return ''.join(word.capitalize() if word else ' ' for word in re.split('(\s+)', s))
