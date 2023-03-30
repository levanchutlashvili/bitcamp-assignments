import sys

def line_arguments(arguments):
    if len(arguments) < 2:
        sys.exit("Too few command-line arguments")
    if len(arguments) > 2:
        sys.exit("Too many command-line arguments")
    
    if arguments[1].split(".")[1] != "py":
        sys.exit("Not a Python file")

    try:
        file = open(arguments[1], "r")
    except:
        sys.exit("File does not exist")

    return file   

def count_lines(file_path):
    try:
        with open(file_path, 'r') as f:
            lines = f.readlines()
        count = 0

        for line in lines:
            line = line.strip()
            if not line:
                continue
            if line.startswith('#'):
                continue 
            count += 1
            return count
    except FileNotFoundError:
              sys.exit('File does not exist') 

def main(arguments):
    file_path = line_arguments(arguments)
    
    print(count_lines(file))

if __name__ == "__main__":
    main(sys.argv)                              