def longestPath(fileSystem):
    # EX. "user\n\tpictures\n\t\tphoto.png\n\t\tcamera\n\tdocuments\n\t\tlectures\n\t\t\tnotes.txt"
    # --> "user/documents/lectures/notes.txt" --> 33
    fileSystem = fileSystem.split("\f")
    path, ans, total = [], 0, 0
    for line in fileSystem:
        tabs = line.count('\t')
        while len(path) > tabs: total -= path.pop() # len(path) represents the levels of the path
        path.append(len(line) - tabs)
        total += path[-1]
        if '.' in line: ans = max(ans, total + (len(path) - 1)) # len(path) - 1 is the number of tabs that are added
    return ans
        