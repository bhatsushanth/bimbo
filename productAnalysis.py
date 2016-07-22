import re
p = re.compile('[A-Z]{2,}\s')
brands = []
with open("producto_tabla.csv", "rw+") as f:
	for line in f:
		li = re.findall(p,line)
		brands.append(' '.join(map(str.strip, li)))
print brands

