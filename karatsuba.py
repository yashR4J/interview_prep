import string

digs = string.digits + string.ascii_letters
def int2base(x, base):
  if x < 0: sign = -1
  elif x==0: return '0'
  else: sign = 1
  x *= sign
  digits = []
  while x:
    digits.append(digs[x % base])
    x /= base
  if sign < 0:
    digits.append('-')
  digits.reverse()
  return ''.join(digits)

def base2int(s ,base): return int(s,base)

def padding(s1,s2):
    """normalizes 2 string representations to the length of the longest by
    padding the shortest with 0, and returns the padded strings and the
    representation length"""
    n = len(s1)
    delta = n - len(s2)
    if delta < 0: return padding(s2,s1)
    elif delta == 0: return s1, s2, n
    return s1, ("0" * delta) + s2, n

# for testing purposes only, accepts any representation length returns a
# representation of length possibly bigger than that of the input
def binaryop2basebinaryop (f):
    """Given a 2-ary operation on integers, returns the same on string
    representations"""
    return lambda x,y,b: int2base(f(base2int(x,b), base2int(y,b)) ,b)
plus = binaryop2basebinaryop(lambda x,y: x+y)
minus = binaryop2basebinaryop(lambda x,y: x-y)
basicmul = binaryop2basebinaryop(lambda x,y: x*y)

def mult(x,y,b,n):
    """Given two string representations of positive integers, their base,
    and their (equal) length, returns their product (as a string) by the
    karatsuba algorithm"""
    # We arbitrarily choose m = n /2. We could take any m<=n, but this way
    # is faster
    m,r = int(n/2), int(n%2)
    if m == 0:
        # we already have 1-digit numbers (we'll then assume r>0): it's a
        # primitive operation
        return basicmul(x[0],y[0],b)
    # x0,y0 are the lowest m digits of resp. x,y
    x1,x0,y1,y0 = x[:n-m],x[n-m:],y[:n-m],y[n-m:]
    z2 = mult(x1,y1,b,m+r)
    # note z0 has less than 2m bits
    z0 = mult(x0,y0,b,m)
    t,u,k = padding(plus(x1,x0,b), plus(y1,y0,b))
    z1 = minus(minus(mult(t,u,b,k),z2,b),z0,b)
    # we build the string from right to left for educational purposes,
    # starting with the lower m bits of z0
    l0 = len(z0)
    res = z0[l0-m:]
    # Next we have to concatenate the digits of z1 (z1*b^m is z1 shifted
    # by m positions) added to the higher digits of z0, again cutting off
    # at the lowest m bits
    v = plus(z1,z0[:l0-m],b) if l0 > m else z1
    lv = len(v)
    res = v[lv-m:]+res
    # next we concateante the bits of z2 (z2 * b^m is z2 shifted by m)
    # added to the higher bits of z1
    w = plus(z2,z1[:lv-m],b) if lv > m else z2
    return (w + res)

if __name__ == '__main__':
    test_cases = [
        ("5","5",10,1),
        ("01","10",2,2),
        ("2","2",3,1),
    ]
    ans = [25, 2, 6]

    for i in range(len(test_cases)):
        arg1, arg2, arg3, arg4= test_cases[i]
        try:
            assert mult(arg1, arg2, arg3, arg4) == ans[i]
        except:
            print(mult(arg1, arg2, arg3, arg4))