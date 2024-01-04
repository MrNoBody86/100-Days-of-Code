# IndexErrors and Working with Nested Lists

list1 = ["item1", "item1", "item2"]

list1[0] = "item0"

list1.append("item3")

list1.extend(["item4","item5"])

# print(list1[len(list1)])

list2 = ["itemA","itemB"]

item_list = [list1 , list2]

print(item_list[1][1])