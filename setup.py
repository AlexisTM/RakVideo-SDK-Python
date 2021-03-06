from distutils.core import setup
from os import path
this_directory = path.abspath(path.dirname(__file__))
try:
    import pypandoc
    long_description = pypandoc.convert(path.join(this_directory, 'README.md'), 'rst')

except(IOError, ImportError):
  print("Install Pandoc: sudo apt-get install pandoc; sudo python3 -m pip install pypandoc")
  with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
      long_description = f.read()

long_description = long_description.replace("\r","")

setup(
  name = 'rak',
  packages = ['rak'],
  version = '0.1.4',
  license='MIT',
  description = 'Rak Wireless Pythonic API for configuration',
  long_description=long_description,
  author = 'Alexis Paques',
  author_email = 'alexis.paques@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/alexistm/RakVideo-SDK-Python',   # Provide either the link to your github or to your website
  # download_url = 'https://github.com/alexistm/RakVideo-SDK-Python/v_01.tar.gz',    # I explain this later on
  keywords = ['RAK', 'RAKWireless', 'Configuration', 'VideoStreaming'],   # Keywords that define your package best
  install_requires=[
          'requests',
      ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 2.7',
  ],
)
