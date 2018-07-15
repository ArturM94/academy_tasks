from unittest import TestCase

from elementary_tasks import Envelope


class TestEnvelopeEntry(TestCase):
    """Envelope Entry tests"""
    def setUp(self):
        """Set up for test"""
        print('\nSet up for [' + self.shortDescription() + ']')
        print(self)

    def tearDown(self):
        """Tear down for test"""
        print('Tear down for [' + self.shortDescription() + ']\n')

    def test_envelope_entry_first_bigger_than_second(self):
        """Envelope Entry method test"""
        envelope = Envelope(7, 9, 5, 4)
        result = envelope.envelope_entry()
        self.assertEqual(result, 'The second envelope can be nested '
                                 'in the first.\n')

    def test_envelope_entry_first_smaller_than_second(self):
        """Envelope Entry method test"""
        envelope = Envelope(5, 4, 7, 9)
        result = envelope.envelope_entry()
        self.assertEqual(result, 'The first envelope can be nested '
                                 'in the second.\n')

    def test_envelope_entry_cannot_be_nested(self):
        """Envelope Entry method test"""
        envelope = Envelope(7, 9, 8, 6)
        result = envelope.envelope_entry()
        self.assertEqual(result, 'None of the envelopes can be nested '
                                 'in another.\n')


if __name__ == '__main__':
    TestEnvelopeEntry()
