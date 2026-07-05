#in PY, any num wit a decimal point is float
#and it refers to the fact that a decimal point can appear at any position in a num
"""
>>> 0.1+0.1
0.2
>>> 0.2+0.2
0.4
>>> 2*0.1
0.2
>>> 2*0.2
0.4
"""
#however, u can sometimes get an arbitrary num of decimal places in your answer
"""
>>> 0.2+0.1
0.30000000000000004
>>> 3*0.1
0.30000000000000004
"""
#happens in all langs and itso little concern
#PY finds a way to represent the result as precise as possible wic smtyms is difficult given how computers
#represent nums internally, just ignore the extra decimal places for now, u'll learn deal with extra places