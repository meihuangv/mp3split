from subprocess import Popen, PIPE

with open('input.txt') as file:
    lines = file.readlines()
    print(lines)
    i = 1
    for l in lines:
       start = l.split('-')[0]
       end = l.split('-')[1].rstrip()
       p=Popen(["ffmpeg", "-y", "-i", "REC2726.mp3", "-c:a","copy","-ss", start, "-to", end, f'{i}.mp3'], stdout=PIPE)
       i = i + 1
