"""Registry wiring only; metadata rules are tested by canonical SDK tooling."""
import os
from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]


class PackageRegistryTest(unittest.TestCase):
    def test_entries_and_checked_in_index_use_explicit_canonical_tool(self):
        tool = Path(os.environ["OBCX_PACKAGE_TOOL"]).resolve()
        result = subprocess.run([sys.executable, str(ROOT / "generate_package_index.py"),
            "--tool", str(tool), "generate", "--entries", str(ROOT / "entries"),
            "--output", str(ROOT / "index/packages.json"), "--check"], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("development-metadata-only", result.stdout)


if __name__ == "__main__":
    unittest.main()
