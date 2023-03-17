# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом
# по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

n_length = int(input("Write n:"))
m_length = int(input("Write m:"))
k_slice = int(input("Write k:"))

if k_slice < n_length * m_length and (k_slice % n_length == 0 or k_slice % m_length == 0):
    print(f"{n_length}, {m_length}, {k_slice} -> yes")
else:
    print(f"{n_length}, {m_length}, {k_slice} -> no")
