from jinja2 import Environment, FileSystemLoader

file_loader = FileSystemLoader("templates")
env = Environment(loader=file_loader)

head = env.get_template("head.pine")

head_args = {"title":"title", "short_title": "short", "overlay": "true"} 
#TODO convert python True to true

output = head.render(**head_args)

with open("script.pine", "w") as pine_file:
    pine_file.write(output)

