#!/usr/bin/python
import pickle

pickleFile = 'pickleDumpFile'



class SprintContainer:
  def __init__(self):
	self.container = []



class Sprint:
  def __init__(self):
    self.itemsToDo = []

  def addItem(self, item):
	self.itemsToDo.append(item)
	print('added element: ' + item)

  def showItems(self):
	print('items:')
	print(self.itemsToDo)



exampleSprint = Sprint()

foo.addItem('first')
foo.addItem('second')

foo.showItems()
