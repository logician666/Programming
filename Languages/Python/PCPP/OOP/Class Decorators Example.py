class WarehouseDecorator:
    def __init__(self, material):
        self.material = material
    
    def __call__(self, function):
        def internal_wrapper(*args):
            print(f"* Wrapping items from {function.__name__} with {self.material}")
            function(*args)
            print()
        return internal_wrapper

@WarehouseDecorator('Gold Paper')
def pack_books(*args):
    print("We'll pack books:", args)

pack_books('Introduction to Discrete Mathematics and It\'s Applications', \
    'Calculus (Tom M. Apostol)')