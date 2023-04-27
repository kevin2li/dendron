---
id: pj2qfnt6imyds8dkwa24uva
title: yaml
desc: ''
updated: 1682601229660
created: 1682601047316
---

参考：https://learnxinyminutes.com/docs/yaml/

# key-value
``` yaml
key: value
another_key: Another value goes here.
a_number_value: 100
scientific_notation: 1e+12
hex_notation: 0x123  # evaluates to 291
octal_notation: 0123 # evaluates to 83
```
# nested key-value
``` yaml
# Nesting uses indentation. 2 space indent is preferred (but not required).
a_nested_map:
  key: value
  another_key: Another Value
  another_nested_map:
    hello: hello
```

# list
``` yaml
# Sequences (equivalent to lists or arrays) look like this
# (note that the '-' counts as indentation):
a_sequence:
  - Item 1
  - Item 2
  - 0.5  # sequences can contain disparate types.
  - Item 4
  - key: value
    another_key: another_value
  - - This is a sequence
    - inside another sequence
  - - - Nested sequence indicators
      - can be collapsed
```
