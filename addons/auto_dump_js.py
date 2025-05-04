## Version 5 ---------------------------------------------------------------------
import os
from datetime import datetime
from bs4 import BeautifulSoup as bfs

class Dump:
    def __init__(self):
        self.path = "./output"

    def response(self, flow):
        if flow.response:
            if flow.request.method == "GET" and "text/html" in flow.request.headers.get("accept", ""):
                scripts = bfs(flow.response.text, "html.parser")
                timestamp = datetime.now().strftime("%y%m%d%H%M%S")
                for script in scripts.find_all('script', {"src":True}):
                    script["src"] += f"?v={timestamp}"
                flow.response.text = str(scripts)

            if "javascript" in flow.response.headers.get("Content-Type", ""):
                clean_name = flow.request.pretty_url.replace("https:/", "")
                full_path = self.path + clean_name[:clean_name.find(".js") + 3]
                os.makedirs(os.path.dirname(full_path), exist_ok=True)
                with open(full_path, 'w') as output:
                    output.write(flow.response.text)
                    output.close()

addons = [Dump()]