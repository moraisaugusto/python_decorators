#!/usr/bin/env python3
"""Overloading example using multipledispatch"""

from multipledispatch import dispatch


@dispatch(int)
def func(param):
    print(f"Integer point: {param}")


@dispatch(float)
def func(param):
    print(f"Float point: {param}")


@dispatch(int, int)
def func(param_a, param_b):
    print(f"Two integer points: {param_a, param_b}")


@dispatch(object)
def func(arg):
    print(f"Generic param: {arg}")


func(1)
func(1.0)
func(2, 3)
func("Hello World")
