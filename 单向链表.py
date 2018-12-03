#  -*- coding:utf-8 -*-
class Node:
    """'节点"""
    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SingleLinkList:
    """链表"""
    def __init__(self, node=None):
        self._head = node

    def is_empty(self):
        """是否为空"""
        return self._head == None

    def length(self):
        """链表长度"""
        cur = self._head
        count = 0
        while cur != None:
            cur = cur.next
            count += 1
        return count

    def travl(self):
        """遍历整个链表"""
        cur = self._head
        while cur != None:
            print(cur.elem, end = '  ')
            cur = cur.next
        print()

    def add(self, item):
        """链表头部添加元素"""
        node = Node(item)  # 把值转为节点对象
        node.next = self._head
        self._head = node

    def append(self, item):
        """链表尾部添加元素"""
        node = Node(item) #把值转为节点对象
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        """在指定位置添加元素"""
        node = Node(item)
        if pos < 1:
            self.add(item)
        elif pos > self.length():
            self.append(item)
        else:
            per = self._head
            count = 0
            while count < (pos-1):
                count += 1
                per = per.next
            # 循环结后per指向pos-1位置
            node.next = per.next
            per.next = node

    def remove(self, item):
        """删除节点"""
        cur = self._head
        per = None
        while cur != None:
            if cur.elem == item:
                # 处理删除节点是头结点的情况
                if cur == self._head:
                    self._head = cur.next
                else:
                    per.next = cur.next
                break
            else:
                per = cur
                cur = cur.next

    def search(self, item):
        """查找节点"""
        cur = self._head
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False


if __name__ == '__main__':
    ll = SingleLinkList()
    ll.add(2)
    ll.travl()
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    ll.travl()
    ll.insert(3, 'a')
    ll.travl()
    ll.remove('a')
    ll.travl()








