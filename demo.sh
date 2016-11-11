#!/bin/bash

function demo() {
 path=$1
 dir=$2
 cmd=$3

 echo "-s $path:thomas:thomas:$dir:'$cmd'"
 
}

function cleanexit() {
  echo
  kill $shellinabox
  echo kill $shellinabox shellinabox
  kill $demo
  echo kill $demo demo
}


trap cleanexit HUP TERM EXIT KILL
#APP=$(demo tmux /home/thomas/github "/usr/bin/tmux attach-session -t demo")
#APP="$APP $(demo third /home/thomas/github)"


shellinaboxd --localhost-only \
  --user-css demo:+demo.css \
  --disable-ssl \
  --port 8081 \
  -s 'tmux:thomas:thomas:/home/thomas/github:/usr/bin/tmux attach-session -t git' >demo.log 2>&1 &
shellinabox=$!
export shellinabox

if [ $? != 0 ]; then
  echo "problem running shellinabox"
  exit
fi
echo "shellinabox running"

./demo.py >demo.log 2>&1 &
demo=$!
export demo

if [ $? != 0 ]; then
  echo "problem running python"
  exit
fi
echo "python running"

wait $shellinabox
echo "shellinabox done"

wait $demo
echo "done demo"
