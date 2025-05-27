def change_string(s):
    if s.startswith("abc"):
        return "www" + s[3:]
    else:
        return s + "zzz"
test_strings = ["abc123", "a", "hello", "xd", "abc", "test", "lol"]
for s in test_strings:
    result = change_string(s)
    print(f"'{s}' -> '{result}'")