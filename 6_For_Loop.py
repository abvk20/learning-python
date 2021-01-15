# list1 = [ ["Harry", 1], ["Larry", 2],
#           ["Carry", 6], ["Marie", 250]]
# dict1 = dict(list1)
#
# for item in dict1:
#     print(item)
# for item, lollypop in dict1.items():
#     print(item, "and lolly is ", lollypop)

Technicals = [
    'DS', 'ALGO', 'PYTHON', 'GIT',
    'AWS', 'JENKINS', 'DOCKER', 'OPENSHIFT'
]
Strength = [
        ['DS', 'Strong'], ['ALGO', 'Strong'], ['PYTHON', 'Strong'], ['GIT', 'Average'],
        ['AWS', 'Average to Strong'], ['JENKINS', 'Strong - should know how to build pipelines'],
        ['DOCKER', 'such that you know working, if not practical'],
        ['OPENSHIFT', 'Should know working and familiar with the UI']
]

# print(list23)
# print(list34)
# for tech in Technicals:
#     print(tech)
for technology, rating in Strength:
    print('Your Strength in', technology, 'should be', rating)
dict_strength = {
    'DS':'Strong',
    'ALGO':'STRONG',
    'PYTHON':'STRONG'
}
print("----------------------------",dict_strength,"------------------------------------")
# print(dict_strength)
for techs in dict_strength:
     print('Technology', techs,'should be')
print("--------------------------",dict_strength.values(),"--------------------------------------")
for ratings in dict_strength.values():
    print((ratings))
print("----------------------",dict_strength.items(),"---------------------------------------")
for key, value in dict_strength.items():
    print("Key is",key,"and Value is",value)
