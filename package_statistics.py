#!/usr/bin/env python3
# Above shebang format should work on most platforms per PEP 394.
"""
package_statistics 0.2 by Phillip Hocking (phillhocking@gmail.com).

This application is intended to fetch and analyze the ten packages with the
largest number of installed files for a particular system architecture via the
Contents Index for the Debian package system hosted on official Debian mirror.

This application was written for Ubuntu 20.04.02 - on a base install you must
pip install requirements.txt
"""
import argparse
import asyncio
import gzip
import io
import operator
import os
import re
import sys

import aiofiles
import aiohttp


async def main(argv=sys.argv):
    """Primary application coroutine."""
    # Instantiate argparse to collect required paramaters, validate input, and
    # catch/throw errors.
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "arch",
        help="architecture to gather statistics for Debian packages",
        type=str,
    )
    args = parser.parse_args(argv)
    result = await fetch(args.arch)


async def fetch(arch):
    """Fetch repository Contents Index and return sorted output."""
    # Instantiate dictionary which will contain aiohttp session data.
    mydict = {}
    # Instantiate aiohttp session as async call to fetch repository data from
    # Debian mirror.
    async with aiohttp.ClientSession() as session:
        # Interpolate user input obtained from argparse and attempt to fetch
        # from mirror.

        # No input sanitation is performed to validate the arch positional, so
        # input that does not match what is available on the mirror via HTTP
        # will result in an error.
        async with session.get(
            "http://ftp.uk.debian.org/debian/dists/stable/main/Contents-"
            + arch
            + ".gz"
        ) as resp:
            # Validate mirror responds with HTTP 200 OK.
            if resp.status == 200:
                # Create temporary file from async session as gzip.open
                # doesn't work with async stream data.
                async with aiofiles.open("file.gz", "wb") as f:
                    await f.write(await resp.read())
                    await f.close()
                    # Create file handler with gzip.open and format for UTF-8
                    # via io.TextIOWrapper.
                with gzip.open("file.gz", "rb") as g:
                    with io.TextIOWrapper(g, "utf-8") as file_content:
                        for line in file_content:
                            # Split lines by whitespace for insertion into
                            # dictionary.
                            values = line.split(" ")
                            # Grab only the Debian package identifier as key in
                            # dictionary and trim newline characters.
                            # Format for Contents Index described here:
                            # wiki.debian.org/RepositoryFormat#A.22Contents.22_indices
                            package = values[1].rstrip()
                            # If the dictionary already contains the package as
                            # key, increment value/count which represents total
                            # files in the key/package.
                            if package in mydict:
                                mydict[package] = mydict[package] + 1
                                # If dictionary does not contain the key, add
                                # key to dictionary and set value/count = 1.
                            else:
                                mydict[package] = 1
                                # Instantiate new dictionary to sort mydict by
                                # value in descending order.
                sorted_dict = dict(
                    sorted(
                        mydict.items(),
                        key=operator.itemgetter(1),
                        reverse=True,
                    )
                )
                # If any HTTP response other than 200 OK is received by
                # aiohttp, print HTTP status code/response and exit nonzero.
            elif resp.status != 200:
                print(
                    "There was a problem retrieving the Content Index from "
                    + "the mirror, please check that you are selecting the "
                    + "correct architecture."
                )
                print(await resp.status)
                print(await resp.text())
                sys.exit(2)
        # Instantiate list to contain ten key/values with highest count from
        # sorted_dict. Exclude 0:0 - this dictionary value matches files but
        # not a corresponding package. TODO: perhaps look at why someday?
    top_ten_dict = list(sorted_dict.items())[1:11]
    #  Invoke disp() with sorted/trimmed dictionary entries passed as list.
    await disp([top_ten_dict])


async def disp(top_ten):
    """Display parsed results from Debian Contents Index via fetch()."""
    count = 1
    for package in top_ten[0]:
        print(str(count) + ". ", str(package[0]), str(package[1]))
        count += 1


# If calling main via script/test, use correct namespace.
if __name__ == "__main__":
    asyncio.run(main(sys.argv[1:]))

# Invoke main() via async coroutine call.
asyncio.run(main(sys.argv[1:]))
