# ImageConverter
Simple commandline image patch converter and thumbnail maker that uses settings file and commandline arguments for extra functionality. Can make Thumb, S/M/L file versions and change image filetype 


Also provides thumbnail, medium and large file size conservions for platforms like WordPress

Can either use console parameters or a json settings file to provide default values / extra functionality that is desired

-t | --thumb                Generates thumbnail file (default 300x300) with suffix _thumb
-s | --small                Generates Small file (default 300x300) with suffix _s
-m | --medium               Generates Medium file (default 300x300) with suffix _m
-l | --large                Generates Large file (default 1024x1024) with suffix _l
st:'%size%'                 Define custom square size for thumbnail file
ss:'%size%'                 Define custom square size for small file
sm:'%size%'                 Define custom square size for medium file
sl:'%size%'                 Define custom square size for large file
from:'%file_type%'          Converts files from the requested type e.g.: from:'.jpg'
to:'%file_type%'            Converts files to the requested type e.g.: to:'.png'
f:'%directory_path%'        Allow you to define the path to the directory where you want to convert
