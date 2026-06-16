import re, glob

for fname in sorted(glob.glob('*.md')):
    if fname.startswith('_'): continue
    with open(fname, 'r', encoding='utf-8') as f:
        text = f.read()

    lines = text.split('\n')
    result = []
    in_block = False

    for line in lines:
        if line.startswith('```'):
            in_block = not in_block
            result.append(line)
            continue

        if in_block:
            result.append(line)
            continue

        # Fix: replace all fullwidth ，with , inside halfwidth parens
        # Handle multiple commas inside parens
        def fix_paren_commas(m):
            content = m.group(1)
            content = content.replace('，', ', ')
            return '(' + content + ')'

        line = re.sub(r'\(([^)]*?，[^)]*?)\)', fix_paren_commas, line)

        # Also fix fullwidth comma inside （...）that are still fullwidth
        def fix_fullwidth_paren_commas(m):
            content = m.group(1)
            content = content.replace('，', ', ')
            return '（' + content + '）'

        line = re.sub(r'（([^）]*?，[^）]*?)）', fix_fullwidth_paren_commas, line)

        result.append(line)

    with open(fname, 'w', encoding='utf-8') as f:
        f.write('\n'.join(result))
    print(f'Done: {fname}')

print('All files processed.')
