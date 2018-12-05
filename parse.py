from instance import Instance


def parse(files):
    lines = [[] for _ in files]

    for i in range(len(files)):
        filename = files[i]

        for line in open(filename):
            if not len(line.strip()) > 3:
                continue

            line = Instance(line)

            print(line.goal, ":", line.features, ":", line.value)

            lines[i].append(line)

    return lines
