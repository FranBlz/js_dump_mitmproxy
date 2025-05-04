## Version 4 ---------------------------------------------------------------------
import os

class Dump:
    def __init__(self):
        self.path = "/home/fran/projects/mitmproxy/output"

    def response(self, flow):
        if flow.response:
            # flow.response.headers.insert(0, "clear-site-data", "cache") # this didn't even work :(
            flow.response.headers["cache-control"] = "no-store"
            flow.response.headers["pragma"] = "no-cache"
            flow.response.headers.pop("etag", None)
            flow.response.headers.pop("last-modified", None)

            if "javascript" in flow.response.headers.get("Content-Type", ""):
                full_path = self.path + flow.request.pretty_url.replace("https:/", "")
                os.makedirs(os.path.dirname(full_path), exist_ok=True)
                with open(full_path, 'w') as output:
                    output.write(flow.response.text)
                    output.close()

addons = [Dump()]