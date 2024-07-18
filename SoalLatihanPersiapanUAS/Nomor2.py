def count_lines(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            if not lines:
                print("File is empty.")
                return
            line_count = {}
            for line in lines:
                line = line.strip()
                if line in line_count:
                    line_count[line] += 1
                else:
                    line_count[line] = 1
            for line, count in line_count.items():
                print(f"{line} {count}")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")