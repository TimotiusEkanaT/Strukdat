class Node: 
    def __init__(self, data, priority):
        self._data = data
        self._priority = priority
        self._next = None

class PriorityQueueUnsorted:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def is_empty(self):
        return self._size == 0
    
    def __len__(self):
        return self._size
    
    def add(self, data, priority):
        baru = Node(data, priority)
        if self.is_empty():
            self._head = baru
            self._tail = baru
        else:
            self._tail._next = baru
            self._tail = baru
        self._size += 1

    def remove(self):
        if self.is_empty() == False:
            if self._size == 1:
                bantu = self._head
                self._head = None
                self._tail = None
                del bantu
            else:
                min_priority = self._head._priority
                hapus = self._head

                while hapus != None:
                    if hapus._priority < min_priority:
                        min_priority = hapus._priority
                    hapus = hapus._next
                
                hapus = self._head
                while hapus._priority != min_priority:
                    hapus = hapus._next

                if hapus == self._head:
                    self._head = self._head._next
                    del hapus

                else:
                    bantu = self._head
                    while bantu._next != hapus:
                        bantu = bantu._next
                    bantu._next = hapus._next
                    del hapus

                    self._tail = self._head
                    while self._tail != None:
                        self._tail = self._tail._next
                self._size -= 1

    def peek(self):
        if self.is_empty():
            return None
        else:
            if self._size == 1:
                return tuple([self._head._data, self._head._priority])
            else:
                min_priority = self._head._priority
                bantu = self._head
                while bantu != None:
                    if bantu._priority < min_priority:
                        min_priority = bantu._priority
                    bantu = bantu._next
                    bantu = self._head
                    while bantu._priority != min_priority:
                        bantu = bantu._next
                    return tuple([bantu._data, bantu._priority])
                
    def print_all(self):
        if self.is_empty():
            print("Kosong")
        else:
            bantu = self._head
            while bantu != None:
                print("(",bantu._data, ",", bantu._priority,")",end = " ")
                bantu = bantu._next
        print()
    

if __name__ == "__main__":
    pq = PriorityQueueUnsorted()
    pq.add ("Rendy",2)
    pq.add ("asep",6)
    pq.remove()
    pq.print_all()                
    