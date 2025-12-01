1.	Read json file, parse data

  Problem Statement:
                  Read intf.json file & parse provided details. Program to handle exception if key not found
  Details to be check:
Interface name, type, ipv4 address, prefix length,  Counters: in octets, in unicast pkts,  out octets, out unicast pkts

Expected Output 
     name : swp1
     type: interface
     Ipv4 address: 10.1.1.1
     Prefix length: 24
     in octets: 232334
     in unicast pkts: 3234324
     out octets: 1212123
     out unicast pkts: 435345
                 Json input — Refer intf.json(attached)

2. Log file analyzer
            Problem Statement:
                 Read log file & extract debug, error, critical log messages. Use regex to search these details
           Pattern to check — [DEBUG, ERROR, CRITICAL]
            Output — Create 3 log file (debug.log, error.log, critical.log) & add log messages
            Log file — Refer feature.log(attached)

3. Python OOP Challenge: File-Based Bug Report & Validation
Problem statement:
     Design a Python Object-Oriented Programming (OOP) model using a Bug class to structure bug reports. You must create the Bug class and then write the necessary functions to read bug data from an input file and save the validation results to an output file.
     Class Create the class Bug (same structure as before: attributes: bug_id, title, description, severity; default status='Open').
     Implement the method validate_report(self). It must check that title, description, and severity are not empty strings (""). It should return a status string (either "VALID" or an error message detailing the missing fields), rather than just printing.
                     Create a standalone function, read_bug_data(file_path), that reads a plain text file. Assume each line contains comma-separated bug data in the order: bug_id, title, description, severity. This function should parse the data and return a list of dictionaries or tuples, ready for processing.
     Create a standalone function, process_and_save_report(data_list, output_file). This function must iterate through the list of bug data, create a Bug object for each entry, call the validate_report() method, and write the final result (Bug ID + Validation Status) to the specified output_file.

Sample Input
101,Login button misaligned,The 'Sign In' button overlaps the 'Forgot Password' link on mobile view.,Medium
102,Crash on Checkout,,High
103,Broken link on FAQ,Link to payment options returns 404.,
104,Sidebar always visible,Sidebar is sticky on all pages.,Low

Sample output
Bug ID 101: VALID
Bug ID 102: Error: The bug report is missing data in the following field(s): 'description'.
Bug ID 103: Error: The bug report is missing data in the following field(s): 'severity'.
Bug ID 104: VALID

4. Design a Python OOP model for a Smart Vehicle Control System using multi-level inheritance and mixins. You must create a base class Vehicle that defines the methods start() and stop(). Then create a subclass Car that inherits from Vehicle and adds a new feature method play_music(). Next, implement two mixins: an ElectricMixin that overrides the start() method to perform a battery check before starting and then calls super().start(), and an AutopilotMixin that also overrides the start() method to run sensor calibration and then calls super().start(). Finally, create a class Tesla using multiple inheritance in the order class Tesla(AutopilotMixin, ElectricMixin, Car).
5. Remote Resource Monitor + Local Alert
 
VM: 10.81.1.116(interns/123123)
Connect every 5 seconds
 
Collect below:
                CPU usage - top -bn1 | head -5
                Memory usage - free -m
                Disk usage - df -h | tail -1
If CPU > 80% OR disk > 90%, write alert to a local log.
 
Extra Challenge:
Use a persistent Paramiko channel (invoke_shell).
6. Multi-Threaded Image File Split & Merge (10 MB txt)
Problem Statement:
You are given a 10 MB txt named:
10mb-examplefile-com.txt(attached)
Write a multithreaded program that:
1. Splits the txt file into 1 MB chunks
2. Saves each chunk as a separate file
3. Uses multiple threads to merge the chunks back
4. Verify the final txt is identical to the original
