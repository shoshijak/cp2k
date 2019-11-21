#!/usr/bin/ruby

all

# Specify Rule Options
rule 'MD013', :line_length => 1200
rule 'MD026', :punctuation => ".,;:。，；：！？"
rule 'MD029', :style => "ordered"

# Exclude Rules
exclude_rule 'MD024'  # Multiple headers with the same content
exclude_rule 'MD034'  # Bare URL used

