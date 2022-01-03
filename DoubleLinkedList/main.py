from DoubleLinkedList import DoubleLinkedList, show_list

a = DoubleLinkedList()
a.add_first('b')
a.add_first('a')
a.add_last('d')
a.insert_after('c',a.search_forward('b'))
show_list(a)

