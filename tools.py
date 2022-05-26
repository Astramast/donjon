def extract(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        raw = f.readlines()
    for i in range(len(raw)):
        raw[i] = raw[i].strip()
        raw[i] = raw[i].split()

    lines = len(raw)
    columns = len(raw[0])

    matrix = [[0 for i in range(lines)] for j in range(columns))]
    for i in range(lines):
        for j in range(columns):
            matrix[i][j] = int(raw[i][j])

    return matrix
