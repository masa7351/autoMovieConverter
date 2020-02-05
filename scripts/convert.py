#! /usr/bin/python
#coding:utf-8

from os import listdir, makedirs, remove
from os.path import isfile, join
import subprocess
import shutil

path = '../'
converted_path = '../converted'
ffmpeg='/usr/local/bin/ffmpeg'
contents = [ f for f in listdir(path) if isfile(join(path, f))]

movies = []

lower = filter(lambda m: '.mov' in m, contents)
for f in lower:
    despaced = f.replace(' ', '\ ')
    movies.append(despaced)

makedirs(converted_path, exist_ok=True)
for movie in movies:
    inputFile = join(path, movie)
    outputFile = inputFile.replace('.mov', '.gif')
    command = '%s -i %s -r 24 %s\n' %(ffmpeg, inputFile, outputFile)
    subprocess.check_call(command, shell=True)
    shutil.move(outputFile.replace('\ ', ' '), converted_path)
    remove(inputFile.replace('\ ', ' '))
