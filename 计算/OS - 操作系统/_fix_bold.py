import re, glob

def smart_lower(word):
    """Lowercase a single English word if it's a common noun (not acronym/proper name).
    Acronyms (all-caps or has 2+ uppercase letters) stay as-is."""
    if word.isupper() or sum(1 for c in word if c.isupper()) >= 2:
        return word  # acronym
    if word[0].isupper() and word[1:].islower() and len(word) > 1:
        return word.lower()
    return word

def transform_annotation(text):
    """Lowercase each word in an English annotation, preserving acronyms."""
    words = text.split()
    return ' '.join(smart_lower(w) for w in words)

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

        # Fix: **term**(English) → **term (english)**
        def repl(m):
            bold = m.group(1)       # **term
            english = m.group(2)    # English text
            lowered = transform_annotation(english)
            return f'{bold} ({lowered})**'

        line = re.sub(
            r'(\*\*[^*]+)\*\*\(([A-Za-z0-9][A-Za-z0-9 /&,.\-:;+]*)\)',
            repl, line
        )

        # Also fix: **term** (English) → **term (english)** (with space)
        line = re.sub(
            r'(\*\*[^*]+)\*\* \(([A-Za-z0-9][A-Za-z0-9 /&,.\-:;+]*)\)',
            repl, line
        )

        result.append(line)

    with open(fname, 'w', encoding='utf-8') as f:
        f.write('\n'.join(result))
    print(f'Done: {fname}')

print('All files processed.')
