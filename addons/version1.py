## Version 1 ---------------------------------------------------------------------
# In this first approach I used basic curl requests proxied through mitmproxy since it simplified the process a bit, also used BeautifulSoup
# since I had some previous experience with it. I was happy once I was able to recognize the basic js elements and their paths.
import os
import logging
from bs4 import BeautifulSoup as bfs

class Dump:
    def __init__(self):
        self.count = 0
        self.path = "/home/fran/projects/mitmproxy/output"

    def response(self, flow):
        if flow.response and flow.response.text:
            scripts = bfs(flow.response.text, "html.parser").find_all('script',{"src":True})
            for item in scripts:
                self.count += 1
                full_path = self.path + item['src']
                os.makedirs(os.path.dirname(full_path), exist_ok=True)
                with open(full_path, 'w') as output:
                    output.write("lorem ipsum")
                    output.close()
            logging.info("Found %d scripts", self.count)

addons = [Dump()]