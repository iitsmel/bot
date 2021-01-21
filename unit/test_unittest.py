from __future__ import unicode_literals
# This Python file uses the following encoding: utf-8
from unit import app_core
import unittest
import os, sys
import parser

class Test_BotReply(unittest.TestCase):
# Inherited unit test

    def testingone(self):
        self.assertEqual(app_core.handle_text_message('BLA hTMl BLA what??'), 1)
        self.assertEqual(app_core.handle_text_message('如何 測試CsS'), 2)
        self.assertEqual(app_core.handle_text_message('BLA hTMl BLA'), 3)
        self.assertEqual(app_core.handle_text_message('測試 CsS'), 3)

    def testingtwo(self):
        # reply english, languages' section
        self.assertEqual(app_core.handle_text_message('what kind of language do you speak?'), 4)
        self.assertEqual(app_core.handle_text_message('what kind of programming language do you use?'), 5)
        self.assertEqual(app_core.handle_text_message('BLA language BLA'), 6)
        self.assertEqual(app_core.handle_text_message('測試 languages'), 6)

    def testingthree(self):
        # reply chinese, languages' section
        self.assertEqual(app_core.handle_text_message('你會說什麼種語言？'), 7)
        self.assertEqual(app_core.handle_text_message('你會用什麼種程式語言？'), 8)
        self.assertEqual(app_core.handle_text_message('語言？'), 9)

    def testingfour(self):
        # reply english, speak example
        self.assertEqual(app_core.handle_text_message(' inTRO in ENGLISH?'), 10)
        self.assertEqual(app_core.handle_text_message('Whats your English certificate /s ?'), 11)
        self.assertEqual(app_core.handle_text_message('ENGLISH'), 12)

    def testingfive(self):
        # reply chinese, speak example
        self.assertEqual(app_core.handle_text_message('用 英 文 來自我介紹'), 13)
        self.assertEqual(app_core.handle_text_message('英文證書?'), 14)
        self.assertEqual(app_core.handle_text_message('英文'), 15)


    def testingfive(self):
        # small talk
        self.assertEqual(app_core.handle_text_message('small talk'), 16)


    def testingsix(self):
        # exception
        self.assertEqual(app_core.handle_text_message('語'), 17)
        self.assertEqual(app_core.handle_text_message('言？'), 17)


        self.assertEqual(app_core.handle_text_message('英'), 17)
        self.assertEqual(app_core.handle_text_message('文'), 17)

        self.assertEqual(app_core.handle_text_message('small'), 17)
        self.assertEqual(app_core.handle_text_message('talk'), 17)

if __name__ == '__main__':
    unittest.main()