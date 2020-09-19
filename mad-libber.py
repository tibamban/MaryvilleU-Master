print('Madlib Maker ')
noun=str(input('name:'))
past_tense_verb=str(input('verb: '))
other_noun=str(input('second name:'))

z="So you're still thinking of {0}\n Just like I {1} you should\n I can not {1} you everything, {2} know I wish I could\n {0}'m so high at the moment\n I'm so {1} up in this\n Yeah, we're just young, dumb and {2}\n But we still got love to give"
out=z.format(noun,past_tense_verb,other_noun)
print(out)