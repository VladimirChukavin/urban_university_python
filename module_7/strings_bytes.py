# Введение. Строки байты и кодировки

print("Hello")
print(ord("a"))
print(ord("h"))

str_ = "hello"
chars = []

for i in str_:
    chars.append(ord(i))

print(chars)

s = ""

for i in chars:
    s += chr(i)

print(s)

# for i in range(1000, 1200):
# print(chr(i), end=" ")

bb = b"\x68"
print(bb.decode())
