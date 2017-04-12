from node import Node
import math
from parse import *
import Queue as queue
from sets import Set
import operator

classAttributeValues = uniqueAttributeValues(examples,'Class')
sizeClassAttributeValues = len(classAttributeValues)
usedAttributes = {'Class' :  True}


def ID3(examples, default):
	totalDataSetSize = len(examples)
	root = Node()
	if examples.empty() :
		return root.set_label(default)
	elif isSameClassifiication(examples):
		return root.set_label(examples[0]['Class'])
	elif  attributes.empty():
		return root.set_label(calculateMode(examples))
	else:
		best = chooseBestAttribute(examples)
		root.set_label(best['label'])
		for variable in best['values']:
			selected = selectExamples(examples,best['label'] , variable)	
			subtree = ID3(selected,calculateMode(selected))
			root.set_children(variable,subtree)
	return root
		 
def uniqueAttributeValues(examples,attribute):
	attribValues = set()
	attribValues.add(examples[0][attribute])
	size = len(examples)
	for i in range(1,size):
		if attribValues != examples[i][attribute]:
			attribValues.add(examples[i][attribute])
	attributeValues = list(attribValues)
	return attributeValues


 def isSameClassification(examples):
 	sampleElement = examples[0]['Class']
 	for item in examples[1:]
 		if item != sampleElement
 			return false
	return true


 def calculateMode(examples):
	count = list()
 	size_examples = len(examples)
 	size_classAttrib = len(classAttributeValues)
	for i in range (0, size_examples) :
		for j in range(0,size_classAttrib):
			if  examples[i]['Class'] == classAttributeValues[j] 
 				count[j] += 1
 	max  = 0 
 	for i in range(0,size_classAtrrib)
 		if count[i] >= max
 			max = i 
 	return classAttributeValues[max]

def Hprior(examples,attribute='Class'):
	count = dict.fromkeys(classAttributeValues,0)
	size = len(examples)
	for i in range (0, size) :
		for j in range (0,sizeClassAttributeValues):
	 		if  examples[i][attribute] == classAttributeValues[j]: 
				count[classAttributeValues[j]] += 1  				

 return entropyWrapper(count)



def entropyWrapper(count):
	if len(count) is not 0:
	totalSum = 0
	hPrior = 0 
	for i in range(0,len(count)):
		totalSum += count[i]   
	for  i in range(0,len(count)):
		hprior -= count[i]/totalSum * math.log(count[i]/totalSum,2)
return 	hPrior

 def entropy(examples,attribute):
 	attributeValuesList = list()
	attributeValues = uniqueAttributeValues(examples, attribute)
	sizeAttribValues = len(attributeValues)
	if attribute != None:
		for i in range(0, sizeAttribValues):
			attributeValuesList[i] = dict.fromkeys(classAttributeValues, 0)
		for instance in examples:
			for i in range(0,sizeAttribValues):
				if instance[attribute] == attributeValues[i]:
					attributeValuesList[i] = entropyLoop(instance,attribute,dict_i)
return attributeValuesList				



def entropyLoop(examples,attribute,dict_i):

	for j in range(0,sizeClassAttributeValues):
		if instance['Class'] == classAttributeValues[j]:
			attributeValuesList[i][classAttributeValues[j]] += 1
			break				 
return attributeValuesList[i]

def proportion(dictionary,examples):
    if len(examples) is not 0:
    totalDataSetSize = len(examples)
    
    for i in range(0,len(count)):
        totalSum += count[i]

    return (totalSum/totalDataSetSize)

def calculateInfoGain(examples,attribute):
	hprior = Hprior(examples)
    informationGain = {attribute:None}
    entropyList = list()
    totalSum = len(examples)
    attributeValuesList = entropy(examples,attribute)
	for i in range(0,sizeAttributeValues):
      for j in range(0,sizeClassAttributeValues):
          entropySum += entropyWrapper(attributeValuesList[i]) * proportion(attributeValuesList[i],examples)    
      
    informationGain[attribute] = Hprior(examples) - entropySum
    return informationGain
	

def getMaxInfoGain(dictionary):
	v=list(dictionary.values())
	k=list(dictionary.keys())
	return k[v.index(max(v))]


def chooseBestAttribute(examples):
	result = {'label' : None, 'values': None}
	informationGain = {}
	attributes = getAttributes(examples)
	for attrib in attributes : 
		if attrib not in usedAttributes:
			calculateInfoGain(examples,attrib)
	result = getMaxInfoGain(informationGain)
	usedAttributes[result] = True
	attributeValues = uniqueAttributeValues(examples,result)
	return dict(label=result,values=attributeValues)

def selectExamples(examples,attribute,variable):
	subExamples= []
	for instance in examples:
		if instance[attribute] is variable:
			subExamples.append(instance)
	return subExamples

def prune(node, examples):
  '''
  Takes in a trained tree and a validation set of examples.  Prunes nodes in order
  to improve accuracy on the validation data; the precise pruning strategy is up to you.
  '''

def test(node, examples):
  '''
  Takes in a trained tree and a test set of examples.  Returns the accuracy (fraction
  of examples the tree classifies correctly).
  '''


def evaluate(node, example):
  '''
  Takes in a tree and one example.  Returns the Class value that the tree
  assigns to the example.
  '''




if __name__ == '__main__':
	filename = "house_votes_84.data"
	examples = parse(filename)
	
	# sampleElement = examples[0][attrib]
	# print sampleElement
	
	#print classAttributeValues
	
	#entropy(examples, attribute)

	# if attribute != None:
	# 	for i in range(0, sizeAttribValues):
	# 		attributeValuesList[i] = dict.fromkeys(classAttributeValues, 0)
	# 	for instance in examples:
	# 		for i in range(0,sizeAttribValues):
	# 			if instance[attribute] == attributeValues[i]:
	# 				attributeValuesList[i][attributeValues[i]] += 1
	# 				print attributeValues[i]
	# attribute = 'handicapped-infants'
	# attributeValues = uniqueAttributeValues(examples, attribute)
	# #print attributeValues[0]

	# sizeAttribValues = len(attributeValues)
	
							#print dict_i[classAttributeValues[j]] 
	# for instance in examples:					
	# 	for i in range(0, sizeClassAttributeValues):
	# 		print instance['Class']
	