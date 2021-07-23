import requests
from bs4 import BeautifulSoup as  bs

github_user = input('Input Github User: ')
url = 'https://github.com/' + github_user
r = request.get(url)
soup = bs(r.content, 'html.parser')
pofile_image = soup.find('img', {'alt' : 'Avatar'})['src']
print(profile_image)





"""
// linear
def linear_search(list, target):
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None

def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target is not found in the list")

numbers = [1,2,3,4,5,6,7,8,9,10]

result = linear_search(numbers,5)
verify(result)


//binary
def binary_search(list,target):
    first = 0
    last = len(list) - 1

    while first <= last:
        midpoint = (first + last) // 2

        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return None

def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target is not found in the list")

numbers = [1,2,3,4,5,6,7,8,9,10]

result = binary_search(numbers,5)
verify(result)



//recursive binary
def recursive_binary_search(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint = (len(list))//2

        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return recursive_binary_search(list[midpoint+1:], target)
            else:
                return recursive_binary_search(list[:midpoint],target)

def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target is not found in the list")

numbers = [1,2,3,4,5,6,7,8,9,10]

result = recursive_binary_search(numbers,5)
verify(result)


class Node: 
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<Node data: %s>" % self.data
    
"""
