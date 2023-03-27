import heapq
from collections import defaultdict
import os 


src = r"C:\Users\aacas\OneDrive\Desktop\Aacash\Github Files\TCT Analysis\SampleTextFiles"

# to map each character its huffman value
codes = {}

# To store the frequency of character of the input data
freq = defaultdict(int)

# A Huffman tree node
class MinHeapNode:
	def __init__(self, data, freq):
		self.left = None
		self.right = None
		self.data = data
		self.freq = freq

	def __lt__(self, other):
		return self.freq < other.freq

# utility function to print characters along with
# there huffman value
def printCodes(root, str):
	if root is None:
		return
	if root.data != '$':
		print(root.data, ":", str)
	printCodes(root.left, str + "0")
	printCodes(root.right, str + "1")

# utility function to store characters along with
# there huffman value in a hash table
def storeCodes(root, str):
	if root is None:
		return
	if root.data != '$':
		codes[root.data] = str
	storeCodes(root.left, str + "0")
	storeCodes(root.right, str + "1")

# function to build the Huffman tree and store it
# in minHeap
def HuffmanCodes(size):
	global minHeap
	for key in freq:
		minHeap.append(MinHeapNode(key, freq[key]))
	heapq.heapify(minHeap)
	while len(minHeap) != 1:
		left = heapq.heappop(minHeap)
		right = heapq.heappop(minHeap)
		top = MinHeapNode('$', left.freq + right.freq)
		top.left = left
		top.right = right
		heapq.heappush(minHeap, top)
	storeCodes(minHeap[0], "")

# utility function to store map each character with its
# frequency in input string
def calcFreq(str, n):
	for i in range(n):
		freq[str[i]] += 1

# function iterates through the encoded string s
# if s[i]=='1' then move to node->right
# if s[i]=='0' then move to node->left
# if leaf node append the node->data to our output string
def decode_file(root, s):
	ans = ""
	curr = root
	n = len(s)
	for i in range(n):
		if s[i] == '0':
			curr = curr.left
		else:
			curr = curr.right

		# reached leaf node
		if curr.left is None and curr.right is None:
			ans += curr.data
			curr = root
	return ans + '\0'


def write_file(encodedString):
	codeCopy = int(encodedString, 2)
	hexCode = []
	while codeCopy:
		hexCode.insert(0, codeCopy % 256)
		codeCopy //= 256

	k2 = bytes(hexCode)
	
	with open(src+r"\outout.txt", "wb") as key:
		key.write(k2)

def save_code(codes):
	val = list(codes.values())
	car= list(codes.keys())
	

	tre=''+val[0]+'1'+car[0]
	for i in range (1,len(val)):
		fir=val[i-1]
		now=val[i]
		if (len(now)>len(fir)):
			tre+='0'*(len(now)-len(fir))
		tre+='1'+car[i]

	# print(tre)

	cods={}

	i=0
	cod=''
	while(i<len(tre)):
		if(tre[i]=='0'):
			cod+='0'
	
		elif (tre[i]=='1' ):
			i+=1
			cods[tre[i]]=cod

			if (tre[i-1]!='0'):
				
				if (cod[-1]=='0'):
					cod=cod[:-1]+'1'

				while (cod[-1]=='1' and ('0' in cod)):
					cod=cod[:-1]
				
			# print(cod)	


		i+=1

	
	with open(src+r"\tre.txt", "w") as key:
		key.write(tre)


	# Driver code
if __name__ == "__main__":
	minHeap = []
	with open(src+r"\TwoHundredWords\one.txt", "r") as inputFile:
		str = inputFile.read()
		
	# print(str)
	encodedString, decodedString = "", ""
	calcFreq(str, len(str))
	HuffmanCodes(len(str))
	save_code(codes)
	
	for i in str:
		encodedString += codes[i]

	write_file('1'+encodedString)

	input_file_size = os.path.getsize(src+r"\TwoHundredWords\one.txt")
	print("Input file size is: ", input_file_size, "bytes")
	output_file_size = os.path.getsize((src+r"\outout.txt"))
	# print("Output file size is: ", output_file_size, "bytes")
	tree_file_size = os.path.getsize((src+r"\tre.txt"))
	# print("tree file size is: ", tree_file_size, "bytes")
	print("Total Output file size is: ", output_file_size+tree_file_size, "bytes")

	# Function call
	# huffCode = read_file()
	# decodedString = decode_file(minHeap[0], huffCode)
	# print("\nDecoded Huffman Data:")
	# print(decodedString)