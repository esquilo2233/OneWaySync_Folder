import os
import shutil
import sys
import time
import hashlib
import argparse

def calculate_md5(file_path):
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def log_message(message, log_file):
    print(message)
    with open(log_file, "a") as log:
        log.write(message + "\n")



def sync_folders(source, replica, log_file):
    
    # Verifies if the Folder replica exists, if not it creates it and logs it on the log file
    if not os.path.exists(replica):
        os.makedirs(replica) 
        log_message(f"Created replica folder: {replica}", log_file)
    
    
    source_files = set(os.listdir(source))
    replica_files = set(os.listdir(replica))
    
    for file in source_files:
        src_path = os.path.join(source, file)
        rep_path = os.path.join(replica, file)
        
        if os.path.isdir(src_path):
            sync_folders(src_path, rep_path, log_file)
        else:
            if file not in replica_files or calculate_md5(src_path) != calculate_md5(rep_path):
                shutil.copy2(src_path, rep_path)
                log_message(f"Copied/Updated file: {src_path} -> {rep_path}", log_file)
    
    # Remove extra files in replica
    for file in replica_files - source_files:
        rep_path = os.path.join(replica, file)
        if os.path.isdir(rep_path):
            shutil.rmtree(rep_path)
        else:
            os.remove(rep_path)
        log_message(f"Removed: {rep_path}", log_file)

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Synchronize source and replica folders.")
    parser.add_argument("-s","--source", required=True, help="Path to the source folder.")
    parser.add_argument("-r","--replica", required=True, help="Path to the replica folder.")
    parser.add_argument("-i","--interval", type=int, default=30, help="Interval (in seconds) between synchronizations.")
    parser.add_argument("-l","--log_file", default="sync_log.txt", help="Path to the log file.")
    
    args = parser.parse_args()
    
    source = args.source
    replica = args.replica
    logFile= args.log_file
    interval=args.interval
    
    # Check if source and replica folders exist
    if not os.path.exists(source):
        print(f"ERROR: Source folder '{source}' does not exist.")
        sys.exit(1)
    if not os.path.exists(replica):
        print(f"ERROR: Replica folder '{replica}' does not exist.")
        sys.exit(1)
    
    while True:
        log_message("Starting synchronization...", args.log_file)
        sync_folders(source, replica, logFile)
        log_message(f"Synchronization complete. Next run in {args.interval} seconds.", logFile)
        time.sleep(interval)

if __name__ == "__main__":
    main()
