import math
import os

def read_floats_from_file(folder, filename):
    """
    Reads a list of floats from a file located in a folder.
    Skips empty lines and warns about any non-numeric lines.
    """
    path = os.path.join(folder, filename)
    numbers = []
    with open(path, 'r') as file:
        for line_number, line in enumerate(file, 1):
            line = line.strip()
            if not line:
                continue  # skip blanks
            try:
                num = float(line)
                numbers.append(num)
            except ValueError:
                print(f"Warning: Skipping invalid number on line {line_number} in {filename}: '{line}'")
    return numbers

def compute_A_values(p, q, r):
    """
    For each triple (p_i, q_i, r_i), compute:
    A_i = ln(p_i + q_i^2) + sin(r_i * pi)
    If math fails (like log of negative), store a string error.
    """
    results = []
    for i, (pi, qi, ri) in enumerate(zip(p, q, r)):
        try:
            sum_val = pi + qi ** 2
            log_part = math.log(sum_val)
            sin_part = math.sin(ri * math.pi)
            result = log_part + sin_part
        except Exception as e:
            result = f"Error at index {i}: {e}"
        results.append(result)
    return results

def compute_B_values(s, t, u, v, x=1.5):
    """
    For each tuple (s_i, t_i, u_i, v_i), compute:
    B_i = exp(-s_i * t_i) + cos(u_i / (v_i + x))
    If division by zero or other math error, store a string error.
    """
    results = []
    for i, (si, ti, ui, vi) in enumerate(zip(s, t, u, v)):
        try:
            denom = vi + x
            if denom == 0:
                raise ZeroDivisionError("v_i + x is zero at index {}".format(i))
            exp_part = math.exp(-si * ti)
            cos_part = math.cos(ui / denom)
            result = exp_part + cos_part
        except Exception as e:
            result = f"Error at index {i}: {e}"
        results.append(result)
    return results

def write_results_to_file(folder, filename, results):
    """
    Writes results to a file in the given folder, one per line, as 'index: value'.
    Creates the folder if it does not exist.
    """
    if not os.path.exists(folder):
        os.makedirs(folder)
    path = os.path.join(folder, filename)
    with open(path, 'w') as file:
        for idx, value in enumerate(results):
            file.write(f"{idx}: {value}\n")

def main():
    # Define input and output folders
    input_folder = 'Input_file'
    output_folder = 'output_file_qno1'

    # Step 1: Read all input files from the input folder
    p = read_floats_from_file(input_folder, 'p.txt')
    q = read_floats_from_file(input_folder, 'q.txt')
    r = read_floats_from_file(input_folder, 'r.txt')
    s = read_floats_from_file(input_folder, 's.txt')
    t = read_floats_from_file(input_folder, 't.txt')
    u = read_floats_from_file(input_folder, 'u.txt')
    v = read_floats_from_file(input_folder, 'v.txt')

    # Step 2: Compute the A and B values using the given formulas
    A_results = compute_A_values(p, q, r)
    B_results = compute_B_values(s, t, u, v)

    # Step 3: Write the results to output files in the output folder
    write_results_to_file(output_folder, 'A.txt', A_results)
    write_results_to_file(output_folder, 'B.txt', B_results)

    print(f"All done! Results are in '{output_folder}/A.txt' and '{output_folder}/B.txt'.")

# This means: only run main() if this file is executed directly, not if imported.
if __name__ == "__main__":
    main()