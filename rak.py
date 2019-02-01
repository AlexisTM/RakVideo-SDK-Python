#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

QUALITY=["QVGA", "VGA", "720p", "1080p"]


class RakSetup(object):
  def __init__(self, ip="192.168.100.100", username="admin", password="admin"):
    self.ip = ip
    self.username = username
    self.password = password
    self.pipes = {}

  def server_cmd(self, _command, _pipe=None, _value=None, _type='h264'):
    link = 'http://'+self.ip+'/server.command?command='+_command
    if _type is not None: link += '&type=' + str(_type)
    if _pipe is not None: link += '&pipe=' + str(_pipe)
    if _value is not None: link += '&value=' + str(_value)
    try:
      r = requests.get(link, auth=(self.username, self.password), timeout=0.5)
      json = r.json()
      return json
    except Exception as ex:
      print(ex)
      return None
  
  def param_cmd(self, _action, _group, _data, _value):
    pass


class Pipe(object):
  def __init__(self, ip, pipe, username="admin", password="admin"):
    self._pipe = int(pipe)
    self._resolution = None
    self._fps = None
    self._quality = None
    self._gop = None
    self._version = None
    self.API = RakSetup(ip, username, password) 

  @property
  def password(self):
    return self.API.password

  @password.setter
  def password(self, password):
    self.API.password = password

  @property
  def username(self):
    return self.API.username

  @username.setter
  def username(self, username):
    self.API.username = username

  @property
  def ip(self):
    return self.API.ip

  @ip.setter
  def ip(self, ip):
    self.API.ip = ip

  @property
  def resolution(self):
    if self._resolution is None:
      response = self.API.server_cmd('get_resol', _type='h264', _pipe=self._pipe)
      if response:
        self._resolution = int(response['value'])
    return self._resolution

  @property
  def resolution_name(self):
    return QUALITY[self.resolution]

  @property
  def gop(self):
    if self._gop is None:
      response = self.API.server_cmd('get_resol', _type='h264', _pipe=self._pipe)
      if response:
        self._gop = int(response['value'])
    return self._gop

  @property
  def quality(self):
    if self._quality is None:
      response = self.API.server_cmd('get_enc_quality', _type='h264', _pipe=self._pipe)
      if response:
        self._quality = int(response['value'])
    return self._quality

  @property
  def fps(self):
    if self._fps is None:
      response = self.API.server_cmd('get_max_fps', _type='h264', _pipe=self._pipe)
      if response:
        self._fps = int(response['value'])
    return self._fps

  @resolution.setter
  def resolution(self, resolution):
    response = self.API.server_cmd('set_resol', self._pipe, resolution)
    if response is not None:
      self._resolution = int(response['value'])
    else:
      print('Failed to set resolution')
    return self

  @gop.setter
  def gop(self, gop):
    response = self.API.server_cmd('set_enc_gop', self._pipe, gop)
    if response is not None:
      self._gop = int(response['value'])
    else:
      print('Failed to set gop')
    return self

  @quality.setter
  def quality(self, quality):
    response = self.API.server_cmd('set_enc_quality', self._pipe, quality)
    if response is not None:
      self._quality = int(response['value'])
    else:
      print('Failed to set quality')
    return self

  @fps.setter
  def fps(self, fps):
    response = self.API.server_cmd('set_max_fps', self._pipe, fps)
    if response is not None:
      self._fps = int(response['value'])
    else:
      print('Failed to set fps')
    return self

  @property
  def version(self):
    if self._version is None:
      response = self.API.server_cmd('get_version', _type='h264', _pipe=self._pipe)
      if response:
        self._version = response['value']
    return self._version

  def refresh(self):
    # Trigger getters:
    _ = self.gop
    _ = self.quality
    _ = self.fps
    _ = self.resolution
    _ = self.version

  def __str__(self):
    return """RAK {self.version} - {self.backend.username}:{self.backend.password}@{self.backend.ip}
\n\t GOP: {self.gop}
\n\t GOP: {self.quality}
\n\t GOP: {self.fps}
\n\t GOP: {self.resolution}
\n\t GOP: {self.gop}
""".format(self)


def main():
  rak = Pipe("192.168.100.100", 1)
  print(rak.version)

if __name__ == "__main__":
  main()

# RTSP links
# rtsp://admin:admin@192.168.100.100/cam1/h264 # Over WiFi
# rtsp://admin:admin@192.168.1.98/cam1/h264 # Over Ethernet
