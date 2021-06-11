#!/usr/bin/env python3
from functools import singledispatch


@singledispatch
def func(arg):
    print(f"This is a generic call: {arg}")


@func.register(int)
def _(arg):
    print(f"This is your integer number: {arg}")


@func.register(list)
def _(arg):
    print(f"This is your list: {arg}")


@func.register(float)
def _(arg):
    print(f"This is your float: {arg}")


func(2)
func(2.0)
func([2, 3])
func("Hello World")
