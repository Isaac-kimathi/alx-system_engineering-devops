#!/usr/bin/env ruby
# The regex: Output should be [SENDER],[RECEIVER],[FLAGS].
# The sender phone number or name (including country code if present)
# The receiver phone number or name (including country code if present)
# The flags that were used
puts ARGV[0].scan(/\[from:(.*?)\]\s\[to:(.*?)\]\s\[flags:(.*?)\]\).join(',')
