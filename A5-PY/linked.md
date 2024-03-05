A linked list is a linear data structure where elements are not stored next to each other in memory. Unlike and array, elements in a linked list use pointers or references to each other to keep the list intact.

Like arrays or traditional lists, linked lists are an ordered collection of objects. Linked lists stand apart from lists in how they store elements in memory. While regular lists like arrays and slices use a contiguous memory block to store references to their data linked lists store references or pointers as part of each element

This code defines a simple implementation of a singly linked list in Python using two classes: Node and LinkedList.

Node class:

Represents an individual element in the linked list.
Attributes:
data: Holds the value of the node.
next: Points to the next node in the sequence. Initialized to None.
Methods:
**init**: Initializes a new node with the given data.

LinkedList class:

Represents the linked list data structure.
Attributes:
head: Points to the first node in the list. Initialized to None.

Methods:
**init**: Initializes an empty linked list.
append: Adds a new node with the given data to the end of the linked list.
display: Displays the elements of the linked list.
Usage:

An instance of the LinkedList class named my_linked_list is created.
Elements 1, 2, and 3 are appended to the linked list using the append method.
The display method is called to print the elements of the linked list.
