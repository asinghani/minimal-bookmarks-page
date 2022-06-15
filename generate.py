import sys
from util import *

if len(sys.argv) < 2:
    print(f"Usage: {sys.argv[0]} (config file)")
    sys.exit(1)

with open(sys.argv[1], "r") as f:
    config = [x.strip() for x in f.readlines()]

curr_category = None
curr_links = []

all_categories = []

for line in config:
    if len(line) < 1:
        continue

    if line.startswith("-"):
        assert curr_category is not None
        curr_links.append(parse_cfg_line(line))
    else:
        if curr_category:
            all_categories.append((curr_category, curr_links))

        curr_category = line
        curr_links = []

if curr_category:
    all_categories.append((curr_category, curr_links))

print("Categories:", "".join(["\n- " + x[0] for x in all_categories]))

with open("template.html", "r") as f:
    template = f.read()

with open("index.html", "w+") as f:
    f.write(template.replace("__CONTENT__",
                             "\n".join([generate_card(*cat) for cat in all_categories])))
