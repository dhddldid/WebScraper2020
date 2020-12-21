import math # https://docs.python.org/3/library/math.html

#올림
print(math.ceil(1.2))
# Return the absolute value of x.
print(math.fabs(-1.2))

# 특정 모듈만 가져오기 math 안의 ceil, fsum 함수
from math import ceil, fsum

print(ceil(1.2))
print(fsum([1, 2, 3, 4, 5, 6, 7]))

# fsum함수의 이름을 sexy_sum 으로정의
from math import fsum as sexy_sum

print(sexy_sum([1,2,3,4,5,6,7]))

from THEORY.THEORY_1.theory_5_Modules_calculator import plus, minus

print(plus(1,2), minus(1,2))