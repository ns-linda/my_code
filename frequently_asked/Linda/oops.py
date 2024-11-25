# class shark:
#
#     def __init__(self):
#         self.name = "linda"
#
#     def set_area(self):
#         self.area = 30
#
#
# s=shark()
# s.set_area()
# print(s.area)

class vehicle:

    def __init__(self, type, model):
        self.type = type
        self.model = model

def from_dict(dict):
    instance = vehicle(None, None)
    instance.__dict__.update(dict)
    return instance

car = vehicle("abc", "abc")
class_state = car.__dict__.copy()
print(class_state)
print(from_dict(class_state).__dict__)

