import pyperclip

restricted = ['%', '@', '#', '$']

def create_move_circuit(alphabet):
    with open('move_circuit_dynamic.txt', 'w') as f:
        for c in alphabet:
            f.write('move1 ' + c + ' @ r m' + c + '\n')
        f.write('move1 % _ r move2\n')
        for c in alphabet:
            f.write('\nm' + c + ' $ * r m' + c + '1\n')
            f.write('m' + c + ' * * r *\n\n')
            f.write('m' + c + '1 _ '+ c +' l move \n')
            f.write('m' + c + '1 * * r *\n')
    with open ('move_circuit_dynamic.txt', 'r') as f:
        s = ''
        for line in f.readlines():
            s += line
        pyperclip.copy(s)

def create_copy_circuit(alphabet):
    with open('copy_circuit_dynamic.txt', 'w') as f:
        for c in alphabet:
            f.write('copy1 ' + c + ' @ l w' + c + '\n')
        f.write('copy1 % _ r copy2\n')
        for c in alphabet:
            f.write('\nw' + c + ' _ ' + c + ' r w' + c + '1\n\n')
            f.write('w' + c + '1 $ * r w' + c + '2\n')
            f.write('w' + c + '1 * * r *\n\n')
            f.write('w' + c + '2 _ '+ c +' l copy \n')
            f.write('w' + c + '2 * * r *\n')
    with open ('copy_circuit_dynamic.txt', 'r') as f:
        s = ''
        for line in f.readlines():
            s += line
        pyperclip.copy(s)

def create_writeLeft_circuit(alphabet):
    with open('writeLeft_circuit_dynamic.txt', 'w') as f:
        for c in alphabet:
            f.write('writeLeft2 ' + c + ' * l wl' + c + '\n')
        for c in alphabet:
            f.write('\nwl' + c + ' # * l wl' + c + '1\n')
            f.write('wl' + c + ' * * l *\n\n')
            f.write('wl' + c + '1 _ '+ c +' r writeLeft3 \n')
            f.write('wl' + c + '1 * * l *\n')
    with open ('writeLeft_circuit_dynamic.txt', 'r') as f:
        s = ''
        for line in f.readlines():
            s += line
        pyperclip.copy(s)

def create_moveToFront_circuit(alphabet):
    with open('moveToFront_circuit_dynamic.txt', 'w') as f:
        for c in alphabet:
            f.write('moveToFront1 ' + c + ' @ r mf' + c + '\n')
        f.write('moveToFront1 % _ r moveToFront2\n')
        for c in alphabet:
            f.write('\nmf' + c + ' # * l mf' + c + '1\n')
            f.write('mf' + c + ' * * r *\n\n')
            f.write('mf' + c + '1 _ '+ c +' l moveToFront \n')
            f.write('mf' + c + '1 * * l *\n')
    with open ('moveToFront_circuit_dynamic.txt', 'r') as f:
        s = ''
        for line in f.readlines():
            s += line
        pyperclip.copy(s)

def create_find_circuit(alphabet):
    with open('find_circuit_dynamic.txt', 'w') as f:
        for c in alphabet:
            f.write('find ' + c + ' _ r f' + c + '\n')
        for c in alphabet:
            f.write('\nf' + c + ' '+c+' * l moveWord\n')
            f.write('f' + c + ' * * r *\n')
    static = ''
    with open ('find_circuit_static.txt', 'r') as f:
        for line in f.readlines():
            static += line
    
    dynamic = ''
    with open ('find_circuit_dynamic.txt', 'r') as f:
        for line in f.readlines():
            dynamic += line
    
    with open('find_circuit.txt', 'w') as f:
        f.write(static)
        f.write(dynamic)


def create_huffman_encoding_dynamic(alphabet):
    create_move_circuit(alphabet)
    create_copy_circuit(alphabet)
    create_writeLeft_circuit(alphabet)
    create_moveToFront_circuit(alphabet)
    create_find_circuit(alphabet)




alphabet = ['0', '1', 'a', 'b', 'c', 'd', 'o', '(', ')', '-']