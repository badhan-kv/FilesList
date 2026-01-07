# Copyright (c) 2026 Khushaldas Vasant Badhan
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.

import os

def list_files_recursively(target_paths, extensions, output_log=None):
    """
    Lists all files with specific extensions from provided directories 
    and their subfolders. Optionally saves the list to a file.
    """
    
    # 1. Normalize inputs to lists
    if isinstance(target_paths, str):
        target_paths = [target_paths]
    if isinstance(extensions, str):
        extensions = [extensions]

    # 2. Normalize extensions (lowercase, ensure dot prefix)
    clean_exts = []
    for ext in extensions:
        clean_ext = ext.lower()
        if not clean_ext.startswith('.'):
            clean_ext = '.' + clean_ext
        clean_exts.append(clean_ext)
    
    # Convert to tuple for endswith() compatibility
    clean_exts = tuple(clean_exts)
    
    found_files = []

    print(f"--- Starting Search ---")
    print(f"Looking for: {clean_exts}")
    print("-" * 30)

    # 3. Walk through directories
    for folder_path in target_paths:
        if not os.path.exists(folder_path):
            print(f"[!] Warning: Directory not found -> {folder_path}")
            continue

        for root, dirs, files in os.walk(folder_path):
            for filename in files:
                # Check extension (case insensitive)
                if filename.lower().endswith(clean_exts):
                    full_path = os.path.join(root, filename)
                    found_files.append(full_path)
                    print(full_path)

    # 4. Summary and Output
    print("-" * 30)
    print(f"Search Complete.")
    print(f"Total files found: {len(found_files)}")

    # 5. Optional: Save to file
    if output_log and found_files:
        try:
            with open(output_log, 'w', encoding='utf-8') as f:
                f.write(f"Search results for {clean_exts}:\n")
                for path in found_files:
                    f.write(f"{path}\n")
            print(f"List saved to: {output_log}")
        except Exception as e:
            print(f"Error saving log file: {e}")

# ==========================================
# Configuration Area
# ==========================================
if __name__ == "__main__":
    
    # 1. Directories to search
    search_directories = [
        r"C:\Users\User\Folder"
    ]

    # 2. Extensions to find
    target_extensions = [".cpp"]

    # 3. (Optional) Save the list to a text file? 
    # Set to None if you don't want a file created.
    # Example: log_file = "found_files.txt"
    log_file = None 

    # Run the function
    list_files_recursively(search_directories, target_extensions, log_file)
