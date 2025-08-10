class Node:
    def __init__(self, data=None):
        self.__data = data
        self.__prev = None
        self.__next = None

    def __del__(self):
        print("data of {} is deleted".format(self.data))

    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def prev(self):
        return self.__prev
    
    @prev.setter
    def prev(self,p):
        self.__prev = p
    
    @property
    def next(self):
        return self.__next
    
    @next.setter
    def next(self,n):
        self.__next = n