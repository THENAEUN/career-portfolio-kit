#!/usr/bin/env python3
"""Check PDF page count, geometry, text, and URI annotations (requires pypdf)."""
import argparse
from pathlib import Path
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('pdf', type=Path)
    parser.add_argument('--kind', choices=['poster', 'portfolio', 'resume'], required=True)
    parser.add_argument('--require-uri', action='append', default=[])
    parser.add_argument('--require-text', action='append', default=[], help='Required extractable text; repeat as needed')
    parser.add_argument('--max-pages', type=int, help='Page limit for resume (default: 2) or portfolio (default: 30)')
    args = parser.parse_args()
    if args.max_pages is not None and (args.kind not in {'resume', 'portfolio'} or args.max_pages < 1):
        parser.error('--max-pages requires --kind resume or portfolio and a positive integer')
    try:
        from pypdf import PdfReader
    except ImportError:
        parser.exit(2, 'pypdf is unavailable. Use a Python environment with pypdf, or inspect manually.\n')
    reader = PdfReader(args.pdf)
    errors, urls, texts = [], set(), []
    count = len(reader.pages)
    if args.kind == 'poster' and count != 1:
        errors.append('Poster must contain one page')
    if args.kind == 'portfolio' and not 1 <= count <= (args.max_pages or 30):
        errors.append(f'Portfolio must contain 1 to {args.max_pages or 30} pages')
    if args.kind == 'resume' and not 1 <= count <= (args.max_pages or 2):
        errors.append(f'Resume must contain 1 to {args.max_pages or 2} pages')
    for i, page in enumerate(reader.pages, 1):
        w, h = float(page.mediabox.width), float(page.mediabox.height)
        if args.kind == 'poster':
            if not all(abs(a - b) < 2 for a, b in zip(sorted([w, h]), [595.276, 841.89])):
                errors.append(f'Page {i}: expected A4, got {w:.2f} x {h:.2f} pt')
        elif args.kind == 'resume':
            if not all(abs(a - b) < 2 for a, b in zip([w, h], [595.276, 841.89])) or int(page.get('/Rotate', 0)) % 360:
                errors.append(f'Page {i}: expected portrait A4, got {w:.2f} x {h:.2f} pt (rotation {page.get("/Rotate", 0)})')
        elif abs(w / h - 16 / 9) > 0.01:
            errors.append(f'Page {i}: expected 16:9')
        page_text = page.extract_text() or ''
        texts.append(page_text)
        if not page_text.strip():
            errors.append(f'Page {i}: no extractable text')
        for ref in page.get('/Annots', []):
            action = ref.get_object().get('/A', {})
            if hasattr(action, 'get_object'):
                action = action.get_object()
            if action.get('/URI'):
                urls.add(str(action['/URI']))
    for uri in args.require_uri:
        if uri not in urls:
            errors.append('Missing link annotation: ' + uri)
    combined_text = '\n'.join(texts)
    for required in args.require_text:
        if required not in combined_text:
            errors.append('Missing extractable text: ' + required)
    for error in errors:
        print('FAIL:', error)
    print(f'Pages: {count}; distinct URI links: {len(urls)}')
    print('Visual inspection of every page is still required.')
    return 1 if errors else 0


if __name__ == '__main__':
    sys.exit(main())
