
data = '''
	BTW	91001	super	2020-01-01 00:00:00.000	super               	2020-01-01 00:00:00.000
	BTW	48131	super	2020-01-01 00:00:00.000	super               	2020-01-01 00:00:00.000
		"
# functions
def inputs(prompt: str = """") -> str:
   data = """"
   chunk = input(prompt)
   while chunk != """" and chunk != BR:
       data += chunk + BR
       chunk = input()
   return data
"		"
# functions
def inputs(prompt: str = """") -> str:
   data = """"
   chunk = input(prompt)
   while chunk != """" and chunk != BR:
       data += chunk + BR
       chunk = input()
   return data
"	""""""""""	yes
			"
# functions
def inputs(prompt: str = """") -> str:
   data = """"
   chunk = input(prompt)
   while chunk != """" and chunk != BR:
       data += chunk + BR
       chunk = input()
   return data
"

'''

import lib
print(lib.excel2grid(data))

# length = len(data)
# grid = []
# row = []
# cell = ''
# # for escape detection
# char1 = ''
# char2 = ''
# multiline = True # if multiline, line break and tabulation will not move to next cell or row
# for i in range(length):
#     char1 = char2
#     char2 = data[i]

#     print(f'{'multil' if multiline else 'single'}: {char2}')

#     if char1 == '	' and char2 == '"':
#         multiline = char2 != '"'

#     if not multiline and (char2 == "	" or char2 == "\n"):
#         row.append(cell)
#         cell = ''
#         if char2 == "\n":
#             grid.append(row)
#             row = []
#     else:
#         cell += char2
# grid.append(row)
# print(grid)
