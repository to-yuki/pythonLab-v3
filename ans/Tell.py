import sys

param = sys.argv

tel = {'Tanaka':'090-1234-5431','Sato':'080-8472-7462','Suzuki':'070-9873-3974'}

print(param[1],end=' ')
print(':',end=' ')
print(tel[param[1]])

