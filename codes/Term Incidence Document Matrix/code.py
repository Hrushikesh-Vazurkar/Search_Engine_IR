import numpy as np

termIncidenceMatrix = []
word_list = []
doc_list = []

input_docs = open('doc.txt','r')
max_len = 0

for f in input_docs:
    head_vs_content =[x.rstrip() for x in f.split(' : ')]
    for x in head_vs_content[1].split(' '):
        if x not in word_list:
            word_list.append(x)

    doc_list.append(head_vs_content[0])

# print(word_list)
# print(doc_list)

termIncidenceMatrix = np.zeros((len(word_list),len(doc_list)),dtype="bool")
# print(termIncidenceMatrix)
input_docs.close()

input_docs = open('doc.txt','r')
c = 0

for f in input_docs:
    head_vs_content =[x.rstrip() for x in f.split(' : ')]
    for x in head_vs_content[1].split(' '):
        c2 = 0
        for y in word_list:
            if x == y:
                termIncidenceMatrix[c2][c] = True
                break
            c2+=1

    c+=1

# print(termIncidenceMatrix)

query = str(input()).split(' ')
# print(query)
qw_list = [x for x in query if x!='and' and x!='AND']
# print(qw_list)

ans = np.ones((len(doc_list),),dtype="bool")
# print(ans)

for q in qw_list:
    c = 0
    for x in word_list:
        if x==q:
            # print("in")
            # print(termIncidenceMatrix[c])
            ans = ans & termIncidenceMatrix[c]
            break
        c+=1

c = 0
for x in ans:
    if x==True:
        print(doc_list[c])
    c+=1