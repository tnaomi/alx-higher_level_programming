#!/usr/bin/python3
""" Print all letters of the alphabet apart from q and e"""
for indx in range(97, (97+26)):
    print(chr(indx).strip('q, e'), end='')
