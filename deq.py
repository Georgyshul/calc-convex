class Deq:
    """
    Реализация дека на базе вектора
    для языка Python она тривиальна)
    """
    

    def __init__(self):
        self.array = []

    
    def size(self):
        return len(self.array)

    
    def push_last(self, c):
        self.array.append(c)

    
    def push_first(self, c):
        self.array.insert(0, c)

    
    def pop_last(self):
        return self.array.pop()

    
    def pop_first(self):
        return self.array.pop(0)

    
    def last(self):
        return self.array[len(self.array) - 1]

    
    def first(self):
        return self.array[0]


if __name__ == "__main__":
    s = Deq()
    print(s.__dict__)
    s.push_first(1)
    s.push_first(2)
    print(s.__dict__)
    a = s.pop_last()
    print(f"a={a}, array={s.__dict__}")
