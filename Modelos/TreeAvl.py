from Modelos.NodeTreeAvl import NodeTreeAvl
from Modelos.LinkedList import linked_list
from graphviz import Digraph


class TreeAvl:

    def __init__(self):
        self.root: NodeTreeAvl = None
        self.listSimple = linked_list()

    def isEmpty(self):
        if self.root is None:
            return True
        else:
            return False

    def balanceFactor(self, nodeTree):
        if nodeTree is None:
            return -1
        else:
            return nodeTree.factory

    def rotationLeft(self, node: NodeTreeAvl):
        temp = node.left
        node.left = temp.right
        temp.right = node
        node.factory = max(self.balanceFactor(node.left), self.balanceFactor(node.right)) + 1
        temp.factory = max(self.balanceFactor(temp.left), self.balanceFactor(temp.right)) + 1
        return temp
        pass

    def rotationRight(self, node: NodeTreeAvl):
        temp = node.right
        node.right = temp.left
        temp.left = node
        node.factory = max(self.balanceFactor(node.left), self.balanceFactor(node.right)) + 1
        temp.factory = max(self.balanceFactor(temp.left), self.balanceFactor(temp.right)) + 1
        return temp
        pass

    def rotationDoubleLeft(self, node: NodeTreeAvl):
        node.left = self.rotationRight(node.left)
        temp = self.rotationLeft(node)
        return temp
        pass

    def rotationDoubleRight(self, node: NodeTreeAvl):
        node.right = self.rotationLeft(node.right)
        temp = self.rotationRight(node)
        return temp
        pass

    def insertNode(self, nodeNew: NodeTreeAvl, nodeTree: NodeTreeAvl):
        nodeFather: NodeTreeAvl
        nodeFather = nodeTree
        if nodeNew.id < nodeTree.id:
            if nodeTree.left is None:
                nodeTree.left = nodeNew
            else:
                nodeTree.left = self.insertNode(nodeNew, nodeTree.left)
                if (self.balanceFactor(nodeTree.left) - self.balanceFactor(nodeTree.right)) is 2:
                    if nodeNew.id < nodeTree.left.id:
                        nodeFather = self.rotationLeft(nodeTree)
                    else:
                        nodeFather = self.rotationDoubleLeft(nodeTree)

        elif nodeNew.id > nodeTree.id:
            if nodeTree.right is None:
                nodeTree.right = nodeNew
            else:
                nodeTree.right = self.insertNode(nodeNew, nodeTree.right)
                if (self.balanceFactor(nodeTree.right) - self.balanceFactor(nodeTree.left)) is 2:
                    if nodeNew.id > nodeTree.right.id:
                        nodeFather = self.rotationRight(nodeTree)
                    else:
                        nodeFather = self.rotationDoubleRight(nodeTree)
        else:
            print()
        if nodeTree.left is None and nodeTree.right is not None:
            nodeTree.factory = nodeTree.right.factory + 1
        elif nodeTree.right is None and nodeTree.left is not None:
            nodeTree.factory = nodeTree.left.factory + 1
        else:
            nodeTree.factory = max(self.balanceFactor(nodeTree.left), self.balanceFactor(nodeTree.right)) + 1
            pass
        return nodeFather

    def insert(self, id, name):
        newX = NodeTreeAvl(id, name)

        if self.root is None:
            self.root = newX
        else:
            self.root = self.insertNode(newX, self.root)
            pass
        pass

    def Pre(self):
        print("*************PREORDER**************")
        self.listSimple = linked_list()
        self.PreOrder(self.root)
        print("\n***************************")
        pass

    def PreOrder(self, node: NodeTreeAvl):
        if node is not None:
            print(node.id, end='->')
            self.listSimple.add_at_end(node.id)
            self.PreOrder(node.left)
            self.PreOrder(node.right)
            pass
        pass

    def Inno(self):
        print("************INORDER***************")
        self.listSimple = linked_list()
        self.InnOrder(self.root)
        print("\n***************************")
        pass

    def InnOrder(self, node: NodeTreeAvl):
        if node is not None:
            self.InnOrder(node.left)
            print(node.id, end='->')
            self.listSimple.add_at_end(node.id)
            self.InnOrder(node.right)
            pass
        pass

    def Post(self):
        print("*************POSTORDER***************")
        self.listSimple = linked_list()
        self.PosOrder(self.root)
        print("\n***************************")
        pass

    def PosOrder(self, node: NodeTreeAvl):
        if node is not None:
            self.PosOrder(node.left)
            self.PosOrder(node.right)
            print(node.id, end='->')
            self.listSimple.add_at_end(node.id)
            pass
        pass

    def graph(self):
        s = Digraph('structs', filename='tree.gv', node_attr={'shape': 'record'})
        current = self.root
        stack = []  # initialize stack
        done = 0
        s.attr(rankdir='TB')
        while True:
            if current is not None:
                stack.append(current)
                current = current.left
            elif stack:
                current = stack.pop()
                s.node(str(current.id), '{' + str(current.name) + ':' + str(current.id) + ' FE:'+ str(current.factory)+'}')
                if current.left is not None:
                    s.edge(str(current.id), str(current.left.id))
                if current.right is not None:
                    s.edge(str(current.id), str(current.right.id))
                current = current.right
            else:
                break
        s.view()
