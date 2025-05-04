## Version 2 ---------------------------------------------------------------------
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