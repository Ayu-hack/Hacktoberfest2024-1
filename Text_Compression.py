# Node class to store characters and their frequencies
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    def __lt__(self, other):
        return self.freq < other.freq

# Function to calculate frequencies of characters in the given text
def calculate_frequencies(text):
    freq = {}
    for char in text:
        if char not in freq:
            freq[char] = 0
        freq[char] += 1
    return freq

# Function to build the Huffman Tree
def build_huffman_tree(frequencies):
    nodes = [Node(char, freq) for char, freq in frequencies.items()]
    while len(nodes) > 1:
        nodes = sorted(nodes, key=lambda x: x.freq)
        left = nodes.pop(0)
        right = nodes.pop(0)
        new_node = Node(None, left.freq + right.freq)
        new_node.left = left
        new_node.right = right
        nodes.append(new_node)
    return nodes[0]

# Function to generate the Huffman Codes by traversing the tree
def generate_huffman_codes(node, current_code="", codes={}):
    if node is None:
        return
    if node.char is not None:
        codes[node.char] = current_code
    generate_huffman_codes(node.left, current_code + "0", codes)
    generate_huffman_codes(node.right, current_code + "1", codes)
    return codes

# Function to encode the text using the Huffman Codes
def encode_text(text, huffman_codes):
    encoded_text = ""
    for char in text:
        encoded_text += huffman_codes[char]
    return encoded_text

# Function to decode the encoded text back to the original text
def decode_text(encoded_text, root):
    decoded_text = ""
    current_node = root
    for bit in encoded_text:
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right
        if current_node.char is not None:
            decoded_text += current_node.char
            current_node = root
    return decoded_text

# Main function to execute Huffman Coding
def huffman_coding(text):
    frequencies = calculate_frequencies(text) #Step 1
    huffman_tree_root = build_huffman_tree(frequencies) #Step2
    huffman_codes = generate_huffman_codes(huffman_tree_root) #Step3
    encoded_text = encode_text(text, huffman_codes) #Step4
    decoded_text = decode_text(encoded_text, huffman_tree_root) #Step5
    print("Original Text:", text)
    print("Character Frequencies:", frequencies)
    print("Huffman Codes:", huffman_codes)
    print("Encoded Text:", encoded_text)
    print("Decoded Text:", decoded_text)

sample_text = "BCAADDDCCACACAC"
huffman_coding(sample_text)
