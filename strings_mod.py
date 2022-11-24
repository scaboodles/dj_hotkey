#!/usr/bin/env python3

def plainText(str):
    return removePadding(str)

def formatSearch(str):
    next = removePadding(str)
    return replaceSpaces(next)

def replaceSpaces(str):
   return str.replace(" ", "%20")

def removePadding(str):
    charList = stringToList(str)
    charList = removeLeadingSpaces(charList)
    charList = removeTrailingSpaces(charList)
    #charList = capitalizeFirsts(charList)
    return listToString(charList)

def removeTrailingSpaces(list):
    for i in range(len(list) -1, 0, -1):
        if list[i]==(" "):
            list.pop(i)
        else:
            break
    return list

def removeLeadingSpaces(list):
    list.reverse()
    despaced = removeTrailingSpaces(list)
    despaced.reverse()
    return despaced

def stringToList(str):
    listString = []
    for char in str:
        listString.append(char)
    return listString

def listToString(list):
    str = ""
    for chr in list:
        str += chr
    return str

def capitalizeFirsts(list):
    capitalizeNext = True
    for i in range(len(list)):
        if capitalizeNext:
            if list[i] == " ":
                list.pop(i)
                i-=1
            else:
                temp = list[i]
                list[i] = temp.capitalize()
                capitalizeNext = False
        elif list[i] == " ":
            capitalizeNext = True
    return list


def test():
    test = " hel lo testing testing "
    print(formatSearch(test))