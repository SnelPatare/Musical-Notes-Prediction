import unittest
import LilyPondHandler

class TestLilyPondHandler(unittest.TestCase):
    def test_file_save(self):
        l = LilyPondHandler.LilyPondHandler()
        l.create_file("test.ly")
        l.save_file()
        with open("test.ly","r") as f:
            self.assertEqual(f.read(), "\\version \"2.22.2\"\n{ }\n")
        l.create_file("otherTest.ly")
        l.save_file()
        with open("otherTest.ly","r") as f:
            self.assertEqual(f.read(), "\\version \"2.22.2\"\n{ }\n")

    def test_simple_melody(self):
        l = LilyPondHandler.LilyPondHandler()
        l.create_file("simpleMelodyTest.ly")
        l.append_note(LilyPondHandler.A1, LilyPondHandler.QUARTER)
        l.append_note(LilyPondHandler.B1, LilyPondHandler.QUARTER)
        l.append_note(LilyPondHandler.C1, LilyPondHandler.QUARTER)
        l.save_file()
        with open("simpleMelodyTest.ly","r") as f:
            self.assertEqual(f.read(), "\\version \"2.22.2\"\n{ a4 b4 c4 }\n")

if __name__ == '__main__':
    unittest.main()
