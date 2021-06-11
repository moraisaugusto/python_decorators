#!/usr/bin/env python3
from multipledispatch import dispatch

@dispatch(int)
def func(point):
    print(f"Integer point: {point}")

@dispatch(float)
def func(x):
    print(f"Float point: {x}")

@dispatch(int, int)
def func(x, y):
    print(f"Two integer points: {x, y}")

@dispatch(object)
def func(arg):
    print(f"Generic param: {arg}")

func(1)
func(1.0)
func(2, 3)
func("Hello World")
