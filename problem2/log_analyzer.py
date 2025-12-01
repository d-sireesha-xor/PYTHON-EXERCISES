import re

def log_file_analyzer():
    # Regex patterns
    debug_pattern = r"\[DEBUG\]"
    error_pattern = r"\[ERROR\]"
    critical_pattern = r"\[CRITICAL\]"

    # Open log files for writing output
    debug_out = open("debug.log", "w")
    error_out = open("error.log", "w")
    critical_out = open("critical.log", "w")

    try:
        # Read input log file
        with open("feature.log", "r") as f:
            for line in f:
                # Check each type using regex
                if re.search(debug_pattern, line):
                    debug_out.write(line)
                elif re.search(error_pattern, line):
                    error_out.write(line)
                elif re.search(critical_pattern, line):
                    critical_out.write(line)

        print("✔ Log processing completed. Check output files.")

    except FileNotFoundError:
        print("Error: feature.log not found!")

    finally:
        debug_out.close()
        error_out.close()
        critical_out.close()


# Run the function
log_file_analyzer()
