class Bug:
    def __init__(self, bug_id, title, description, severity, status="Open"):
        self.bug_id = bug_id
        self.title = title
        self.description = description
        self.severity = severity
        self.status = status

    def validate_report(self):
        missing_fields = []

        if self.title == "":
            missing_fields.append("title")
        if self.description == "":
            missing_fields.append("description")
        if self.severity == "":
            missing_fields.append("severity")

        if missing_fields:
            return f"Error: The bug report is missing data in the following field(s): '{', '.join(missing_fields)}'."
        else:
            return "VALID"


def read_bug_data(file_path):
    data_list = []

    with open(file_path, "r") as f:
        for line in f:
            parts = line.strip().split(",")
            data_list.append(parts)

    return data_list


def process_and_save_report(data_list, output_file):
    with open(output_file, "w") as f:
        for entry in data_list:
            bug = Bug(entry[0], entry[1], entry[2], entry[3])
            status = bug.validate_report()
            f.write(f"Bug ID {bug.bug_id}: {status}\n")
