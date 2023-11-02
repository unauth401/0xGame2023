from Crypto.Util.number import *
from random import getrandbits,randint
from hashlib import sha1
pri_key = 2746225058

class DSA:
    def __init__(self):
        self.q=1456162496340542425374371290437334743490424406311
        self.p=72841069613124631751805267930276882824381743093379818119209711473619790022043432352075870320018597237546487869639155736405121849068664311686015894669435165001653397200645403885067286425100899084073499803767377264054648958466521292317527403925567792577704719995665929014352199034486484542148846324177771403277
        self.g=46558068934124732406430773258764223928028320903408737981233203773125469199851630563857798672894134848206823035995256419026564438820246849887679235434193715375497649204903523656889616845383026014561499136157657188708582182253685067540602760780484861646460575320727995438584054832050366348457069467982870116795
        self.y=45459891333002006876040499506940016656674510764889141461205543223199501353087183552550129903566637048967789261859172910101408627862714531323297930724689586485406532359032328120052576384831053252147875065571336203379271623160424421592520238210614797825937741168217673252428527901460827078642478831355460291617
        self.x = pri_key
    def sign(self,m):
        H = bytes_to_long(sha1(m).digest())
        k = getrandbits(128)
        r = pow(self.g,k,self.p)%self.q
        s = (inverse(k,self.q)*(H+r*self.x))%self.q
        return (s,r)

    def verify(self,m,s_,r_):
        H = bytes_to_long(sha1(m).digest())
        u1 = (inverse(s_,self.q)*H)%self.q
        u2 = (inverse(s_,self.q)*r_)%self.q
        r = (pow(self.g,u1,self.p)*pow(self.y,u2,self.p))%self.p%self.q
        if r == r_:
            return True
        else:
            return False

Test = DSA()
s,r = Test.sign(b'admin')
assert Test.verify(b'admin',s,r) == True
print(s,r)