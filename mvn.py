import os
import subprocess

def compile_maven_projects(base_directory):
    for item in os.listdir(base_directory):
        item_path = os.path.join(base_directory, item)

        if os.path.isdir(item_path) and os.path.exists(os.path.join(item_path, 'pom.xml')):
            print(f"Compiling Maven project in: {item_path}")

            result = subprocess.run(['mvn', 'compile'], cwd=item_path, capture_output=True, text=True)

            if result.returncode == 0:
                print(f"Compilation successful for {item_path}")
            else:
                print(f"Compilation failed for {item_path}")
                print(result.stderr)

base_directory = '/path/to/your/projects'

compile_maven_projects(base_directory)
