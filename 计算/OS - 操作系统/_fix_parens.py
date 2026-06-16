import re, glob

def has_han(s):
    """Return True if string contains Chinese/Japanese/Korean characters"""
    for ch in s:
        cp = ord(ch)
        if (0x4E00 <= cp <= 0x9FFF or   # CJK Unified Ideographs
            0x3400 <= cp <= 0x4DBF or   # CJK Extension A
            0x2E80 <= cp <= 0x2FDF or   # Kangxi Radicals
            0x3040 <= cp <= 0x309F or   # Hiragana
            0x30A0 <= cp <= 0x30FF or   # Katakana
            0xAC00 <= cp <= 0xD7AF):    # Hangul
            return True
    return False

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

        def replace_paren(m):
            content = m.group(1)
            if has_han(content):
                return m.group(0)  # keep as-is
            content = content.replace('、', ', ')
            return '(' + content + ')'

        line = re.sub(r'（([^）]*?)）', replace_paren, line)
        result.append(line)

    with open(fname, 'w', encoding='utf-8') as f:
        f.write('\n'.join(result))
    print(f'Done: {fname}')

print('All files processed.')
