import json

def parse_cfg_line(line):
    assert line.startswith("-")
    line = line[1:]
    name, link = line.split("::")
    name = json.loads(name.strip())
    link = link.strip()

    return (name, link)

def generate_link(name, link):
    return """
<a href="__LINK__">
    <li class="list-group-item">
        __NAME__
    </li>
</a>
    """.replace("__NAME__", name).replace("__LINK__", link)

def generate_card(title, links):
    links = [generate_link(*x) for x in links]
    links = "\n".join(links)

    return """
<div class="col-sm-4 col-lg-3 mb-3">
    <div class="card">
        <div class="card-header">
            __TITLE__
        </div>
        <ul class="list-group list-group-flush">
            <!-- Start Links -->
__LINKS__
            <!-- End Links -->
        </ul>
    </div>
</div>
    """.replace("__TITLE__", title).replace("__LINKS__", links)
