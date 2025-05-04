## Version 2 ---------------------------------------------------------------------
# At this point I wanted to tackle the problem using only mitmproxy, which turned out to be pretty straight forward but with a minor caveat.
# For the .js files to be downloaded the browser cache has to be flushed/ignored, to do this manually I simulated a "fresh" request using ctrl+shift+R
# which always gives a full page download.
import os

class Dump:
    def __init__(self):
        self.path = "/home/fran/projects/mitmproxy/output"

    def response(self, flow):
        if flow.response and flow.request.pretty_url.endswith(".js"):
            full_path = self.path + flow.request.pretty_url.replace("https:/", "")
            os.makedirs(os.path.dirname(full_path), exist_ok=True)
            with open(full_path, 'w') as output:
                output.write(flow.response.text)
                output.close()

addons = [Dump()]