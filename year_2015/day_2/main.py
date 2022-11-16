with open('input.txt', 'r') as input_file:
    input_text = input_file.read().splitlines()

total_wrapping_paper = 0

for line in input_text:
    l, w, h = line.split('x')
    l, w, h = int(l), int(w), int(h)

    lw = l*w
    wh = w*h
    hl = h*l

    total_wrapping_paper += 2 * (lw + wh + hl) + min(lw, wh, hl)

print('part 1 total_wrapping_paper: ', total_wrapping_paper)

with open('input.txt', 'r') as input_file:
    input_text = input_file.read().splitlines()

total_ribbon = 0

for line in input_text:
    l, w, h = line.split('x')
    l, w, h = int(l), int(w), int(h)

    v = l*w*h
    p1 = 2*l + 2*w
    p2 = 2*w + 2*h
    p3 = 2*h + 2*l

    total_ribbon += min(p1, p2, p3) + v

print('part 2 total_ribbon: ', total_ribbon)
