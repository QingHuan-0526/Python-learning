from base import module1
from base.module1 import z

y = 20

# 访问当前模块 y
print(y)
# 访问module的y
print(module1.y)
# 访问module1的z
print(z)