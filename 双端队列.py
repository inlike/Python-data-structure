#  -*- coding:utf-8 -*-
class Deque:
    def __init__(self):
        self.__list = []

    def add_front(self, item):
        """'队列头添加元素"""
        self.__list.insert(0, item)

    def add_rear(self, item):
        """'队列尾添加元素"""
        self.__list.append(item)

    def pop_front(self):
        """'队列头删除元素"""
        return self.__list.pop(0)

    def pop_rear(self):
        """'队列尾删除元素"""
        return self.__list.pop()

    def is_empty(self):
        """'判断是否为空"""
        return self.__list == []
    
    def size(self):
        """'返回队列长度"""
        return len(self.__list)


if __name__ == '__main__':
    q = Deque()
   

