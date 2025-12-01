from bug_model import read_bug_data, process_and_save_report

# Step 1: Read input file
data_list = read_bug_data("bugs.txt")

# Step 2: Process and save validation report
process_and_save_report(data_list, "output.txt")

print("✔ Bug validation completed. Check output.txt.")
