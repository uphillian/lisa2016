#!/bin/bash

function demo() {
 path=$1
 dir=$2
 cmd=$3

 echo "-s $path:thomas:thomas:$dir:'$cmd'"
 
}

#APP=$(demo tmux /home/thomas/github "/usr/bin/tmux attach-session -t demo")
#APP="$APP $(demo third /home/thomas/github)"


shellinaboxd --localhost-only \
  --user-css demo:+demo.css \
  --disable-ssl \
  -s 'tmux:thomas:thomas:/home/thomas/github:/usr/bin/tmux attach-session -t demo' &

python -m SimpleHTTPServer 8080 &
