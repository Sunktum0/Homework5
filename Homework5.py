immutable_var= 1, 'vlad', True
print(immutable_var)
# immutable_var [0]=100
# print(immutable_var)
# Кортежи являються неизменяемыми,но если в кортеженаходится список элемент этого списка мы сможем его изменить
mutable_list = [1, 'vlad', True]
print(mutable_list)
mutable_list[0]= 2
mutable_list[1]='Anton'
mutable_list[2]=False
print(mutable_list)