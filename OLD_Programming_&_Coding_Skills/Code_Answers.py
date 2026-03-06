from collections import Counter, deque
import unittest
from typing import List, Optional

# Function stubs


def reverse_array_in_place(input_array: List) -> List:
    l = len(input_array)

    for i in range(l // 2):
        input_array[i], input_array[l - i -
                                    1] = input_array[l - i - 1], input_array[i]

    return input_array


def find_kth_largest_element_in_array(input_array: List, k: int) -> int:
    sorted_array = []

    for element in input_array:
        inserted = False
        for i in range(len(sorted_array)):
            if element > sorted_array[i]:
                sorted_array.insert(i, element)
                inserted = True
                break
        if not inserted:
            sorted_array.append(element)

    return sorted_array[k - 1]


def move_all_zero_elements_to_the_end_of_array(input_array: List) -> None:
    insert_pos = 0

    for i in range(len(input_array)):
        if input_array[i] != 0:
            input_array[insert_pos] = input_array[i]
            insert_pos += 1

    # Fill the remaining positions with zeros
    for i in range(insert_pos, len(input_array)):
        input_array[i] = 0


def check_if_strings_are_anagrams(input_string_a: str, input_string_b: str) -> bool:
    return Counter(input_string_a.replace(" ", "").lower()) == Counter(
        input_string_b.replace(" ", "").lower()
    )


# Node class for linked list


class Node:
    def __init__(self, data):
        self.data = data
        self.next: Optional["Node"] = None


# Linked list class


class LinkedList:
    def __init__(self):
        self.head: Optional[Node] = None

    def append(self, data):
        new_node = Node(data)

        # If list is empty, make new node the head
        if self.head is None:
            self.head = new_node
            return

        # Otherwise, traverse to the end and append
        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    def display(self):
        values = []
        current = self.head

        while current:
            values.append(str(current.data))  # convert to string for join
            current = current.next

        return " -> ".join(values)

    def reverse(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next  # Store next node
            current.next = prev  # Reverse the link
            prev = current  # Move prev forward
            current = next_node  # Move current forward

        self.head = prev

    def detect_cycle(self):
        """
        Detects whether the linked list contains a cycle.

        Uses Floyd’s Tortoise and Hare algorithm:
        - Two pointers (slow and fast) start at the head.
        - Slow moves one step at a time.
        - Fast moves two steps at a time.
        - If a cycle exists, fast will eventually "lap" slow
          and they will meet at the same node.
        - If fast reaches None, the list has no cycle.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True  # Cycle detected

        return False  # No cycle

    def sort(self):
        """
        Sorts the linked list using Merge Sort.

        Logic:
        - Base case: if list is empty or has one node, it's already sorted.
        - Split the list into two halves using slow/fast pointers.
        - Recursively sort both halves.
        - Merge the sorted halves.

        Time Complexity: O(n log n)
        Space Complexity: O(log n) (recursive stack)
        """

        def merge(l1: Optional[Node], l2: Optional[Node]) -> Optional[Node]:
            dummy = Node(0)
            tail = dummy

            while l1 and l2:
                if l1.data <= l2.data:
                    tail.next = l1
                    l1 = l1.next
                else:
                    tail.next = l2
                    l2 = l2.next
                tail = tail.next

            tail.next = l1 if l1 else l2
            return dummy.next

        def get_middle(head: Node) -> Node:
            slow = head
            fast = head.next

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

            return slow

        def merge_sort(head: Optional[Node]) -> Optional[Node]:
            if not head or not head.next:
                return head

            middle = get_middle(head)
            right_head = middle.next
            middle.next = None  # Split list

            left = merge_sort(head)
            right = merge_sort(right_head)

            return merge(left, right)

        self.head = merge_sort(self.head)

    def merge_list(self, other: "LinkedList"):
        """
        Merges two sorted linked lists into a single sorted list.

        Logic:
        - Create a dummy node to simplify pointer handling.
        - Use a 'tail' pointer to build the new merged list.
        - Compare nodes from both lists (p1 and p2).
        - Attach the smaller node to tail and move that pointer forward.
        - Continue until one list is exhausted.
        - Attach any remaining nodes from the non-empty list.
        - Update self.head to the start of the merged list.

        Assumes both lists are already sorted.

        Time Complexity: O(n + m)
        Space Complexity: O(1) (no new nodes created)
        """
        dummy = Node(0)
        tail = dummy

        p1 = self.head
        p2 = other.head

        while p1 and p2:
            if p1.data <= p2.data:
                tail.next = p1
                p1 = p1.next
            else:
                tail.next = p2
                p2 = p2.next

            tail = tail.next

        # Attach remaining nodes
        if p1:
            tail.next = p1
        if p2:
            tail.next = p2

        self.head = dummy.next


# Linked list algorithms


def reverse_linked_list_itteratively(input_linked_list: LinkedList) -> LinkedList:
    """
    Reverse a LinkedList iteratively and return the same LinkedList (reversed in-place).
    """
    input_linked_list.reverse()
    return input_linked_list


def detect_cycle_in_linked_list(input_linked_list: LinkedList) -> bool:
    """
    Wrapper that returns whether the provided linked list contains a cycle.
    """
    return input_linked_list.detect_cycle()


def merge_two_sorted_linked_lists(l1: LinkedList, l2: LinkedList) -> LinkedList:
    """
    Merge two sorted linked lists into a single sorted linked list.
    Returns a LinkedList (head is the merged head). This function re-uses nodes
    from the input lists and runs in O(n + m) time and O(1) extra space.
    """
    dummy = Node(0)
    tail = dummy

    p1 = l1.head
    p2 = l2.head

    while p1 and p2:
        if p1.data <= p2.data:
            tail.next = p1
            p1 = p1.next
        else:
            tail.next = p2
            p2 = p2.next
        tail = tail.next

    tail.next = p1 if p1 else p2

    merged = LinkedList()
    merged.head = dummy.next
    return merged


# Graph class


class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        # Add vertex if not exists
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, vertex1, vertex2):
        # Add undirected edge (create vertices if needed)
        if vertex1 not in self.adjacency_list:
            self.add_vertex(vertex1)
        if vertex2 not in self.adjacency_list:
            self.add_vertex(vertex2)

        # Avoid duplicate edges in simple implementation
        self.adjacency_list[vertex1].append(vertex2)
        self.adjacency_list[vertex2].append(vertex1)

    def display(self):
        # Return adjacency list representation (useful for tests/printing)
        return {k: list(v) for k, v in self.adjacency_list.items()}


def search_a_graph(search_type: int, input_graph: Graph, start: Optional[str] = None):
    """
    Traverses a graph using either BFS or DFS.

    Search means:
        Explore the graph starting from a node and visit connected nodes.

    It does not mean:
        Find a specific value
        Look for a target
        Return a match

    It means:
        Traverse (walk through) the structure.

    So in this case:
        Search = Graph traversal

    What it does:
    - Starts at a given node (or picks the first node if none is provided).
    - Visits all reachable nodes from that starting point.
    - Returns a list showing the order in which nodes were visited.

    search_type:
    - 1 = Breadth-First Search (BFS)
      Visits nodes level by level (explores neighbors first).
    - 2 = Depth-First Search (DFS)
      Goes as deep as possible before backtracking.

    If the graph is empty or the start node does not exist,
    it returns an empty list.

    If search_type is invalid, it returns None.
    """
    if not input_graph.adjacency_list:
        return []

    if start is None:
        # pick arbitrary start (first inserted key)
        start = next(iter(input_graph.adjacency_list.keys()))

    if start not in input_graph.adjacency_list:
        return []  # start vertex not in graph

    if search_type == 1:
        # BFS
        visited = set()
        q = deque([start])
        order = []

        while q:
            v = q.popleft()
            if v in visited:
                continue
            visited.add(v)
            order.append(v)
            for nei in input_graph.adjacency_list[v]:
                if nei not in visited:
                    q.append(nei)
        return order

    elif search_type == 2:
        # DFS (iterative)
        visited = set()
        stack = [start]
        order = []

        while stack:
            v = stack.pop()
            if v in visited:
                continue
            visited.add(v)
            order.append(v)
            # push neighbors (to visit in adjacency order)
            for nei in reversed(input_graph.adjacency_list[v]):
                if nei not in visited:
                    stack.append(nei)
        return order

    else:
        return None


def sort(sort_type: int, input_array: List) -> List:
    """
    Sorts a list using either Quick Sort or Merge Sort.

    Sort means:
        Rearrange the elements of a list into ordered form.
        Usually ascending order.

    What it does:
    - Takes a list of values.
    - Returns a new sorted list (does NOT modify the original).

    sort_type:
    - 1 = Quick Sort
      Picks a pivot and splits values into smaller and larger groups,
      then recursively sorts them.
      Fast on average.

    - 2 = Merge Sort
      Splits the list into halves, recursively sorts each half,
      then merges them back together in order.
      Very predictable performance.

    Raises:
    - ValueError if an unknown sort_type is provided.
    """

    def quicksort(arr: List) -> List:
        if len(arr) <= 1:
            return arr[:]
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)

    def mergesort(arr: List) -> List:
        if len(arr) <= 1:
            return arr[:]
        mid = len(arr) // 2
        left = mergesort(arr[:mid])
        right = mergesort(arr[mid:])
        i = j = 0
        merged = []
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged

    if sort_type == 1:
        return quicksort(input_array)
    elif sort_type == 2:
        return mergesort(input_array)
    else:
        raise ValueError("Unknown sort_type")


def check_if_number_is_a_palindrome(input_number: int) -> bool:
    number_str = str(input_number)
    length = len(number_str)
    mid = length // 2

    if length % 2 == 0:
        first_half = number_str[:mid]
        second_half = number_str[mid:]
    else:
        first_half = number_str[:mid]
        second_half = number_str[mid + 1:]

    return first_half == second_half[::-1]


# Test class


class TestAnswers(unittest.TestCase):
    def test_reverse_array_in_place(self):
        arr = [1, 2, 3]
        reverse_array_in_place(arr)
        self.assertEqual(arr, [3, 2, 1])

    def test_find_kth_largest_element_in_array(self):
        arr = [1, 2, 3]
        result = find_kth_largest_element_in_array(arr, 3)
        self.assertEqual(result, 1)  # 3rd largest in [1,2,3] is 1

    def test_move_all_zero_elements_to_the_end_of_array(self):
        arr = [1, 0, 3]
        move_all_zero_elements_to_the_end_of_array(arr)
        self.assertEqual(arr, [1, 3, 0])

    def test_check_if_strings_are_anagrams(self):
        self.assertTrue(check_if_strings_are_anagrams("same", "mase"))
        self.assertFalse(check_if_strings_are_anagrams("hello", "world"))

    def test_reverse_linked_list_iteratively(self):
        ll = LinkedList()
        for val in [1, 2, 3]:
            ll.append(val)

        ll.reverse()  # Call method directly

        current = ll.head
        result = []
        while current:
            result.append(current.data)
            current = current.next

        self.assertEqual(result, [3, 2, 1])

    def test_detect_cycle_in_linked_list(self):
        ll = LinkedList()
        for val in [1, 2, 3]:
            ll.append(val)

        # No cycle initially
        self.assertFalse(ll.detect_cycle())

        # Create a cycle manually: last node -> head
        tail = ll.head
        while tail.next:
            tail = tail.next
        tail.next = ll.head  # Create cycle

        self.assertTrue(ll.detect_cycle())

    def test_merge_two_sorted_linked_lists(self):
        l1 = LinkedList()
        l2 = LinkedList()

        for val in [1, 3]:
            l1.append(val)

        for val in [2, 4]:
            l2.append(val)

        merged = merge_two_sorted_linked_lists(l1, l2)

        current = merged.head
        result = []
        while current:
            result.append(current.data)
            current = current.next

        self.assertEqual(result, [1, 2, 3, 4])

    def test_sort_linked_list(self):
        ll = LinkedList()
        for val in [4, 1, 3, 2]:
            ll.append(val)

        ll.sort()

        current = ll.head
        result = []
        while current:
            result.append(current.data)
            current = current.next

        self.assertEqual(result, [1, 2, 3, 4])

    def test_search_a_graph(self):
        g = Graph()
        g.add_vertex('A')
        g.add_vertex('B')
        g.add_edge('A', 'B')
        result = search_a_graph(1, g)
        self.assertIsNotNone(result)

    def test_sort(self):
        arr = [3, 1, 2]
        sorted_quick = sort(1, arr.copy())
        sorted_merge = sort(2, arr.copy())
        self.assertEqual(sorted_quick, sorted(arr))
        self.assertEqual(sorted_merge, sorted(arr))

    def test_check_if_number_is_a_palindrome(self):
        self.assertTrue(check_if_number_is_a_palindrome(12321))
        self.assertFalse(check_if_number_is_a_palindrome(12345))


if __name__ == "__main__":
    unittest.main()
