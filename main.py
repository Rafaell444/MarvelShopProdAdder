import os

with open("names.txt", "r+") as file:
    for line in file:
        done = os.path.basename("r" + line)

        print("""{{title:"{},desc: "Wolverine &nbsp;&nbsp;5ცალი",output: "ფასი: 1"}},""".format(done))
