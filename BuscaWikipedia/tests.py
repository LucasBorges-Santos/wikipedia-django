from django.test import TestCase
import wikipedia

# Create your tests here.
wikipedia.set_lang('pt')
n = wikipedia.page('dinossauro')
t = n.summary.split('\n')

print(n.summary)

print(n.images)

