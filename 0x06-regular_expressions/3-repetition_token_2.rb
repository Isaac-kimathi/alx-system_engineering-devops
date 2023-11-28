#!/usr/bin/env ruby
# A RegEx that matches 1 or more occurrence of a char,
# must appear atleast once
puts ARGV[0].scan(/hbt+n/).join
