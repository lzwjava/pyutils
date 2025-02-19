import os
import subprocess
import argparse

def compile_maven_projects(base_directory, log_directory="mvn_logs", maven_options=None):
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

    for item in os.listdir(base_directory):
        item_path = os.path.join(base_directory, item)

        if os.path.isdir(item_path) and os.path.exists(os.path.join(item_path, 'pom.xml')):
            print(f"Compiling Maven project in: {item_path}")
            log_file_path = os.path.join(log_directory, f"{item}.log")

            mvn_command = ['mvn', 'compile', '-X', '-f', os.path.join(item_path, 'pom.xml')]
            if maven_options:
                mvn_command.extend(maven_options.split())

            try:
                # Normalize paths to forward slashes
                mvn_command = [path.replace("\\", "/") for path in mvn_command]

                result = subprocess.run(mvn_command, cwd=item_path, capture_output=True, text=True, check=True)
                with open(log_file_path, "w") as log_file:
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

def main():
    parser = argparse.ArgumentParser(description="Compile Maven projects.")
    parser.add_argument("username", type=str, help="The username for the base directory path.")
    parser.add_argument("--project_name", type=str, default="projectname", help="The name of the project directory under Projects/.")
    parser.add_argument("--log_subdirectory", type=str, default="mvn_compile_logs", help="The subdirectory under Projects/ to store compilation logs.")
    parser.add_argument("--maven_options", type=str, default="-Dversion=1.1", help="Maven options to pass to the compile command.")

    args = parser.parse_args()

    # Use os.path.join to create paths with correct separators
    base_directory = os.path.join('C:', 'Users', args.username, 'Projects', args.project_name)
    log_directory = os.path.join('C:', 'Users', args.username, 'Projects', args.log_subdirectory)
    maven_options = args.maven_options

    compile_maven_projects(base_directory, log_directory, maven_options)

if __name__ == "__main__":
    main()
