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
  memoized_independent_set = {}
  
  def __init__(self, name, value):
    self.name = name
    self.value = value
    self.children = []

  def independent_set(self, must_include):
    if (Node.memoized_independent_set.has_key(self.name)):
      return Node.memoized_independent_set[self.name]
   
    me_invitees = [] 
    me_and_grandchildren = self.value
    for child in self.children:
      for grandchild in child.children:
        info = grandchild.independent_set(False) 
        me_and_grandchildren += info['max']
        for person in info['invitees']:
          me_invitees.append(person) 

    not_me_invitees = []
    children_not_me = 0
    if (not must_include):
      for child in self.children:
        info = child.independent_set(False)
        children_not_me += info['max']
        for person in info['invitees']:
          not_me_invitees.append(person)
  
    if me_and_grandchildren > children_not_me or must_include:
      me_invitees.append(self.name)
      return_hash = {'max': me_and_grandchildren, 'invitees': me_invitees}
    else:
      return_hash = {'max': children_not_me, 'invitees': not_me_invitees}
    
    Node.memoized_independent_set[self.name] = return_hash
    return return_hash
