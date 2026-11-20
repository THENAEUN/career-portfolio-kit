"""Check explicit submission limits without forcing every portfolio into 10 pages."""
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

try:
    from pypdf import PdfWriter
    from pypdf.generic import DictionaryObject, NameObject, DecodedStreamObject
except ImportError:
    PdfWriter = None

CHECK = Path(__file__).resolve().parents[1] / 'tools/check_pdf.py'


@unittest.skipUnless(PdfWriter is not None, 'pypdf is needed for PDF-limit fixtures')
class PdfLimitTests(unittest.TestCase):
    def create_pdf(self, destination, pages, a4=False):
        writer = PdfWriter()
        for _ in range(pages):
            page = writer.add_blank_page(width=595.276 if a4 else 1200,
                                         height=841.89 if a4 else 675)
            font = DictionaryObject({NameObject('/Type'): NameObject('/Font'),
                                     NameObject('/Subtype'): NameObject('/Type1'),
                                     NameObject('/BaseFont'): NameObject('/Helvetica')})
            page[NameObject('/Resources')] = DictionaryObject({
                NameObject('/Font'): DictionaryObject({NameObject('/F1'): font})})
            stream = DecodedStreamObject()
            stream.set_data(b'BT /F1 12 Tf 72 600 Td (Synthetic fixture) Tj ET')
            page[NameObject('/Contents')] = writer._add_object(stream)
        with destination.open('wb') as output:
            writer.write(output)

    def check(self, path, *args):
        return subprocess.run([sys.executable, str(CHECK), str(path), *args],
                              capture_output=True, text=True)

    def test_portfolio_default_allows_chapters_but_rejects_above_limit(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'portfolio.pdf'
            self.create_pdf(path, 18)
            self.assertEqual(self.check(path, '--kind', 'portfolio').returncode, 0)
            self.create_pdf(path, 31)
            self.assertEqual(self.check(path, '--kind', 'portfolio').returncode, 1)

    def test_user_submission_limit_overrides_portfolio_default(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'portfolio.pdf'
            self.create_pdf(path, 18)
            self.assertEqual(self.check(path, '--kind', 'portfolio', '--max-pages', '10').returncode, 1)
            self.create_pdf(path, 31)
            self.assertEqual(self.check(path, '--kind', 'portfolio', '--max-pages', '40').returncode, 0)

    def test_resume_and_poster_limits_remain_independent(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'a4.pdf'
            self.create_pdf(path, 3, a4=True)
            self.assertEqual(self.check(path, '--kind', 'resume').returncode, 1)
            self.assertEqual(self.check(path, '--kind', 'resume', '--max-pages', '3').returncode, 0)
            self.create_pdf(path, 1, a4=True)
            self.assertEqual(self.check(path, '--kind', 'poster').returncode, 0)
            self.assertEqual(self.check(path, '--kind', 'poster', '--max-pages', '2').returncode, 2)

    def test_invalid_page_limits_are_rejected(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'portfolio.pdf'
            self.create_pdf(path, 1)
            for limit in ['0', '-1']:
                self.assertEqual(self.check(path, '--kind', 'portfolio', '--max-pages', limit).returncode, 2)


if __name__ == '__main__':
    unittest.main()
