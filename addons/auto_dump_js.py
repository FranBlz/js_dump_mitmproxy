## Version 5 ---------------------------------------------------------------------
# At this point I had read about cache-busting which seemed to be the only real solution to forcing a browser to download the whole page regardless
# of its cache contents. This attemp was somewhat successfull, it does download all js components automatically but only the ones that are directly mentioned
# in the main HTML file, if the reference to the js component is in another HTML file then it doesn't work. I'll try to address this in the future.
# Another weird problem is that sometimes the main HTML file is not requested, in which case nothing is downloaded.
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