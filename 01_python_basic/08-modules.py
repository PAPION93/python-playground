# 모듈과 패키지

from pkg.fibonacci import Fibonacci

Fibonacci.fib('', 300)
print(Fibonacci.fib2('', 300))
print(Fibonacci().title)
print()

from pkg.fibonacci import Fibonacci as fb

fb.fib('', 300)
print(fb.fib2('', 300))
print(fb().title)
print()

import pkg.calc as c
print(c.add(10, 100))

from pkg.calc import div as d
print(int(d(100,11)))

import pkg.prints as p
import builtins
p.prt1()
p.prt2()
print(dir(builtins))