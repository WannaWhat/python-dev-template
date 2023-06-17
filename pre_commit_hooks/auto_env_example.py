#
# Code generate by ChatGPT

import os


def main():
    # Determining the path to the folder with .env files based on the directory from which the script is run
    current_directory = os.getcwd()
    folder_path = os.path.join(current_directory, 'configs')
    # Getting a list of files .env in the folder
    env_files = [filename for filename in os.listdir(folder_path) if filename.endswith('.env')]

    for env_file in env_files:
        env_file_path = os.path.join(folder_path, env_file)
        env_example_path = os.path.join(folder_path, env_file.replace('.env', '.env.example'))

        with open(env_file_path, 'r') as file:
            lines = file.readlines()

        with open(env_file_path, 'w') as file:
            for line in lines:
                stripped_line = line.strip().replace(' ', '')  # Remove spaces
                file.write(stripped_line + '\n')

        with open(env_example_path, 'w') as file:
            for line in lines:
                stripped_line = line.strip()
                if stripped_line and '=' in stripped_line and ' ' not in stripped_line:
                    key = stripped_line.split('=')[0].strip()
                    file.write(f'{key}=\n')
                else:
                    file.write('\n')


if __name__ == '__main__':
    main()
