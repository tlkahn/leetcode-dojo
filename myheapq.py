import numpy as np
import numpy.typing as npt


class PriorityQueue:
    """
    A heap is a specialized tree-based data structure that satisfies the following two
    properties, which are known as the heap property:

    1. The heap must be a complete binary tree. This means that all levels of the tree must
    be completely filled, except possibly for the last level, which must be filled from left
    to right. In other words, if the last level of the tree is not completely filled, all
    nodes on that level must be as far left as possible.

    2. The value of each node must be greater than or equal to (for a max-heap) or less than
    or equal to (for a min-heap) the values of its children. This is known as the heap-order
    property.

    Together, these properties ensure that the largest (or smallest) element in the heap is
    always at the root of the tree, and that the remaining elements are ordered in a way
    that allows for efficient access to the next largest (or smallest) element.

    Heaps are commonly used in priority queues, where the highest-priority element is always
    at the front of the queue, and in heap sort, which is a popular sorting algorithm that
    uses a heap to sort an array of elements.
    """

    def __init__(self) -> None:
        self.queue: npt.NDArray[np.int64] = np.array([], dtype=np.int64)

    def push(self, item: int) -> None:
        self.queue = np.append(self.queue, item)
        self._heapify_up()

    def pop(self) -> int:
        if self.size == 0:
            raise ValueError("Queue is empty")
        root: int = self.queue[0]
        self.queue[0] = self.queue[self.size - 1]
        self.queue = np.delete(self.queue, self.size - 1)
        self._heapify_down(0)
        return root

    def _heapify_up(self) -> None:
        """
        The `_heapify_up` method is used to maintain the heap property of the priority queue
        after a new item has been added. It does this by comparing the newly added item with its
        parent, and swapping the two if necessary to maintain the heap property.

        Here's how the `_heapify_up` method works:

        1. The method takes the index `i` of the last element in the heap (which is the element
        that was just added) and calculates the index `parent` of its parent element using the
        formula `(i - 1) // 2`.

        2. If the parent element exists and is smaller than the newly added element, the method
        swaps the two elements.

        3. The method then repeats this process with the parent element as the new index `i`,
        and calculates the index `parent` of its parent element using the same formula as
        before.

        4. The method continues this process until it reaches the root of the heap, or until the
        parent element is not smaller than the newly added element.

        By doing this, the `_heapify_up` method ensures that the newly added element is placed
        in its correct position in the heap, so that the maximum element is always at the root
        of the heap. The method is called after a new element has been added to the heap,
        because adding a new element can violate the heap property, and the `_heapify_up` method
        is needed to restore it.
        """
        i: int = self.size - 1
        parent: int = (i - 1) // 2
        while parent >= 0 and self.queue[i] > self.queue[parent]:
            self.queue[i], self.queue[parent] = (
                self.queue[parent],
                self.queue[i],
            )
            i = parent
            parent = (i - 1) // 2

    def _heapify_down(self, i: int) -> None:
        left_child: int = 2 * i + 1
        right_child: int = 2 * i + 2
        largest: int = i
        if left_child < self.size and self.queue[left_child] > self.queue[largest]:
            largest = left_child
        if right_child < self.size and self.queue[right_child] > self.queue[largest]:
            largest = right_child
        if largest != i:
            self.queue[i], self.queue[largest] = (
                self.queue[largest],
                self.queue[i],
            )
            self._heapify_down(largest)

    @property
    def size(self) -> int:
        return len(self.queue)


def test() -> None:
    pq = PriorityQueue()
    pq.push(-1)
    pq.push(5)
    pq.push(9)
    pq.push(1)
    pq.push(3)
    pq.push(7)
    pq.push(2)

    assert pq.pop() == 9
    assert pq.pop() == 7
    assert pq.pop() == 5
    assert pq.pop() == 3
    assert pq.pop() == 2
    assert pq.pop() == 1
    try:
        assert pq.pop() == -1
    except ValueError as e:
        print(f"Error: {e}")

    print("all tests passed")


test()
