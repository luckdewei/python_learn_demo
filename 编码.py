text = "Hello"
encoded = text.encode("ascii")
print(encoded)  # b'Hello'
print(encoded.hex())  # 48656c6c6f
print("".join(f"\\x{b:02x}" for b in encoded))  # \x48\x65\x6c\x6c\x6f
print(encoded.decode("ascii"))  # Hello
