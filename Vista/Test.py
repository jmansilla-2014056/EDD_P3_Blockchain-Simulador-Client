from Controlador import Bulk
from Modelos.TreeAvl import TreeAvl

avl = TreeAvl()
avl.insert(10, "A")
avl.insert(5, "B")
avl.insert(13, "C")
avl.insert(1, "D")
avl.insert(6, "E")
avl.insert(17, "F")
avl.insert(16, "J")

g = input()
test = Bulk.readCSV(g)
Bulk.ReadBlockJson(test)
Bulk.Orders(test)
Bulk.validateJson(test)