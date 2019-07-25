
import os
import unittest

from cdfutils.Config import ConfigStore


CONFIG_FILENAME = r"config.ini"
CFG_USERNAME    = "Fred"
CFG_EMAIL       = "fred@rubble.com"
CFG_USERS       = 5
CFG_FAMILY      = ["Wilma", "Pebbles"]

class TestConfig(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.config = ConfigStore(CONFIG_FILENAME)
        self.config.username = CFG_USERNAME
        self.config.email    = CFG_EMAIL
        self.config.users    = CFG_USERS
        self.config.family   = CFG_FAMILY
        del self.config     # Close the file

    @classmethod
    def tearDownClass(self):
        os.remove(CONFIG_FILENAME)

    def setUp(self):
        self.config = ConfigStore(CONFIG_FILENAME)

    def tearDown(self):
        del self.config

    def test_GetValues(self):
        self.assertEqual(self.config.username, CFG_USERNAME)
        self.assertEqual(self.config.email   , CFG_EMAIL)
        self.assertEqual(self.config.users   , CFG_USERS)
        self.assertEqual(self.config.family  , CFG_FAMILY)

    def test_ChangeValues(self):
        NEWNAME = "Barney"
        oldname = self.config.username
        self.config.username = NEWNAME
        self.assertEqual(self.config.username, NEWNAME)
        self.config.username = oldname  # Restore

        self.config.users += 1
        self.assertEqual(self.config.users   , CFG_USERS+1)
        self.config.users -= 1

if __name__ == "__main__":
    unittest.main()
