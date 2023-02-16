import unittest
import cake_aligner


class TestCakeAligner(unittest.TestCase):
    def test_align_llm_ais(self):
        """Test that the Cake Aligner can align LLM AIs"""
        result = cake_aligner.align_llm_ais()
        self.assertTrue(result)

    def test_installation(self):
        """Test that the Cake Aligner can be installed with pip"""
        result = cake_aligner.install()
        self.assertTrue(result)

    def test_quick_start(self):
        """Test that the Cake Aligner can be started quickly with a single command"""
        result = cake_aligner.quick_start()
        self.assertTrue(result)

    def test_software_stack(self):
        """Test that the Cake Aligner uses the correct software stack"""
        result = cake_aligner.check_software_stack()
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()
