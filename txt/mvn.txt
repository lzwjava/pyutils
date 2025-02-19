import os
import subprocess

def compile_maven_projects(base_directory, log_directory="mvn_logs", maven_options=None):
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

    for item in os.listdir(base_directory):
        item_path = os.path.join(base_directory, item)

        if os.path.isdir(item_path) and os.path.exists(os.path.join(item_path, 'pom.xml')):
            print(f"Compiling Maven project in: {item_path}")
            log_file_path = os.path.join(log_directory, f"{item}.log")

            mvn_command = ['mvn', 'compile', '-X']
            if maven_options:
                mvn_command.extend(maven_options.split())

            try:
                with open(log_file_path, "w") as log_file:
                    result = subprocess.run(mvn_command, cwd=item_path, capture_output=True, text=True, check=True)
                    log_file.write(result.stdout)
                    print(f"Compilation successful for {item_path}. Log saved to {log_file_path}")

            except subprocess.CalledProcessError as e:
                print(f"Compilation failed for {item_path}")
                print(e.stderr)
                if os.path.exists(log_file_path):
                    with open(log_file_path, "a") as log_file:
                        log_file.write(e.stderr)
            except Exception as e:
                print(f"An error occurred during compilation for {item_path}: {e}")

username = "username"
base_directory = f'/Users/{username}/Projects/projectname'  # Replace with the actual path to your projects
log_directory = f"/Users/{username}/Projects/mvn_compile_logs" # Replace with the desired log directory name
maven_options = '-Dversion=1.1' # Example usage of maven options
compile_maven_projects(base_directory, log_directory, maven_options)
