import os
import subprocess

def compile_maven_projects(base_directory):
    # List all items in the base directory
    for item in os.listdir(base_directory):
        item_path = os.path.join(base_directory, item)

        # Check if the item is a directory and contains a pom.xml file
        if os.path.isdir(item_path) and os.path.exists(os.path.join(item_path, 'pom.xml')):
            print(f"Compiling Maven project in: {item_path}")

            # Run the 'mvn compile' command in the subdirectory
            result = subprocess.run(['mvn', 'compile'], cwd=item_path, capture_output=True, text=True)

            # Print the output of the mvn compile command
            if result.returncode == 0:
                print(f"Compilation successful for {item_path}")
            else:
                print(f"Compilation failed for {item_path}")
                print(result.stderr)

# Specify the base directory containing your Maven projects
base_directory = '/path/to/your/projects'

# Call the function to compile all Maven projects in the base directory
compile_maven_projects(base_directory)
