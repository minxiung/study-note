1. use `file <file>` command to see the file, it's a ELF file.
2. use `xxd <file>` to take a look and fortunatly we find the flag.

```
00001fe0: 0000 0000 0000 0000 0000 0000 0000 0000  ................
00001ff0: 0000 0000 0000 0000 0000 0000 0000 0000  ................
00002000: 0100 0200 0000 0000 4400 5500 4300 5400  ........D.U.C.T.
00002010: 4600 7b00 7300 7400 7200 6900 6e00 6700  F.{.s.t.r.i.n.g.
00002020: 6500 6e00 7400 5f00 7300 7400 7200 6900  e.n.t._.s.t.r.i.
00002030: 6e00 6700 7300 5f00 7300 7400 7200 6900  n.g.s._.s.t.r.i.
00002040: 6e00 6700 7d00 666c 6167 3f20 0077 726f  n.g.}.flag? .wro
00002050: 6e67 2100 636f 7272 6563 7421 0000 0000  ng!.correct!....
00002060: 011b 033b 3400 0000 0500 0000 c0ef ffff  ...;4...........
00002070: 6800 0000 20f0 ffff 5000 0000 19f1 ffff  h... ...P.......
00002080: 9000 0000 f0f1 ffff b800 0000 60f2 ffff  ............`...
```
flag: DUCTF{stringent_strings_string}