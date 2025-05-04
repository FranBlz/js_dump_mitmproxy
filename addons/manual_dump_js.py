## Version 3 ---------------------------------------------------------------------
# This version is almost the same as the previous one but I changed the js object detection to be dependant on the response instead of the request.
# Still requires a manual full page request.
import os

class Dump:
    def __init__(self):
        self.path = "./output"

    def response(self, flow):
        if flow.response and "javascript" in flow.response.headers.get("Content-Type", ""):
                full_path = self.path + flow.request.pretty_url.replace("https:/", "")
                os.makedirs(os.path.dirname(full_path), exist_ok=True)
                with open(full_path, 'w') as output:
                    output.write(flow.response.text)
                    output.close()

addons = [Dump()]