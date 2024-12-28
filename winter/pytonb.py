import nbformat as nbf

def py_to_nb(filename, ans: bool = False):
    with open(filename, "r") as file:
        content = file.read()

    # content = content.replace("\(", "$")
    # content = content.replace("\)", "$")
    # content = content.replace("\[", "$$")
    # content = content.replace("\]", "$$")

    nb = nbf.v4.new_notebook()

    chunks = content.split('"""')[1:]

    nbcells = []
    for i, chunk in enumerate(chunks):
        content = chunk.strip("\n")
        if content == "":
            continue

        content = content.replace("#EMPTYCELL", "")
        if i % 2 == 0:
            # Explanation
            nbcells.append(nbf.v4.new_markdown_cell(chunk))
        else:
            # Code; template and answer separated by `#ANSWER`
            if "#ANSWER" in content:
                content = content.split("#ANSWER")[int(ans)]
            # elif ans:
            #     # no answer provided
                 # continue
            for cell in content.split("#NEWCELL"):
                cell = cell.strip()
                nbcells.append(nbf.v4.new_code_cell(cell))

    nb['cells'] = nbcells

    if ans:
        filename = filename.replace(".py", "_ans.py")
    with open(filename.replace(".py", ".ipynb"), 'w') as f:
        nbf.write(nb, f)


filenames = ["l1", "l2", "l3", "l4", "l5", "l6", "l7", "l8", "l9"]
for filename in filenames:
    py_to_nb(f"{filename}.py")
py_to_nb("l6.py", True)
py_to_nb("l7.py", True)
py_to_nb("l8.py", True)
