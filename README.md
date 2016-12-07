# Video Collage Creator
This was a little tool I wrote a while back in order to create a video collage of different picture sequences. Creating a video from frames is easy, but I need a way to stitch together several frame sequences, possibly not all of the same length. With this little tool you can specify everything in a json file and let the rest be done for you. I hope I'll find the time to polish this some more in the future, but I wanted to push it out to make sure this doesn't just die on some hidden HDD folder some day.

Have a look at the example file, the idea is you create an empty canvas of a fixed size and color and then you specify a set of frames in which you want to render the actual image sequences, the result is an image sequence itself. For each sequence you need to specify a location, a filename pattern, the start and end frame numbers, whether it loops or not, a frame rate and a position. Some of these are not mandatory. But all of this should be fairly obvious from the code.

## License

Copyright (c) 2016 Alexander Hermans

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.