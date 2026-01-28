from math import floor
class MaxHeap:
    def __init__(self):
        self.max_heap = []

    def peek(self):
        return self.max_heap[0] if self.max_heap else None
    
    def push(self, value):
        self.max_heap.append(value)
        self._bubble_up(len(self.max_heap)-1)
    
    def pop(self):
        if not self.max_heap:
            return None
        ret_val = self.max_heap[0]
        if self.max_heap:
            self.max_heap[0] = self.max_heap[-1]
            self.max_heap.pop(-1)
            self._bubble_down(0)
        return ret_val
    
    def _bubble_up(self, ind):
        if not self.max_heap:
            return 
        head = floor(abs(ind - 1)//2)
        if head != ind and self.max_heap[head] < self.max_heap[ind]:
            self.max_heap[head], self.max_heap[ind] = self.max_heap[ind], self.max_heap[head]
            return self._bubble_up(head)
    
    def _bubble_down(self, ind):
        left = 2 * ind + 1
        right = 2 * ind + 2
        largest = ind

        if left < len(self.max_heap) and self.max_heap[left] > self.max_heap[ind]:
            largest = left
        if right < len(self.max_heap) and self.max_heap[right] > self.max_heap[largest]:
            largest = right
        if largest != ind:
            self.max_heap[largest], self.max_heap[ind] = self.max_heap[ind], self.max_heap[largest]

            return self._bubble_down(largest)


heap = MaxHeap()

heap.push(1)
heap.push(2)
heap.push(8)
heap.push(10)
heap.pop()
print(heap.peek())
heap.push(3)
heap.push(5)
heap.push(4)
heap.push(7)


heap.pop()

print(heap.peek())

