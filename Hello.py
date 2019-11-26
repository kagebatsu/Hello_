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
        self.tagset       = []
        self.wordprint    = {}
        self.noveltyscore = 0.0
        self.noveltyprint = []
        self.mlen_sum     = 0
        self.total_msgs   = 0
        self.current_mess = 0
        print('Created Hello profile for ' + self.user_name)
        ## store the summed length of all messages (mlen_sum)
        ## Store the total # of msgs   (total_msgs)
    
    def tag_message(self, message): 
        
        '''tag each message with a possible function'''
        
        response = ['ok', 'k', 'yeah', 'sure', 'right']
        greeting = ['hey', 'hello', 'hi', 'sup', 'yo']
        goodbye  = ['see ya', 'bye', 'later']
        thanks   = ['ty', 'thanks']
        #question = ['?']
        
        for word in message:
            if word in response:
                return self.tagset.append([message, 'response'])
            if word in greeting:
                return self.tagset.append([message, 'greeting'])
            if word in goodbye:
                return self.tagset.append([message, 'goodbye'])
            if word in thanks: 
                return self.tagset.append([message, 'thanks'])
            if word not in response or greeting: 
                return self.tagset.append([message, 'statement'])
        
    def average(self):
        
        '''Determine the average amount of words a user deploys in a message'''
        
        return self.mlen_sum / self.total_msgs
        ## update average divides the total lengths of all messages mlen_sum 
        ## by the total amount of messages (total_msgs)

    def novelty(self, message):
        
        ''' Calculate a message's novelty '''
        
        novelty = len([word for word in message if word not in self.wordprint])
        ## if the user has never used this word before, it is novel
        novelty = (novelty / self.current_mess)
        ## take the number of novel words  
        ## and divide by the total words in the message.
        self.noveltyprint.append([message, novelty])
        
        return novelty 
    
    def update_wordprint(self, message):
        
        '''The wordprint is a dict with words as keys and their frequency as values'''
        
        for word in message:
            if word in self.wordprint.keys():
                self.wordprint[word] += 1
            else:
                self.wordprint[word] = 1
    
        ## when we see a word, add it to the user's wordprint 
        ## and document how many times we've seen it
        
    def preprocess(self, message):
        
        
        return [word for word in message.split()]
            
    def display(self, verbose=False):
        print('total words: '        + str(self.mlen_sum))
        print('words per message: '  + str(self.average()))
        print('total messages' + ' ' + str(self.total_msgs))
        if verbose:
            for word in self.wordprint.keys():
                print(word + ' ' + str(self.wordprint[word]))
            print('NOVELTY CHART')
            print(self.noveltyprint)
    
    def says(self, message):
        message = self.preprocess(message)
        self.current_mess = len(message)
        self.mlen_sum += len(message)
        self.total_msgs  += 1
        self.noveltyscore = self.novelty(message)
        self.update_wordprint(message)
        self.tag_message(message)
        print('MESSAGE TYPE: ' + (self.tagset[-1][1]))
        print('NOVELTY: ' + str(self.noveltyscore) + ' Scores close to 1 represent novel conversation.')
        
        # read_message updates mlen == the length of the message it takes as arg
        # read_message updates the total_msgs value by 1
        
    #def scan(self, message)
        
#nesto = Hello('nesto')
    