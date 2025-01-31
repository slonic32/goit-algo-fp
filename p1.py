class Node:
	def __init__(self, data=None):
		self.data = data
		self.next = None


class LinkedList:
	def __init__(self):
		self.head = None

	def insert_at_beginning(self, data):
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node

	def insert_at_end(self, data):
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
		else:
			cur = self.head
			while cur.next:
				cur = cur.next
			cur.next = new_node

	def insert_after(self, prev_node: Node, data):
		if prev_node is None:
			print("Попереднього вузла не існує.")
			return
		new_node = Node(data)
		new_node.next = prev_node.next
		prev_node.next = new_node

	def delete_node(self, key: int):
		cur = self.head
		if cur and cur.data == key:
			self.head = cur.next
			cur = None
			return
		prev = None
		while cur and cur.data != key:
			prev = cur
			cur = cur.next
		if cur is None:
			return
		prev.next = cur.next
		cur = None

	def search_element(self, data: int) -> Node | None:
		cur = self.head
		while cur:
			if cur.data == data:
				return cur
			cur = cur.next
		return None

	def print_list(self):
		current = self.head
		while current:
			print(current.data)
			current = current.next
	
	def reverse(self):
		prev = None
		cur = self.head
		while cur:
			next_node = cur.next
			cur.next = prev
			prev = cur
			cur = next_node
		self.head = prev

	def merge(self, a: Node, b: Node) -> Node:
		if not a:
			return b
		if not b:
			return a
		if a.data <= b.data:
			result = a
			result.next = self.merge(a.next, b)
		else:
			result = b
			result.next = self.merge(a, b.next)
		return result
	
	def _find_center(self, head: Node) -> Node:
		a = head
		b = head
		while a.next and a.next.next:
			b = b.next
			a = a.next.next
		return b
	
	def _merge_sort(self, head: Node) -> Node:
		if not head or not head.next:
			return head
		center = self._find_center(head)
		next = center.next
		center.next = None
		left = self._merge_sort(head)
		right = self._merge_sort(next)
		return self.merge(left, right)
	
	def merge_sort(self):
		if not self.head or not self.head.next:
			return
		self.head = self._merge_sort(self.head)
		
def merge_lists(list1, list2) :
		result = LinkedList()
		result.head = result.merge(list1.head, list2.head)
		return result


        


def main():
	llist = LinkedList()

	# Вставляємо вузли в початок
	llist.insert_at_beginning(5)
	llist.insert_at_beginning(10)
	llist.insert_at_beginning(15)

	# Вставляємо вузли в кінець
	llist.insert_at_end(20)
	llist.insert_at_end(25)

	# Друк зв'язного списку
	print("Зв'язний список:")
	llist.print_list()

	llist.reverse()
	print("\nЗв'язний список після реверсування:")
	llist.print_list()

	llist.merge_sort()
	print("\nЗв'язний список після сортування:")
	llist.print_list()


	llist2 = LinkedList()

	# Вставляємо вузли в початок
	llist2.insert_at_beginning(55)
	llist2.insert_at_beginning(105)
	llist2.insert_at_beginning(150)
	llist2.merge_sort()
	llist3 = merge_lists(llist, llist2)
	print("\nЗв'язний список після злиття:")
	llist3.print_list()

if __name__ == "__main__":
    main()
    