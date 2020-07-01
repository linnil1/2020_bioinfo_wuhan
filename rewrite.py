import re
lines = []

now_replace = False
char_line = []
print("input 05_haplo.nex")
for line in open("05_haplo.nex"):
    if now_replace:
        if line == ';\n':
            lines.append("CHARSTATELABELS\n")
            lines.extend([i[0] + ' ' + i[1]  + '\n' for i in re.findall(r"\[(\d+)\]\s*(\w+)", '\n'.join(char_line))])
            lines.append(";\n")
            now_replace = False
        char_line.append(line)
        continue

    if line == "CHARLABELS\n":
        now_replace = True
        continue
    lines.append(line)


open("05_haplo_rewrite.nex", 'w').write(''.join(lines))
print("output 05_haplo_rewrite.nex")
