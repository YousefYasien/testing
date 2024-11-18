from tqdm import tqdm

def merge_files(file1, file2, output_file):
    # Use a set to store unique lines
    unique_lines = set()

    # Read lines from the first file with UTF-8 encoding
    with open(file1, 'r', encoding='utf-8') as f1:
        lines1 = f1.readlines()
        for line in tqdm(lines1, desc=f'Reading {file1}', unit='line'):
            unique_lines.add(line.strip())  # Strip whitespace and add to the set

    # Read lines from the second file with UTF-8 encoding
    with open(file2, 'r', encoding='utf-8') as f2:
        lines2 = f2.readlines()
        for line in tqdm(lines2, desc=f'Reading {file2}', unit='line'):
            unique_lines.add(line.strip())  # Strip whitespace and add to the set

    # Write the unique lines to the output file with UTF-8 encoding
    with open(output_file, 'w', encoding='utf-8') as out_file:
        for line in tqdm(unique_lines, desc=f'Writing to {output_file}', unit='line'):
            out_file.write(line + '\n')  # Write each unique line to the output file

# Example usage
merge_files('./passwords.txt', './hk_hlm_founds.txt', 'passwords_2.txt')