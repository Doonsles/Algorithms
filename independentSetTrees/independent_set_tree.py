import json

class Tree:
  def __init__(self, filename):
    name_hash = {}
    with open(filename) as data_file:    
      data = json.load(data_file)
   
    root = False 
    for obj in data:
      if(obj['boss'] == None):
        parent = None
        root = True
      else:
        parent = name_hash[obj['boss']]
        root = False

      new_node = Node(obj['name'], obj['party-animal-score'])
      if (parent != None):
        parent.children.append(new_node)
      
      name_hash[new_node.name] = new_node
      if(root):
        self.root = new_node

 
class Node:
  memoized_disjoint_set = {}
  
  def __init__(self, name, value):
    self.name = name
    self.value = value
    self.children = []

  def disjoint_set(self, must_include):
    if (Node.memoized_disjoint_set.has_key(self.name)):
      return Node.memoized_disjoint_set[self.name]
   
    me_invitees = [] 
    me_and_grandchildren = self.value
    for child in self.children:
      for grandchild in child.children:
        info = grandchild.disjoint_set(False) 
        me_and_grandchildren += info['max']
        for person in info['invitees']:
          me_invitees.append(person) 

    not_me_invitees = []
    children_not_me = 0
    if (not must_include):
      for child in self.children:
        info = child.disjoint_set(False)
        children_not_me += info['max']
        for person in info['invitees']:
          not_me_invitees.append(person)
  
    if me_and_grandchildren > children_not_me or must_include:
      me_invitees.append(self.name)
      print "appending " + self.name + " to invitees"
      print "me_and_grandchildren is ", me_and_grandchildren
      return_hash = {'max': me_and_grandchildren, 'invitees': me_invitees}
    else:
      return_hash = {'max': children_not_me, 'invitees': not_me_invitees}
    
    Node.memoized_disjoint_set[self.name] = return_hash
    return return_hash
