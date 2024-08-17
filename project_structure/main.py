# import site

# print(site.getsitepackages())

# import sys

# for path in sys.path:
#     print(path)

from pipeline.extract import extract_from_excel

print(extract_from_excel('data/input'))