#  -*- coding:utf-8 -*-
class Queue:
    def __init__(self):
        self.__list = []

    def enqueue(self, item):
        """'队列添加元素"""
        self.__list.append(item)
        
    def dequeue(self):
        """'队列删除元素"""
        return self.__list.pop(0)

    def is_empty(self):
        """'判断是否为空"""
        return self.__list==[]
    
    def size(self):
        """'返回队列长度"""
        return len(self.__list)


if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    print(q.dequeue())


