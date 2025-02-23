import unittest
from main import extract_title

def test_title():
    md = '# Hi'
    title = extract_title(md)
    unittest.assertEqual(title, 'Hi')

def test_title2():
    md = '## Hi\n# Not Hi'
    title = extract_title(md)
    unittest.assertEqual(title, 'Not Hi')


def main():
    unittest.main()

if '__main__' == __name__:
    main()
