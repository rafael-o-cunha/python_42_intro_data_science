import os
import subprocess
import sys
import unittest


class TestPimpImageProgram(unittest.TestCase):
    """End-to-end tests: run pimp_image.py exactly as it would be run from
    the command line (`python3 pimp_image.py`), checking its printed
    output and the file it produces. Exercises load_image.py and
    pimp_image.py together, the same way the real program does."""

    OUTPUT_FILE = "pimp_output.png"

    def setUp(self):
        if os.path.exists(self.OUTPUT_FILE):
            os.remove(self.OUTPUT_FILE)

    def tearDown(self):
        if os.path.exists(self.OUTPUT_FILE):
            os.remove(self.OUTPUT_FILE)

    def run_program(self):
        """Run pimp_image.py as a subprocess and return the completed
        process. MPLBACKEND=Agg avoids opening a GUI window so the test
        doesn't hang waiting for a window to be closed."""
        env = os.environ.copy()
        env["MPLBACKEND"] = "Agg"
        return subprocess.run(
            [sys.executable, "pimp_image.py"],
            capture_output=True,
            text=True,
            env=env,
            timeout=30,
        )

    def test_program_runs_without_crashing(self):
        result = self.run_program()
        self.assertEqual(result.returncode, 0)

    def test_program_prints_image_shape(self):
        result = self.run_program()
        self.assertIn("The shape of image is: (257, 450, 3)", result.stdout)

    def test_program_prints_invert_docstring(self):
        result = self.run_program()
        self.assertIn(
            "Invert the colors of an image", result.stdout
        )

    def test_program_confirms_image_saved(self):
        result = self.run_program()
        self.assertIn("Image saved as pimp_output.png", result.stdout)

    def test_program_creates_output_file(self):
        self.run_program()
        self.assertTrue(os.path.exists(self.OUTPUT_FILE))
        self.assertGreater(os.path.getsize(self.OUTPUT_FILE), 0)

    def test_program_no_unhandled_traceback(self):
        result = self.run_program()
        self.assertNotIn("Traceback", result.stderr)


if __name__ == "__main__":
    unittest.main()