word_list = []
doc_list = []
input_docs = open('doc.txt','r')
max_len = 0

for f in input_docs:
    head_vs_content = [x.rstrip() for x in f.split(' : ')]
    doc_list.append(head_vs_content[0])

    for x in head_vs_content[1].split(' '):
