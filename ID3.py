from node import Node
import math
from parse import * 



def uniqueAttributeValues(examples,attribute):
  attribValues = set()
  attribValues.add(examples[0][attribute])
  size = len(examples)
  for i in range(1,size):
    if attribValues != examples[i][attribute]:
      attribValues.add(examples[i][attribute])
    attributeValues = list(attribValues)
  return attributeValues

filename = "house_votes_84.data"
examples = parse(filename)
classAttributeValues = uniqueAttributeValues(examples,'Class')
sizeClassAttributeValues = len(classAttributeValues)


def isSameClassification(examples):
  sampleElement = examples[0]['Class']
  for item in examples[1:]:
    if item != sampleElement:
      return False
  return True

def getAttributes(examples):
  list_attr = []
  for dic in examples[1]:
    if dic != "Class":
      list_attr.append(dic)
  return list_attr

def calculateMode(examples):
  count = [0]
  size_examples = len(examples)
  size_classAttrib = len(classAttributeValues)
  count=count*2
  for i in range (0, size_examples) :
    for j in range(0,size_classAttrib):
      if  examples[i]['Class'] == classAttributeValues[j]: 
        count[j] += 1
  max  = 0 
  for i in range(0,size_classAttrib):
    if count[i] >= max:
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
    totalSum = 0.0
    hPrior = 0.0 
    for key in count:
      totalSum += count[key]   
    for key in count:
      hPrior -= count[key]/totalSum * math.log(count[key]/totalSum,2.0)
  return  hPrior


def entropy(examples,attribute):
  attributeValuesList = [0]
  attributeValues = uniqueAttributeValues(examples, attribute)
  #print attributeValues
  sizeAttribValues = len(attributeValues)
  attributeValuesList*=sizeAttribValues
  if attribute != None:
    for i in range(0, sizeAttribValues):
      attributeValuesList[i] = dict.fromkeys(classAttributeValues, 0)
    #print attributeValuesList
    for instance in examples:
      for i in range(0,sizeAttribValues):
        if instance[attribute] == attributeValues[i]:
          for j in range(0,sizeClassAttributeValues):
            if instance['Class'] == classAttributeValues[j]:
              attributeValuesList[i][classAttributeValues[j]] += 1
             
  return attributeValuesList        

def proportion(dictionary,examples):
  totalSum=0.0
  if len(examples) is not 0:
    totalDataSetSize = len(examples)
  
  for key in dictionary:
    totalSum += dictionary[key]

  return (totalSum/totalDataSetSize)

def calculateInfoGain(examples,attribute):
  hprior = Hprior(examples)
  informationGain = {attribute:None}
  entropyList = list()
  entropySum=0
  #totalSum = len(examples)
  attributeValuesList = entropy(examples,attribute)
  sizeAttributeValues = len(attributeValuesList)
  for i in range(0,sizeAttributeValues):
    #for j in range(0,sizeClassAttributeValues):
    entropySum += entropyWrapper(attributeValuesList[i]) * proportion(attributeValuesList[i],examples)    
    #print entropyWrapper(attributeValuesList[i])  
    #print proportion(attributeValuesList[i],examples)   
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
      informationGain.update(calculateInfoGain(examples,attrib))
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

def ID3(examples, default):
  attributes = getAttributes(examples)
  ID3(examples, attributes,default)
  


def ID3(examples,attributes,default):

  totalDataSetSize = len(examples)
  root = Node()
  if len(examples)==0 :
    return root.set_label(default)
  elif isSameClassification(examples):
    return root.set_label(examples[0]['Class'])
  elif  len(attributes)==0:
    return root.set_label(calculateMode(examples))
  else:
    best = chooseBestAttribute(examples)
    root.set_label(best['label'])
    for variable in best['values']:
      selected = selectExamples(examples,best['label'] , variable)
      if best in attributes: 
          attributes.remove[best]  
      subtree = ID3(selected, attributes ,calculateMode(selected))
      root.set_children(variable,subtree)
  return root

  '''
  Takes in an array of examples, and returns a tree (an instance of Node) 
  trained on the examples.  Each example is a dictionary of attribute:value pairs,
  and the target class variable is a special attribute with the name "Class".
  Any missing attributes are denoted with a value of "?"
  '''
def breadth_first_search(root):
  ans=""
  if root.get_value()==None:
    ans="Tree is empty"
  else:
    q = Queue()
    q.put(root)
    while True:
      if q.empty():
        break
      a=q.get()
      ans=ans+str(a.get_value())+" "
      if(a.get_children()!=None):
        children=a.get_children()
        noofchilderen=len(children)
        for i in range(1,noofchilderen+1):
          q.put(children[i])
  return ans[0:len(ans)-1]




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


#if __name__ == '__main__':

  #print classAttributeValues
  #print sizeClassAttributeValues
  #print usedAttributes
  #print isSameClassification(examples)
  #print calculateMode(examples)
  #print Hprior(examples)
  #print entropy(examples,'physician-fee-freeze')
  #print calculateInfoGain(examples,'physician-fee-freeze')
  #print chooseBestAttribute(examples)
  #print len(selectExamples(examples,'physician-fee-freeze','y'))
  #print getAttributes(examples)
  #ID3(examples,0)