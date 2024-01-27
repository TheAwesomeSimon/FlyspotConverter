import glob, os, subprocess, sys

def convert_avi_to_mp4(file):
    output = file.rsplit('.', maxsplit=1)[0] + '.mp4'
    subprocess.call(['ffmpeg', '-i', file, '-strict', '-2', output])
    return True

def delete_file(file):
    os.remove(file)

def get_arguments():
    args = sys.argv
    args.pop(0)
    return args

def convert(file):
    convert_avi_to_mp4(file)
    delete_file(file)

def main():
    args = get_arguments()
    if len(args) == 0:
        args.append("centerline")
        args.append("desk")
    print(args)
    converted = 0
    deleted = 0

    os.chdir("/Users/I344396/Documents/Flyspot/")
    
    for file in glob.glob("*.avi"):
        if any(substr in file for substr in args):
            convert(file)
            converted += 1
        else:
            delete_file(file)
            deleted += 1

    print("Converted: " + str(converted))
    print("Deleted: " + str(deleted))

main()