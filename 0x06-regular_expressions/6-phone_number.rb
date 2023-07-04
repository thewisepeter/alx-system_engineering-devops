#!/usr/bin/env ruby
#Ruby script that accepts one argument and
# pass it to a regular expression matching method

#puts ARGV[0].scan(/hbt{1,4}n/).join
puts ARGV[0].scan(/^\d{10}/).join
