#!/usr/bin/python

''' Class for Red-Black Binary Search Tree 
	Lei Wei
	03/23/2016
	
	Functions brief:
		nsert(newvalue): 			Insert new value into Red Black tree and maintain the tree property & rank info
		solveColor(newNode): 		Solove the color exception
		insertTree(self,rootnode): 	Combine RB BST with a regualr BST 
		deletenode(self,delNode): 	Del one node form RB BST
		findkeyNode(self,key,rNode):Find all node in a tree with the same key as given, and return as a list the tree rooted at rNode
		delKeyNode(self,key): 		Find all node using the same key as given, and delete them all
		findIthEle(self,i):			Find the i'th smallest element in the tree, if equal, return one of them
		printSubTree(self,RNode):	print subtree rooted at RNode as a sorted list
		sortedList(self):			Print the Tree keys as a sorted list, and return a sorted List as L
'''

''' Node class defined for the balanced Red-Black BST'''
class RBTNode:
	
	def __init__(self,value,parent):
		self.value = value
		self.parent = parent
		'''here we use 1 for color red, 0 for color black'''
		self.color = 1 
		self.leftchild = None
		self.rightchild = None
		''' rank for this node = (rank for leftchild)+(rank for rightchild)+1 '''
		self.rank = 1
		
	def maintainRank(self):
		''' Used to maintain the rank info of the node'''
		m,n = 0,0
		if self.leftchild!=None:
			self.leftchild.maintainRank()
			m = self.leftchild.rank
		if self.rightchild!=None:
			self.rightchild.maintainRank()
			n = self.rightchild.rank
			
		self.rank = m+n+1
		
	def setcolor(self,ch):
		'''set the node color, black or red'''
		if ch =='B':
			self.color = 0
		if ch =='R':
			self.color = 1
	
	def checkLF(self):
		'''check which brand the node is in its parent,left or right'''
		if self.value<=self.parent.value:
			return 'L'
		elif self.value>self.parent.value:
			return 'R'
		else:
			return 'N'
			

		
'''class for Red-Black Binary Search Tree'''
class RBBST:
	def __init__(self,rootvalue,Arra):
		''' init could form a single root, or a complete tree based on array Arra'''
		self.root = RBTNode(rootvalue, None)
		self.root.setcolor('B')
		if Arra != None :
			self.root.value = Arra[0]
			i = 1
			while (i<=(len(Arra)-1)):
				self.insert(Arra[i])
				i+=1
	
	def insert(self,newvalue):
		''' Insert new value into Red Black tree and maintain the tree property & rank info'''
		nodeP = self.root
		newNode = RBTNode(newvalue, None)
		''' BST insert'''
		inserted = 0
		while inserted==0:
			if newvalue<=nodeP.value:
				if nodeP.leftchild == None:
					nodeP.leftchild = newNode
					newNode.parent = nodeP
					nodeP.rank +=1
					inserted = 1
				else:
					nodeP.rank+=1
					nodeP = nodeP.leftchild
			elif newvalue > nodeP.value:
				if nodeP.rightchild == None:
					nodeP.rightchild = newNode
					newNode.parent = nodeP
					nodeP.rank +=1
					inserted = 1
				else:
					nodeP.rank +=1
					nodeP = nodeP.rightchild
			else:
				print 'Red_black BST instert exception occured'	
		self.solveColor(newNode)
			
	def solveColor(self,newNode):
		''' Solove the color exception'''
		while newNode.parent.color == 1:
			if newNode.parent.checkLF()=='L':
				uncleNode = newNode.parent.parent.rightchild
				if (uncleNode!=None) and (uncleNode.color == 1):
					newNode.parent.setcolor('B')
					uncleNode.setcolor('B')
					if uncleNode.parent!= self.root:
						uncleNode.parent.setcolor('R')
						newNode = uncleNode.parent
					else:
						break
				else:
					if newNode.checkLF()=='R':
						A = newNode.parent
						B = newNode
						B2 = newNode.leftchild
						C = newNode.parent.parnet
						C.leftchild = B
						B.parent = C
						B.leftchild = A
						A.parent = B
						A.rightchild = B2
						if B2!=None:
							B2.parent = A
						C.maintainRank()
						newNode = A
					
					A = newNode
					B = newNode.parent
					C = newNode.parent.parent
					B3 = newNode.parent.rightchild
					
					if C==self.root:
						self.root = B
					elif C.checkLF()=='L':
						C.parent.leftchild = B
					elif C.checkLF()=='R':
						C.parent.rightchild = B
					else:
						print 'Insert exception occured when rotation in case 3'
						break
						
					B.parent = C.parent
					B.leftchild = A
					A.parent = B
					B.rightchild = C
					C.parent = B
					C.leftchild = B3
					if B3!=None:
						B3.parent = C
					if B == self.root:
						B.maintainRank()
					else:
						B.parent.maintainRank()
					A.setcolor('R')
					B.setcolor('B')
					C.setcolor('R')
					
			elif newNode.parent.checkLF()=='R':	
				uncleNode = newNode.parent.parent.leftchild
				if (uncleNode!=None)and(uncleNode.color==1):
					newNode.parent.setcolor('B')
					uncleNode.setcolor('B')
					if uncleNode.parent!=self.root:
						uncleNode.parent.setcolor('R')
						newNode = uncleNode.parent
					else:
						break
				else:
					if newNode.checkLF()=='L':
						B = newNode
						A = newNode.parent
						C = newNode.parent.parent
						B3 = newNode.rightchild
						C.rightchild = B
						B.parent = C
						B.rightchild = A
						A.parent = B
						A.leftchild = B3
						if B3!=None:
							B3.parent = A
						newNode = A
					
					A = newNode
					B = newNode.parent
					C = newNode.parent.parent
					B2 = newNode.parent.leftchild
					
					if C ==self.root:
						self.root = B
					elif C.checkLF()=='L':
						C.parent.leftchild = B
					elif C.checkLF()=='R':
						C.parent.rightchild = B
					else:
						print 'Insert exception occured when rotation in case 3'
						break
						
					B.parent = C.parent
					B.leftchild = C
					C.parent = B
					B.rightchild = A
					A.parent = B
					C.rightchild = B2
					if B2!=None:
						B2.parent = C
					if B==self.root:
						B.maintainRank()
					else:
						B.parent.maintainRank()
					A.setcolor('R')
					B.setcolor('B')
					C.setcolor('R')
			else:
				print 'newNode parent color check error'
				break
					
					
	
	def insertTree(self,rootnode):
		''' Combine RB BST with a regualr BST''' 
		self.insert(rootnode.value)
		if rootnode.leftchild!=None:
			self.insertTree(rootnode.leftchild)
		if rootnode.rightchild!=None:
			self.insertTree(root.rightchild)
	
	def deletenode(self,delNode):
		''' Del one node form RB BST'''
		LF = delNode.checkLF()
		if LF == 'L':
			delNode.parent.leftchild = delNode.leftchild
			if delNode.leftchild!=None:
				delNode.leftchild.parent = delNode.parent.leftchild
				self.solveColor(delNode.leftchild)
			if delNode.rightchild!=None:
				self.insertTree(delNode.rightchild)
		elif LF == 'R':
			delNode.parent.rightchild = delNode.rightchild
			if delNode.rightchild!=None:
				delNode.rightchild.parent = delNode.parent.rightchild
				self.solveColor(delNode.rightchild)
			if delNode.leftchild!=None:
				self.insertTree(delNode.leftchild)
		else:
			print 'deletenode error in delNode.checkLF()'
			
	def findkeyNode(self,key,rNode):
		''' Find all node in a tree with the same key as given, and return as a list
		the tree rooted at rNode'''
		if rNode==None:
			return []
		elif rNode.value==key:
			return self.findkeyNode(key,rNode.leftchild)+[rNode]+self.findkeyNode(key,rNode.rightchild)
		else:
			return self.findkeyNode(key,rNode.leftchild)+[]+self.findkeyNode(key,rNode.rightchild)
		
	def delKeyNode(self,key):
		''' Find all node using the same key as given, and delete them all'''
		L = self.findkeyNode(key, self.root)
		for ele in L:
			self.deletenode(ele)
	
	def findIthEle(self,i):
		'''Find the i'th smallest element in the tree, if equal, return one of them'''
		def findith(Tnode,i):
			if (Tnode.rank==1) or (i == Tnode.leftchild.rank+1):
				return Tnode.value
			elif i < Tnode.leftchild.rank+1:
				return findith(Tnode.leftchild,i)
			elif i > Tnode.leftchild.rank+1:
				return findith(Tnode.rightchild,(i-Tnode.leftchild.rank-1))
			else:
				print 'findith() function exception occured'
		
		self.root.maintainRank()
		return findith(self.root, i)
		
	def printSubTree(self,RNode):
		'''print subtree rooted at RNode as a sorted list'''
		if RNode==None:
			return ''
		return ' '+self.printSubTree(RNode.leftchild)+' '+str(RNode.value)+' '+self.printSubTree(RNode.rightchild)
	
	def walkToList(self,RNode):
		'''walk through the bst rooted at RNode and creat a list L'''
		if RNode==None:
			return []
		else:
			return self.walkToList(RNode.leftchild)+[RNode.value]+self.walkToList(RNode.rightchild)
			
	def sortedList(self):
		'''Print the Tree keys as a sorted list, and return a sorted List as L'''
		'''print self.printSubTree(self.root)'''
		L = self.walkToList(self.root)	
		return L
		
				
def test(Arr):
	
	A = RBBST(None, Arr)
	L = A.sortedList()
	print L
	print 'deleate '+str(Arr[2])
	A.delKeyNode(Arr[2])
	L = A.sortedList()
	print L, '  the '+str(3)+' th element is '+ str(A.findIthEle(3))
	

	
test([1,2,3,4,5,6,23,45,2,57,32,84,23,3,75,2,5,798,23,243,65,2,6,8])
print ''
test('abckahsahifdfak')
		