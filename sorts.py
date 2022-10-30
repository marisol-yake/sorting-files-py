import os
import time


def main():
    cwd = os.getcwd()
    print("Preparing files for sorting...")
    print()
    time.sleep(2)

    # For all files in the current directory
    for filename in os.listdir(cwd):
        time.sleep(1)
        date_mod_obj = time.localtime(os.path.getmtime("./" + filename))
        year_dir = "/".join([cwd, str(date_mod_obj.tm_year)])
        
        print(f"File name: {filename}, Year (of last mod): {date_mod_obj.tm_year}")
        
        # If folder for year does not exist
        if not os.path.isdir(year_dir):
            # Make folder for year
            os.mkdir(year_dir)
            
        # Move file into folder for year
        os.replace((cwd + "/" + filename), (year_dir + "/" + filename))

    time.sleep(2)
    print()
    print("Job completed successfully!")

if __name__ == "__main__":
    main()