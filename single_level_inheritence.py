class parents:
    def show_parents_name(self):
        return ("kanha","mili ni")
        
class children(parents):
    def show_children_name(self):
        return ("moris","mummy ki pasand")


# parname = parents()
childname = children()
print("parents name: ", childname.show_parents_name())
print("children name :",childname.show_children_name())

