#!/usr/bin/python
import pickle#serialisation

#source:
#https://pythontips.com/2013/08/02/what-is-pickle-in-python/

a = ['f', 's', 't']

foo='bar'
fileName = 'test'
fileObject = open(fileName, 'wb')

pickle.dump(a, fileObject)
fileObject.close()

fileObject = open(fileName, 'r')
b = pickle.load(fileObject)

print(b)


