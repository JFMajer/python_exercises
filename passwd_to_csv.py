from pathlib import Path
import csv


def passwd_to_csv(filename: str = '/etc/passwd', output_filename: str = 'files/output.csv') -> None:
    path = Path(filename)
    output_path = Path(output_filename)
    try:
        with path.open(mode='r') as f, output_path.open(mode='w') as o:
            csv_writer = csv.writer(o, delimiter='\t')
            for line in f:
                if not line or line.startswith('#'):
                    continue
                splitted = line.split(':')
                if len(splitted) > 2:
                    csv_writer.writerow([splitted[0], splitted[2]])
    except FileNotFoundError:
        print("Provided filename could not be found")


passwd_to_csv()

