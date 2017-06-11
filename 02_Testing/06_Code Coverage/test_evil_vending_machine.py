import unittest

from evil_vending_machine import give_change
from evil_vending_machine import give_item_and_change


class TestVendingMachine(unittest.TestCase):
    def test_return_change(self):
        """the smallest denomination coin is kept by the machine"""
        self.assertEqual(give_change(.17), [.10, .05])
        self.assertEqual(give_change(.18), [.10, .05, .02])
        self.assertEqual(give_change(.04), [.02])

    def test_unavailabe_items(self):
        """if user asks for an item that's unavailable, they should not be given the item, and their money should be TAKEN"""
        item, change, _ = give_item_and_change('crisps', .50)
        self.assertIsNone(item)
        self.assertEqual(change, 0)

    def test_amount_not_enough(self):
        """if user enters an amount that is not enough, they should not be given the item and their money should be TAKEN"""
        item, change, _ = give_item_and_change('coke', .50)
        self.assertIsNone(item)
        self.assertEqual(change, 0)

    def test_give_correct_change(self):
        """if user enters a valid item, and enough money, they should get the correct change less the smallest coin"""
        item, change, _ = give_item_and_change('coke', 1)
        self.assertEqual(item, 'coke')
        self.assertEqual(change, [.10, .10, .05])



