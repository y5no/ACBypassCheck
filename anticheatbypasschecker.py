import os
import time

def find_files(filenames):
    found_files = []
    for current_dir, subdirs, files_list in os.walk("/", topdown=True):
        for filename in filenames:
            if filename in files_list:
                filepath = os.path.join(current_dir, filename)
                last_modified = time.ctime(os.path.getmtime(filepath))
                found_files.append((filename, filepath, last_modified))
    return found_files

def main():
    files_to_find = ["1v1.dll", "1v1.DevSettings.dll"]
    
    found_files = find_files(files_to_find)
    
    if found_files:
        print("=====================================================")
        print("            Anti-Cheat Bypass Checker                ")
        print("=====================================================")
        print("\nAntiCheat has been changed/bypassed and anticheat has been bypassed.")
        for file_info in found_files:
            print(f"File: {file_info[0]}\nDirectory: {file_info[1]}\nLast modified: {file_info[2]}\n")
        print("=====================================================")
        
        dll_mod_times = [file_info[2] for file_info in found_files]
        message = "same" if len(set(dll_mod_times)) == 1 else "different"
        print(f"\nAnalysis complete: '{files_to_find[0]}' and '{files_to_find[1]}' have been modified at {message} times/days.")
    else:
        print("=====================================================")
        print("             Anti-Cheat Bypass Checker               ")
        print("=====================================================")
        print("\nAnti-Cheat has not been modified.")

    input("\nPress Enter to exit.")

if __name__ == "__main__":
    main()
