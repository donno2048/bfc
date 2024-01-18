from subprocess import run
from os import remove
labels, label_count = [], 0
def start_loop() -> str:
    global labels, label_count
    label_count += 1
    labels.append(label_count)
    return f"loop_start{label_count}:\nldrb w3, [x1]\ncmp w3, wzr\nbeq loop_end{label_count}\n"
def end_loop() -> str:
    global labels
    label_count = labels.pop()
    return f"b loop_start{label_count}\nloop_end{label_count}:\n"
initialization = ".data\ntape: .fill 30000\nend:\n.text\n.global _start\n_start:\nldr x1, =tape\nmov x2, #1\nmov x4, x1\nldr x5, =end-1\n"
conversion = {
    '>': lambda: "cmp x1, x5\ncsinc x1, x4, x1, EQ\n",
    '<': lambda: "cmp x1, x4\ncsinc x1, x1, x5, NE\nsub x1, x1, x2\n",
    '+': lambda: "ldrb w3, [x1]\nadd w3, w3, #1\nstrb w3, [x1]\n",
    '-': lambda: "ldrb w3, [x1]\nsub w3, w3, #1\nstrb w3, [x1]\n",
    '.': lambda: "mov x0, #1\nmov w8, #64\nsvc #0\n",
    ',': lambda: "mov x0, #0\nmov w8, #63\nsvc #0\n",
    '[': start_loop,
    ']': end_loop,
}
exit = "mov x0, #0\nmov w8, #93\nsvc #0"
def bf2asm(code: str) -> str:
    return initialization + str().join(map(lambda char: conversion.get(char, lambda: '')(), code)) + exit
def compile(input_file: str, output_file: str) -> None:
    open("temp.asm", 'w').write(bf2asm(open(input_file, 'r').read()))
    run(["as", "-W", "temp.asm"])
    run(["ld", "a.out", "-o", output_file])
    remove("temp.asm")
    remove("a.out")
