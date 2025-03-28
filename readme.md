# Sync files in one way
### Description
This is a program that synchronizes two folders: source and
replica. The program maintain a full, identical copy of source
folder at replica folder. The synchronization process runs at a set interval, which can be customized.

It also logs all actions (file copies, deletions, folder creations) to a specified log file, allowing you to track the changes made during each synchronization.

## Features

+ Sync files and folders: Copies new or updated files from the source to the replica folder.

+ Delete extra files: Removes files in the replica folder that no longer exist in the source folder.

+ MD5 hash check: Ensures files are only copied if their contents have changed, not just their names.

+ Customizable synchronization interval: Set how frequently the synchronization process runs.

+ Logging: Keeps a log of all actions taken (e.g., files copied, folders created, files removed).

+ Recursive folder synchronization: Syncs nested folders as well.

## Usage
### Command-line Arguments
To run the script, use the following command in the terminal or command prompt:
```Bash
python sync_folders.py -s or --source <source_folder_path> -r or --replica <replica_folder_path> [-i or --interval <seconds>] [-l or --log_file <log_file_path>]

```
### Arguments
 - `-s` or `--source` (**required**) - Path to the source folder. This folder will be mirrored in the replica folder.
 - `-r` or `--replica`(**required**)  - Path to the replica folder. This folder will be updated to match the source.
 - `-i` or `--interval`(**Optional, default is 30s**): The interval (in seconds) between each synchronization. Set how often the synchronization should run automatically.
 - `-l` or `--log_file`(optional, default: `sync_log.txt`): Path to the log file where synchronization actions will be recorded.

### Example Usage:

#### 1. Basic usage (sync every 30 seconds and log actions in sync_log.txt):
```bash
python sync_folders.py --source /path/to/source --replica /path/to/replica

```

#### 2. Custom interval (e.g., every 60 seconds):
```bash
python sync_folders.py --source /path/to/source --replica /path/to/replica --interval 60
```

#### 3. Custom log file:
```Bash
python sync_folders.py --source /path/to/source --replica /path/to/replica --log_file /path/to/logfile.txt
```
#### Example Output:
```bash
Starting synchronization...
Created replica folder: /path/to/replica
Copied/Updated file: /path/to/source/file.txt -> /path/to/replica/file.txt
Removed: /path/to/replica/old_file.txt
Synchronization complete. Next run in 30 seconds
```
## Functions
`calculate_md5(file_path)`

- **Description**: Calculates the MD5 hash of a file to compare its contents.

- **Parameters**:

    - `file_path (str)`: The path to the file to calculate the MD5 hash.

- **Returns**: The MD5 hash of the file as a hexadecimal string.

`log_message(message, log_file)`
- **Description**: Logs a message to a log file and also prints it to the console.

- **Parameters**:
message (str): The message to log.

log_file (str): The path to the log file where the message will be written.

`sync_folders(source, replica, log_file)`

 - **Description**: Synchronizes the contents of the source folder with the replica folder. It copies new or updated files and removes files that are no longer in the source folder.

 - **Parameters**:

    - source (str): The path to the source folder.

    - replica (str): The path to the replica folder.

    - log_file (str): The path to the log file.

`main()`
- **Description**: The main entry point of the script. It parses command-line arguments and runs the synchronization process in an infinite loop with a defined interval.

## Error Handling
- If the source folder does not exist, the script will print an error message and exit.

- If the replica folder does not exist, the script will print an error message and exit.