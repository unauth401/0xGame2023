from Crypto.Util.number import *
def string2bits(s):
    return [int(b) for b in s]


initState = [0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0]
outputState = string2bits('1101111111011101100001000011111101001000111000110100010011110111010011100110100100111001101010110110101110000011110101000110010010000011111111001111000110111001100111101110010100100001101001111110001010000100111101011011100010000000100000100000100111010110')
states = initState + outputState
    
ms = MatrixSpace(GF(2), 128, 128)
mv = []
for i in range(128):
    mv += states[i : i + 128]
m= ms(mv)
    
vs = MatrixSpace(GF(2), 128, 1)
vv = outputState[0:128]
v = vs(vv)
    
secret = m.inverse() * v
M=secret.str().replace('\n','').replace('[','').replace(']','')
print(long_to_bytes(eval('0b'+M)))