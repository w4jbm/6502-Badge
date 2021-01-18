# 6502-Badge

Here are various items related to the 6502 Badge computer kit available from Lee Hart.

# eWoz Monitor

This is still best considered 'work in progress', but what I've tested seems to work. To get back to the Badge's monitor use `FFC3R` to run the reset code.

It does use Page Zero locations used by ehBASIC, so they won't play well together.


## bdg_hello

This is a Hello World example for the Badge that makes use of ROM routines. It is small enough to enter through the monitor, but I also have provided a .mon file that can be pasted into the monitor to save you the typing.

## hex2bmon.py

This is a quick Python hack that will take an Intel Hex file and convert it to the format used by the Badge's monitor. I see this more as a convinient way to bootstrap a hex file loader to the platform than to support large file transfers since there is no error checking. But it is kind of handy to quickly build and test programs on the platform.

## And the fine print...

To the extent applicable, all code and other material in this repository is:

Copyright 2020 by James McClanahan and made available under the terms of The MIT License.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
