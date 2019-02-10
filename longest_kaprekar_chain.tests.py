#!/usr/bin/env python3

from longest_kaprekar_chain import *
import unittest

class KaprekarTestCases(unittest.TestCase):
  def test_reverse(self):
    inputs_to_outputs = {
      "1":"1",
      "10":"01",
      "153":"351",
      "100":"001",
      "101":"101",
      "220":"022",
      "260":"062"
    }
    for (input, output) in inputs_to_outputs.items():
      self.assertEqual(reverse_number(input), output)

  def test_chain_generator(self):
    inputs_to_outputs = {
      ("947",10):["947","495"],
      ("6174",10):["6174","3087","8352","6174"],
      ("111",10):[],
      ("495",10):["495"],
      ("6174",10):["6174"],
      ("221",10):["221","099","891","792","693","594","495"],
      ("211",10):["211","099","891","792","693","594","495"],
      ("3141",10):["3141","3177","6354","3087","8352","6174"],
      ("74943",10):["74943","62964","71973","83952"]
    }
    for (input, output) in inputs_to_outputs.items():
      self.assertEqual(chain_generator(input[0], input[1], 1000), output)

    known_constants = {
      (3,10,7):"495",
      (4,10,8):"6174"
    }

    for (input, output) in known_constants.items():
      for i in range(int(first_number(input[0])), int("".join([str(input[1] - 1) for x in range(input[0])]), input[1])):
        number = toStr(i, input[1])
        if not all_digits_the_same(number):
          self.assertEqual(chain_generator(number, input[1], input[2])[-1], output)


  def test_all_digits_the_same(self):
    inputs_to_outputs = {
      "111":True,
      "222":True,
      "0":True,
      "1":True,
      "5555":True,
      "33":True,
      "72":False,
      "7773":False,
      "111115":False,
      "12":False,
      "224":False,
      "3962":False
    }
    for (input, output) in inputs_to_outputs.items():
      self.assertEqual(all_digits_the_same(input), output)

  def test_first_number(self):
    inputs_to_outputs = {
      3:"100",
      4:"1000",
      5:"10000"
    }
    for (input, output) in inputs_to_outputs.items():
      self.assertEqual(first_number(input), output)

if __name__ == '__main__':
  unittest.main()
