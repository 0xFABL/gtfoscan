#!/usr/bin/env python3
"""
This script will automatically scan the system to 
see if the scripts exist in the system.
"""

import requests
import shutil


def fetch_all_gtfobin_names() -> list[str]:
    """
    This url is tailored such that all the .md files returned will be gtfo bins.
    Example API Response Record: 
        {'name': '.dir-locals.el', 
            'path': '_gtfobins/.dir-locals.el', 
            'sha': '7f84dc63038bfbff4177e602963891c1338be334', 
            'size': 36, 
            'url': 'https://api.github.com/repos/GTFOBins/GTFOBins.github.io/contents/_gtfobins/.dir-locals.el?ref=master', 
            'html_url': 'https://github.com/GTFOBins/GTFOBins.github.io/blob/master/_gtfobins/.dir-locals.el', 
            'git_url': 'https://api.github.com/repos/GTFOBins/GTFOBins.github.io/git/blobs/7f84dc63038bfbff4177e602963891c1338be334', 
            'download_url': 'https://raw.githubusercontent.com/GTFOBins/GTFOBins.github.io/master/_gtfobins/.dir-locals.el', 
            'type': 'file', 
            '_links': {'self': 'https://api.github.com/repos/GTFOBins/GTFOBins.github.io/contents/_gtfobins/.dir-locals.el?ref=master', 
            'git': 'https://api.github.com/repos/GTFOBins/GTFOBins.github.io/git/blobs/7f84dc63038bfbff4177e602963891c1338be334', 
            'html': 'https://github.com/GTFOBins/GTFOBins.github.io/blob/master/_gtfobins/.dir-locals.el'}}
    """
    GTFOBIN_GITHUB_RAW_URL="https://api.github.com/repos/GTFOBins/GTFOBins.github.io/contents/_gtfobins?ref=master"
    response = requests.get(GTFOBIN_GITHUB_RAW_URL)
    data = response.json()
    gtfo_bins = []
    for record in data:
        if record["type"] == "file":
            if record["name"].endswith(".md"):
                gtfo_bin_name = record["name"].replace(".md", "")
                gtfo_bins.append(gtfo_bin_name)
    return gtfo_bins

def scan_system_for_gtfo_bins():
    gtfo_bins = fetch_all_gtfobin_names() 
    found_executable_paths = []
    for bin_name in gtfo_bins:
        path = shutil.which(bin_name)
        if path:
            print(f"[*] {bin_name} found at {str(path)}")
            found_executable_paths.append(path)

    if len(found_executable_paths) < 1:
        print("[!] no gtfo bins found")
    else:
        print(f"[!] {len(found_executable_paths)} results successfully found.")

if __name__ == "__main__":
    scan_system_for_gtfo_bins()
    

