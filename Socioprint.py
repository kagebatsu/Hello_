#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 18:36:42 2019

@author: snijinski
"""

#import nltk 

class Hello:
    
    def __init__(self, name):
        self.user_name    = (name)
        self.mlen_sum     = 0
        self.total_msgs   = 0
        print('Created Hello profile for ' + self.user_name)
        #store the summed length of all messages (mlen_sum)
        #Store the total # of msgs   (total_msgs)
        
    def average(self):
        
        '''Determine the average amount of words a user deploys in a message'''
        
        return self.mlen_sum / self.total_msgs
        #update average divides the total lengths of all messages mlen_sum 
        #by the total amount of messages (total_msgs)

    def display(self):
        print('total words: '        + str(self.mlen_sum))
        print('words per message: '  + str(self.average()))
        print('total messages' + ' ' + str(self.total_msgs))
    
    def wordprint(self, message):
        
    def says(self, message):
        self.mlen_sum += len(message.split())
        self.total_msgs  += 1
        #read_message updates mlen == the length of the message it takes as arg
        #read_message updates the total_msgs value by 1
        
    #def scan(self, message)
        
#nesto = Hello('nesto')
    
