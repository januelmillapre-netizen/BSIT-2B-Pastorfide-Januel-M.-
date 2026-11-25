
class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        index = len(self.heap) - 1

        # Move the new value upward
        while index > 0:
            parent = (index - 1) // 2

            if self.heap[index] < self.heap[parent]:
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                index = parent
            else:
                break

    def peek(self):
        if len(self.heap) == 0:
            return None
        return self.heap[0]

    def extract(self):
        if len(self.heap) == 0:
            return None

        smallest = self.heap[0]
        last = self.heap.pop()

        if len(self.heap) > 0:
            self.heap[0] = last
            self.heapify_down(0)

        return smallest

    def heapify_down(self, index):
        size = len(self.heap)

        while True:
            smallest = index
            left = 2 * index + 1
            right = 2 * index + 2

            if left < size and self.heap[left] < self.heap[smallest]:
                smallest = left

            if right < size and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest != index:
                self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
                index = smallest
            else:
                break

    def size(self):
        return len(self.heap)


# Testing Min-Heap
min_heap = MinHeap()

numbers = [5, 9, 11, 14, 19, 17, 18, 13]

for number in numbers:
    min_heap.insert(number)

print("Min-Heap")
print("Size:", min_heap.size())
print("Peek:", min_heap.peek())

print("Extracted values:")
while min_heap.size() > 0:
    print(min_heap.extract(), end=" ")

print()
