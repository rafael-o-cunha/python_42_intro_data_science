ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

ft_list[1] = "World!"

ft_tuple = (ft_tuple[0], "Brazil!")

# para garantir ordem nesse caso seria preciso usar "sorted" na impressão
ft_set.remove("tutu!")
ft_set.add("Rio de Janeiro!")

ft_dict["Hello"] = "42Rio!"

print(ft_list)
print(ft_tuple)
print(ft_set) 
print(ft_dict)
