import os
import json
import unittest
import jc.parsers.finger

THIS_DIR = os.path.dirname(os.path.abspath(__file__))


class MyTests(unittest.TestCase):

    def setUp(self):
        # input
        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/centos-7.7/finger.out'), 'r', encoding='utf-8') as f:
            self.centos_7_7_finger = f.read()

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/ubuntu-18.04/finger.out'), 'r', encoding='utf-8') as f:
            self.ubuntu_18_4_finger = f.read()

        # output
        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/centos-7.7/finger.json'), 'r', encoding='utf-8') as f:
            self.centos_7_7_finger_json = json.loads(f.read())

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/ubuntu-18.04/finger.json'), 'r', encoding='utf-8') as f:
            self.ubuntu_18_4_finger_json = json.loads(f.read())


    def test_finger_nodata(self):
        """
        Test plain 'finger' with no data
        """
        self.assertEqual(jc.parsers.finger.parse('', quiet=True), [])

    def test_finger_centos_7_7(self):
        """
        Test plain 'finger' on Centos 7.7
        """
        self.assertEqual(jc.parsers.finger.parse(self.centos_7_7_finger, quiet=True), self.centos_7_7_finger_json)

    def test_finger_ubuntu_18_4(self):
        """
        Test plain 'finger' on Ubuntu 18.4
        """
        self.assertEqual(jc.parsers.finger.parse(self.ubuntu_18_4_finger, quiet=True), self.ubuntu_18_4_finger_json)


if __name__ == '__main__':
    unittest.main()
