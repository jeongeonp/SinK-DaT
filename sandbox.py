hexstring = "645b d0b1 682f 491a b1fe c993 9309 3ca4"
bo = bytes.fromhex(hexstring) 
ascii = bo.decode("utf-16")
print(ascii)