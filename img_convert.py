from PIL import Image
import os, sys
import json

def read_settings(settings_filename:str='settings.json'):
    '''
    Reads the settings defined in settings json file, use default settings.json if no other filename is provided
    '''
    with open(settings_filename, 'r') as settings_file:
        settings_data = json.load(settings_file)
        return settings_data

def main():
    '''
    Simple console app that uses python's image library to try to convert all files in the folder of given filetype to new filetype.
    
    Also provides thumbnail, medium and large file size conservions for platforms like WordPress

    Can either use console parameters or a json settings file to provide default values / extra functionality that is desired

    -t | --thumb                Generates thumbnail file (default 300x300) with suffix _thumb
    -s | --small                Generates Small file (default 300x300) with suffix _s
    -m | --medium               Generates Medium file (default 300x300) with suffix _m
    -l | --large                Generates Large file (default 1024x1024) with suffix _l
    -st:'%size%'                Define custom square size for thumbnail file
    -ss:'%size%'                Define custom square size for small file
    -sm:'%size%'                Define custom square size for medium file
    -sl:'%size%'                Define custom square size for large file
    from:'%file_type%'          Converts files from the requested type e.g.: from:'.jpg'
    to:'%file_type%'            Converts files to the requested type e.g.: to:'.png'
    f:'%directory_path%'        Allow you to define the path to the directory where you want to convert

    '''
    
    settings_data = read_settings()
        
    # DEFAULT SETTINGS
    THUMB_SIZE = (settings_data['THUMB_W'], settings_data['THUMB_H'])
    SMALL_SIZE = (settings_data['SMALL_W'], settings_data['SMALL_H'])
    MEDIUM_SIZE = (settings_data['MEDIUM_W'], settings_data['MEDIUM_H'])
    LARGE_SIZE = (settings_data['LARGE_W'], settings_data['LARGE_H'])

    file_type_from = settings_data['FILE_TYPE_FROM']
    file_type_to = settings_data['FILE_TYPE_TO']


    make_thumb = settings_data['MAKE_THUMB']
    make_small = settings_data['MAKE_SMALL']
    make_medium = settings_data['MAKE_MEDIUM'] 
    make_large = settings_data['MAKE_LARGE']

    directory = settings_data['DEFAULT_DIRECTORY']
    if directory == '':
        directory = os.curdir

    print(str(sys.argv))

    if len(sys.argv) > 0:
        for arg in sys.argv[1:]:
            print(arg)
            if arg in ['-t', '--thumb']:
                make_thumb = True
            elif arg in ['-s', '--small']:
                make_small = True
            elif arg in ['-m', '--medium']:
                make_medium = True
            elif arg in ['--large','-l']:
                make_large = True
            elif arg[0:3] == 'st:':
                size_t = int(arg.removeprefix('st:').strip())
                THUMB_SIZE = (size_t, size_t)
            elif arg[0:3] == 'ss:':
                size_s = int(arg.removeprefix('ss:').strip())
                SMALL_SIZE = (size_s, size_s)
            elif arg[0:3] == 'sm:':
                size_m = int(arg.removeprefix('sm:').strip())
                MEDIUM_SIZE = (size_m, size_m)
            elif arg[0:3] == 'sl:':
                size_l = int(arg.removeprefix('sl:').strip())
                LARGE_SIZE = (size_l, size_l)
            elif arg[0:2] == 'f:':
                directory = arg.removeprefix('f:').strip()
            elif arg[0:5] == 'from:':
                file_type_from = arg.removeprefix('from:').strip()
            elif arg[0:3] == 'to:':
                file_type_to = arg.removeprefix('to:').strip()


    for filename in os.listdir(directory):
        if filename.endswith(file_type_from):
            full_path = os.path.join(directory, filename)
            im = Image.open(full_path)
            prefix = full_path.replace(file_type_from, '')

            new_name = prefix + file_type_to
            rgb_im = im.convert('RGB')
            rgb_im.save(new_name)
            print(new_name)

            if make_thumb:
                thumb = rgb_im.copy()
                thumb.thumbnail(THUMB_SIZE)
                thumb_name =  prefix + '_thumb' + file_type_to
                thumb.save(thumb_name)
                print(thumb_name)
            if make_small:
                small = rgb_im.resize(SMALL_SIZE)
                small_name =  prefix + '_s' + file_type_to
                small.save(small_name)
                print(small_name)
            if make_medium:
                medium = rgb_im.resize(MEDIUM_SIZE)
                medium_name = prefix +'_m' + file_type_to
                medium.save(medium_name)
                print(medium_name)
            if make_large:
                large = rgb_im.resize(LARGE_SIZE)
                large_name = prefix +'_l' + file_type_to
                large.save(large_name)
                print(large_name)

            continue
        else:
            continue


if __name__ == '__main__':
    main()
