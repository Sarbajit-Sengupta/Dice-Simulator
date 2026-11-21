import subprocess
import sys
import unittest
from pathlib import Path


class CliTests(unittest.TestCase):
    def test_uppercase_reply_and_eof(self):
        result = subprocess.run([sys.executable, str(Path(__file__).with_name('main.py'))],
                                input=' YES \n', text=True, capture_output=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.count('Rolling The Dices...'), 2)
        values = [int(line) for line in result.stdout.splitlines() if line.isdigit()]
        self.assertEqual(len(values), 4)
        self.assertTrue(all(1 <= value <= 6 for value in values))


if __name__ == '__main__':
    unittest.main()
