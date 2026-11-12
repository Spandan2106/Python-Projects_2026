class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_word = False


class Autocomplete:

    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):

        current = self.root

        for char in word.lower():
            if char not in current.children:
                current.children[char] = TrieNode()

            current = current.children[char]

        current.is_word = True

    def search(self, prefix):

        current = self.root
        prefix = prefix.lower()

        for char in prefix:

            if char not in current.children:
                return []

            current = current.children[char]

        results = []

        def collect(node, word):

            if node.is_word:
                results.append(word)

            for char in sorted(node.children):
                collect(node.children[char], word + char)

        collect(current, prefix)

        return results[:10]


autocomplete = Autocomplete()

words = [
    "python", "pytorch", "programming",
    "program", "project", "java",
    "javascript", "json", "database"
]

for word in words:
    autocomplete.add_word(word)

while True:

    prefix = input("\nEnter prefix (exit to stop): ")

    if prefix.lower() == "exit":
        break

    print("Suggestions:", autocomplete.search(prefix))
