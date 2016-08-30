from xml.etree import ElementTree
from collections import Counter

with open('F:\Documents\GitHub\Co-citationMatrix/citation.xml', 'rt') as f:
    tree = ElementTree.parse(f)

counter = Counter()
authorlist = []

for node in tree.iter('Article'):
	title = node[0].text
	author1 = node[1][0][0].text + ',' + node[1][0][1].text
	author2 = node[1][1][0].text + ','+ node[1][1][1].text
 	counter[author1 + author2] += 1
 	counter[author1 +author1] += 1
 	counter[author2 + author2] += 1
 	counter[author2 + author1] += 1
 	if author1 not in authorlist:
 		authorlist.append(author1)
 	if author2 not in authorlist:
 		authorlist.append(author2)

for author1 in authorlist:
	for author2 in authorlist:
		print counter[author1+author2],

	print