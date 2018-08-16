from struct import *

# store as bytes data
packed_data = pack("iif", 6, 19, 12.42)
print(packed_data)

print(calcsize("i"))
print(calcsize("f"))
print(calcsize("iif"))

# to get bytes data back to normal (b'\x06\x00\x00\x00\x13\x00\x00\x00R\xb8FA')
original_data = unpack("iif", packed_data)
print(original_data)
