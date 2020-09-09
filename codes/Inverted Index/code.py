
invertedIndexMap = {}

file = open('doc.txt')
for f in file:
    doc_vs_data = f.split(' : ')
    doc_vs_data[1] = doc_vs_data[1].rstrip()

    for x in doc_vs_data[1].split(' '):
        if x in invertedIndexMap.keys():
            invertedIndexMap[x].append(doc_vs_data[0])
        else:
            invertedIndexMap[x] = []
            invertedIndexMap[x].append(doc_vs_data[0])

print(invertedIndexMap)

query = str(input()).split(' ')
qw_list = [x.lower() for x in query]

