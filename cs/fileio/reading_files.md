**Reading Files in Python**
Opening a file in python

**example.txt**
'''
Hello Class!
'''

```python
f = open('example.txt')
# same as f = open('example.txt', 'r')

text = f.read()
text

f.close()
```
Prints output of the text file:
"Hello Class"

Then closes the text file with `f.close()`

```python
with open('example.txt', 'w') as f:
    f.write("I can totally do a backflip")

with open('example.txt') as f:
    print(f.read())
    
    text = f.read()

    print('text: {}'.format(text))
    print(f.read())
```
Opens file with the ability to write to the file, then writes
to the file with the function `print(text)`

```python
with open('example.txt', 'a') as f:
    f.write('line 1!\n')
    f.write('line 2!\n')
```
Writes two new lines to the file

**Resources**
- (Reading and Writing Files)[https://docs.python.org/3/tutorial/inputoutput.html]
