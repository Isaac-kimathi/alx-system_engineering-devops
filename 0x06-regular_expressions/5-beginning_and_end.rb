#!/usr/bin/env ruby
#A regex matching a string starts with h ends with n
#can have any single character in between
puts ARGV[0].scan(/h.n/).join
