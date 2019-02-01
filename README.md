# RakVideo-SDK-Python
Python API for the RAK Video modules, tested on RAK566

## Installation

Until Pypi publishing:

```bash
sudo pip install rak
```

## Usage

```python
from rak import RakDevice

# If you connect to the RAK567, the ip of the RAK566 (or other transmitters) is 192.168.100.100
# If you connect to the RAK566 (or other transmitters) directly, the ip will be 192.168.100.1
# RakDevice(self, ip, pipe, username="admin", password="admin"):
pipe0 = RakDevice("192.168.100.100", pipe=0, username='admin', password='admin')
pipe1 = RakDevice("192.168.100.100", pipe=1, username='admin', password='admin')

# Refresh force to read all the properties
pipe0.refresh()

# Show the pipe properties (refreshes only the data that is not yet read)
print(str(pipe0))

# Set the highest resolution (FHD) and quality for the pipe0
pipe0.resolution(3).quality(136).fps(30).gop(30)

# Disable pipe1 as nothing is connected by default on the RAK566
pipe1.resolution(0).quality(5).fps(1).gop(1)
```

## Credits

- [@AlexisTM](http://github.com/AlexisTM) - AlexisTM
