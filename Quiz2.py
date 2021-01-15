from typing import Any, Union

list1 = ['dfdf', float, 'dsfads56fa', 314324, 234, 'dsdsf', 78567, 'asdfd7dfw2', 34, 2, 4, 5, 6, 2, 7]
components: Union[Union[str, int], Any]
for components in list1:
    print(type(components))
    if str(components).isnumeric() and components < 6:
        print(components)

items = [int, float, "HaERRY", 5,3, 3, 22, 21, 64, 23, 233, 23, 6]

for item in items:
    if str(item).isnumeric() and item>=6:
        print(item)