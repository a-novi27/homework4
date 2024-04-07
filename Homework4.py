immutable_var = 1, 5, True, "Please"
print(immutable_var)
print(type(immutable_var))
#immutable_var[0, 3] = 100#<class 'tuple'> не изменяемый тип!
mutable_list = ['1', '5', 'True', 'Please']
print(type(mutable_list))
mutable_list[0] = "Go"
mutable_list[2] = 'False'
print(mutable_list)
