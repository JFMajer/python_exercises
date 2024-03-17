from pathlib import Path


def reverse_lines(filename: str, output_filename: str):
    path = Path(filename)
    output_path = Path(output_filename)
    with path.open(mode='r') as f, output_path.open(mode='w') as o:
        for line in f:
            o.write(f'{line.rstrip()[::-1]}\n')



reverse_lines("files/lines.txt", "files/lines_output.txt")

