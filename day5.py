#file = open("testinputday5.txt",'r')
file = open("inputday5.txt",'r')
content = file.readlines()
file.close()
print(content)

def format_rules(rules):
    formatted_rules = []
    for i in range(len(rules)):
        formatted = rules[i].split('|')
        formatted_rules.append((int(formatted[0]),int(formatted[1])))
    return formatted_rules

def format_pages(pages):
    print(pages)
    formatted_pages = []
    for i in range(len(pages)):
        splitted = pages[i].split(',')
        #print('SPLITTED : ',splitted)
        formatted = []
        for i in range(len(splitted)):
            formatted.append(int(splitted[i]))
        formatted_pages.append(formatted)
    return formatted_pages

def is_ordered_page(rules,index_page,updated_pages):
    for rule in rules:
        if rule[0] == updated_pages[index_page]:
            for i in range(index_page):
                if updated_pages[i] == rule[1]:
                    return False
    return True

def is_ordered_list(rules,list_pages):
    for i in range(len(list_pages)):
        if not is_ordered_page(rules,i,list_pages):
            return False
    return True


def get_correctly_ordered(rules,array_pages):
    ordered = []
    for list_pages in array_pages:
        if is_ordered_list(rules,list_pages):
            ordered.append(list_pages)
    return ordered

def get_middle_page(array_pages):
    return array_pages[len(array_pages)//2]

def get_sum_middle_pages(array_list):
    sum = 0
    for pages in array_list:
        sum += get_middle_page(pages)
    return sum


rules = []
pages_to_produce = []
for data in content:
    if '|' in data:
        rules.append(data)
    elif data !='\n':
        pages_to_produce.append(data)

print('RULES : ', rules,'PAGES : ', pages_to_produce)


formatted_rules = (format_rules(rules))
formatted_pages = (format_pages(pages_to_produce))

print("Formatted pages : ",formatted_pages)

correctly_ordered = get_correctly_ordered(formatted_rules,formatted_pages)

print("Correctly ordered : ",correctly_ordered)

print(get_sum_middle_pages(correctly_ordered))
