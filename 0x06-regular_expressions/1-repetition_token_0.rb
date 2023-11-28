#!/usr/bin/env ruby
# A RegEx that a matches a repeation of single char
puts ARGV[0].scan(/hbt{2,5}n/).join
