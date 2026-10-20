"""Keep packaged paths short enough for Windows host Git staging prefixes."""
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from validate_package import walk_files


class WindowsPathBudgetTest(unittest.TestCase):
    def test_relative_package_file_paths_fit_windows_staging_budget(self):
        for path in walk_files(ROOT):
            relative = path.relative_to(ROOT).as_posix()
            with self.subTest(path=relative):
                self.assertLessEqual(
                    len(relative),
                    90,
                    "Shorten this distribution path; Windows hosts add a long staging prefix.",
                )


if __name__ == "__main__":
    unittest.main()
