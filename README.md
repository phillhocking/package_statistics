# package_statistics
![main](https://github.com/phillhocking/package_statistics/actions/workflows/pytest.yml/badge.svg) [![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-390/) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Python project to display statistics about Debian packages by architecture, specifically the amount of files that are installed by a particular `deb` package. 

Usage: `package_statistics.py arch`

Example Output: 

```
$ ./package_statistics.py amd64
1.  devel/piglit 51380
2.  science/esys-particle 17410
3.  math/acl2-books 8933
4.  kernel/linux-headers-5.10.0-8-amd64 6144
5.  kernel/linux-headers-5.10.0-8-rt-amd64 6142
6.  libdevel/libboost1.74-dev 5411
7.  net/zoneminder 5172
8.  games/tuxfootball 4630
9.  debug/linux-image-5.10.0-8-amd64-dbg 3910
10.  debug/linux-image-5.10.0-8-rt-amd64-dbg 3904
```
Pull requests are welcome, please let me know if you have any suggestions or feature requests via opening an issue. 