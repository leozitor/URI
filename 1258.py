sizes ={'P':1, 'M': 2, 'G':3}
colors ={'branco':1, 'vermelho': 2}
def mergeN(llist, rlist):
    """
    Merge two lists into an ordered list.
    """
    final = []
    while llist or rlist:
        # This verification is necessary for not try to compare
        # a NoneType with a valid type.
        if len(llist) and len(rlist):
            lname = llist[0][2]
            rname = rlist[0][2]
            if lname < rname:
                final.append(llist.pop(0))
            else:
                final.append(rlist.pop(0))

        # This two conditionals here, is for the case when the two lists
        # have diferent sizes. This save us of an error trying to acess
        # an index out of range.
        if not len(llist):
            if len(rlist): final.append(rlist.pop(0))

        if not len(rlist):
            if len(llist): final.append(llist.pop(0))

    return final


def merge_sortN(list):
    """
    Sort the list passed by argument with merge.
    """
    if len(list) < 2: return list
    mid = round(len(list) / 2)
    return mergeN(merge_sortN(list[:mid]), merge_sortN(list[mid:]))


def mergeC(llist, rlist):
    """
    Merge two lists into an ordered list.
    """
    final = []
    while llist or rlist:
        # This verification is necessary for not try to compare
        # a NoneType with a valid type.
        if len(llist) and len(rlist):
            lname = llist[0][0]
            rname = rlist[0][0]
            if lname < rname:
                final.append(llist.pop(0))
            else:
                final.append(rlist.pop(0))

        # This two conditionals here, is for the case when the two lists
        # have diferent sizes. This save us of an error trying to acess
        # an index out of range.
        if not len(llist):
            if len(rlist): final.append(rlist.pop(0))

        if not len(rlist):
            if len(llist): final.append(llist.pop(0))

    return final


def merge_sortC(list):
    """
    Sort the list passed by argument with merge.
    """
    if len(list) < 2: return list
    mid = round(len(list) / 2)
    return mergeC(merge_sortC(list[:mid]), merge_sortC(list[mid:]))


def mergeS(llist, rlist):
    """
    Merge two lists into an ordered list.
    """
    final = []
    while llist or rlist:
        # This verification is necessary for not try to compare
        # a NoneType with a valid type.
        if len(llist) and len(rlist):
            lname = llist[0][1]
            lname = sizes[lname]
            rname = rlist[0][1]
            rname = sizes[rname]
            if lname < rname:
                final.append(llist.pop(0))
            else:
                final.append(rlist.pop(0))

        # This two conditionals here, is for the case when the two lists
        # have diferent sizes. This save us of an error trying to acess
        # an index out of range.
        if not len(llist):
            if len(rlist): final.append(rlist.pop(0))

        if not len(rlist):
            if len(llist): final.append(llist.pop(0))

    return final


def merge_sortS(list):
    """
    Sort the list passed by argument with merge.
    """
    if len(list) < 2: return list
    mid = round(len(list) / 2)
    return mergeS(merge_sortS(list[:mid]), merge_sortS(list[mid:]))

if __name__ == '__main__':
    #wf = "1258in.txt"  # -- remover ao enviar
    #f = open(wf, 'r')  # -- remover ao enviar
    #f = f.readlines()  # -- remover ao enviar
    c = 0
    while True:
        n = int(input())
        #n = n*2
        #n = int(f.pop(0))  # --  remover
        if n == 0:
            quit()

        studentList = []
        for _ in range(n):
            name = input()
            s = input().split()
            #name = f.pop(0)
            #s = f.pop(0).split()
            color, size = s[0], s[1]
            student = [color, size, name]
            studentList.append(student)
        # solucao --------------
        #for i in studentList:
        #    print(i)
        newlist = merge_sortC(studentList)
        newlistL = []
        newlistR = []
        for i in newlist:
            if i[0] == 'branco':
                newlistL.append(i)
            else:
                newlistR.append(i)
        newlistL = merge_sortS(newlistL)
        #print(newlistL)
        newlistR = merge_sortS(newlistR)
        #print(newlistR)
        newlistLP = []
        newlistLM = []
        newlistLG = []
        newlistRP = []
        newlistRM = []
        newlistRG = []

        for i in newlistL:
            if i[1] == 'P':
                newlistLP.append(i)
            elif i[1] == 'M':
                newlistLM.append(i)
            else:
                newlistLG.append(i)

        for i in newlistR:
            if i[1] == 'P':
                newlistRP.append(i)
            elif i[1] == 'M':
                newlistRM.append(i)
            else:
                newlistRG.append(i)
        newlist = []
        if len(newlistLP) > 0:
            newlist = newlist + merge_sortN(newlistLP)
        if len(newlistLM) > 0:
            newlist = newlist + merge_sortN(newlistLM)
        if len(newlistLG) > 0:
            newlist = newlist + merge_sortN(newlistLG)
        if len(newlistRP) > 0:
            newlist = newlist + merge_sortN(newlistRP)
        if len(newlistRM) > 0:
            newlist = newlist + merge_sortN(newlistRM)
        if len(newlistRG) > 0:
            newlist = newlist + merge_sortN(newlistRG)
        if c != 0:
            print()
        c = 1
        for i in newlist:
            print(i[0], end=" ")
            print(i[1], end=" ")
            print(i[2])




