import independent_set_tree

my_file = raw_input("Enter a file to read from: ")
my_tree = independent_set_tree.Tree(my_file)

boss_choice = raw_input("Do you require that the CEO be invited to the party? (Y/N)")

if(boss_choice == "Y" or boss_choice == "y"):
  answer = my_tree.root.independent_set(True)

else:
  answer = my_tree.root.independent_set(False)


print ""
print "You should invite these employees to the party:"
for person in answer['invitees']:
  print person

print "For a total score of ", answer['max']

