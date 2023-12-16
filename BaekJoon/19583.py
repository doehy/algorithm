import sys
input = sys.stdin.readline

start , end , stream_end = input().split()
start = int(start[0:2] + start[3:])
end = int(end[0:2] + end[3:])
stream_end = int(stream_end[0:2] + stream_end[3:])

data = set()
result = 0
while True:
    try:
        time,name = input().split()
        time = int(time[0:2] + time[3:])
        if time <= start:
            if name not in data:
                data.add(name)
        elif end <= time <= stream_end:
            if name in data:
                data.remove(name)
                result += 1
    except:
        break

print(result)