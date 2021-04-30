#! /bin/bash

myDir='/home/noah/Documents/school/'
options=$(cd ${myDir} && /bin/ls -d */ | cut -d " " -f1)
arr=($options)

choice=$(echo -e "${options[@]}" | dmenu -i -p 'School: ')

#if [ "$choice" == ${arr[0]} ]; then 

#if [ "$choice" == ${arr[0]} ]; then 

if [ "$choice" == ${arr[2]} ]; then 
  exec ranger -c ${myDir}${arr[2]} && cd semester\ 2/ bindercheck2/'

#if [ "$choice" == ${arr[0]} ]; then 

#if [ "$choice" == ${arr[0]} ]; then 

#if [ "$choice" == ${arr[0]} ]; then 


fi
