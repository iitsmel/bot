from __future__ import unicode_literals
# This Python file uses the following encoding: utf-8
import os
import sys
import random
import parser

def handle_text_message(event):

    inputtext = event
    inputtext = inputtext.lower()
    autoreply = 'hmm, what do you mean by that?'

    # resume example
    if 'html' in inputtext or 'css' in inputtext:

        # reply english
        if 'how' in inputtext or 'what' in inputtext or 'resume' in inputtext:
            #_bot_api.reply_message()
            return 1

        # reply chinese
        elif '怎麼' in inputtext or '如何' in inputtext or '履歷' in inputtext:
            #_bot_api.reply_message()
            return 2

        else:
            return 3


    # reply english, languages' section
    elif 'language' in inputtext or 'languages' in inputtext:

        # reply english, speak
        if 'speak' in inputtext:
            return 4

        # reply english, program
        elif 'program' in inputtext or 'programming' in inputtext:
            return 5

        else:
            return 6


    # reply chinese, languages' section
    elif '語言' in inputtext or '語' in inputtext and '言' in inputtext:
        # reply chinese, speak
        if '說' in inputtext:
            return 7

        # reply chinese, program
        if '程式' in inputtext or '程式語言' in inputtext:
            return 8

        else:
            return 9


    # reply english, speak example
    elif 'english' in inputtext:
            
        # self introduction
        if 'intro' in inputtext or 'introduction' in inputtext or 'self' in inputtext:
            return 10

        # english certificate
        elif 'certificate' in inputtext or 'toeic' in inputtext:
            return 11

        else:
            return 12



    # reply chinese, speak example
    elif '英文' in inputtext or '英' in inputtext and '文' in inputtext:
            
        # self introduction
        if '自介' in inputtext or '自我介紹' in inputtext or '講你自己' in inputtext:
            return 13

        # english certificate
        elif '證照' in inputtext or '證書' in inputtext or '多益' in inputtext or 'toeic' in inputtext:
            return 14

        else:
            return 15


    # small talk
    elif 'small talk' in inputtext or 'small' in inputtext and 'talk' in inputtext:
        return 16

    else:
        return 17


if __name__ == "__main__":
    app.run()