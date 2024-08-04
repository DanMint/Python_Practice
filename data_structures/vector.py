class Vector:
    def __init__(self, size = None, values = None) -> None:
        if size == None and values != None:
            raise "Cant input values into and empty vector"
        
        if size != None and values != None:
            if size != len(values):
                raise "amount of values does not correspond to the size (or vise versa)"

        if size == None:
            self.__capacity = 1
            self.__size = 0
            self.__vector = [None]*self.__capacity
        else:
            s
            elf.__size = size
            
            self.__capacity = self.__size * 2
            self.__vector = [None]*self.__capacity

        if values != None:
            self.__vector = self.__initial_fill_vector(values)

    def __add__(self, other):
        if isinstance(other, Vector):
            temp = Vector()
            for val in self.__vector:
                if val == None:
                    break
                temp.push(val)

            for val in other.vector:
                temp.push(val)

            return temp
        
        return NotImplemented

    def __repr__(self) -> str:
        return "This class is a modified implementaion of sn std::vector in c++"

    def __initial_fill_vector(self, values) -> None:
        for i in range(len(values)):
            self.__vector[i] = values[i]

    def __resize(self, new_capacity) -> None:
        self.__capacity = new_capacity
        updated_vector = [None] * self.__capacity

        for i in range(len(self.__vector)):
            updated_vector[i] = self.__vector[i]

        self.__vector = updated_vector

    def push(self, val) -> None:
        if self.__size == self.__capacity:
            self.__resize(self.__capacity * 2)

        self.__vector[self.__size] = val
        self.__size += 1

    # remove value from end of vector
    def __pop(self) -> None:
        self.__size -= 1
        self.__vector[self.__size] = None

    def __get_left_hand(self, index) -> list:
        left_hand_vector = [None]*(index)

        for i in range(0, index):
            left_hand_vector[i] = self.__vector[i]
            
        return left_hand_vector

    def __get_right_hand(self, index) -> list:
        right_hand_vector = [None]*(self.__size - index - 1)

        for i in range(index , self.__size):
            right_hand_vector[i - index - 1] = self.__vector[i]
        
        return right_hand_vector

    # remove a specific value via index
    def remove(self, index) -> None:
        if index > self.__size - 1:
            raise "Indes out of range"
        
        left_hand_vector = self.__get_left_hand(index)
        right_hand_vector = self.__get_right_hand(index)

        combination = left_hand_vector + right_hand_vector

        self.__size -= 1
        self.__vector[self.__size] = None

        for i in range(len(combination)):
            self.__vector[i] = combination[i]

    @property
    def pop(self) -> None:
        return self.__pop()

    @property
    def print(self) -> None:
        for val in self.__vector:
            if val == None:
                continue
            print(val, end=" ")
        print()
    
    @property
    def size(self) -> int:
        return self.__size
    
    @property 
    def vector(self) -> list:
        temp = [val for val in self.__vector if val is not None]
        return temp
    
vec1 = Vector()
vec1.push(0)
vec1.push(1)
vec1.push(2)
vec1.push(3)
vec2 = Vector()
vec2.push(4)
vec2.push(5)
vec2.push(6)
vec2.push(7)

vec3 = vec1 + vec2
vec3.print
