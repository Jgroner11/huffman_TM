# Make sure to run this in the circuit directory
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
    static = ''
    with open ('move_circuit_static.txt', 'r') as f:
        for line in f.readlines():
            static += line
    
    dynamic = ''
    with open ('move_circuit_dynamic.txt', 'r') as f:
        for line in f.readlines():
            dynamic += line
    
    with open('move_circuit.txt', 'w') as f:
        f.write(static)
        f.write('\n')
        f.write(dynamic)

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
    static = ''
    with open ('copy_circuit_static.txt', 'r') as f:
        for line in f.readlines():
            static += line
    
    dynamic = ''
    with open ('copy_circuit_dynamic.txt', 'r') as f:
        for line in f.readlines():
            dynamic += line
    
    with open('copy_circuit.txt', 'w') as f:
        f.write(static)
        f.write('\n')
        f.write(dynamic)

def create_writeLeft_circuit(alphabet):
    with open('writeLeft_circuit_dynamic.txt', 'w') as f:
        for c in alphabet:
            f.write('writeLeft2 ' + c + ' * l wl' + c + '\n')
        for c in alphabet:
            f.write('\nwl' + c + ' # * l wl' + c + '1\n')
            f.write('wl' + c + ' * * l *\n\n')
            f.write('wl' + c + '1 _ '+ c +' r writeLeft3 \n')
            f.write('wl' + c + '1 * * l *\n')
    static = ''
    with open ('writeLeft_circuit_static.txt', 'r') as f:
        for line in f.readlines():
            static += line
    
    dynamic = ''
    with open ('writeLeft_circuit_dynamic.txt', 'r') as f:
        for line in f.readlines():
            dynamic += line
    
    with open('writeLeft_circuit.txt', 'w') as f:
        f.write(static)
        f.write('\n')
        f.write(dynamic)

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
    static = ''
    with open ('moveToFront_circuit_static.txt', 'r') as f:
        for line in f.readlines():
            static += line
    
    dynamic = ''
    with open ('moveToFront_circuit_dynamic.txt', 'r') as f:
        for line in f.readlines():
            dynamic += line
    
    with open('moveToFront_circuit.txt', 'w') as f:
        f.write(static)
        f.write('\n')
        f.write(dynamic)

def create_find_circuit(alphabet):
    with open('find_circuit_dynamic.txt', 'w') as f:
        for c in alphabet:
            f.write('find ' + c + ' _ r f' + c + '\n')
        for c in alphabet:
            f.write('\nf' + c + ' ' + c + ' * l moveWord\n')
            f.write('f' + c + ' * * r f' + c + '1\n')
            f.write('f' + c + ' _ * r *\n\n')
            f.write('f' + c + '1 _ * r f' + c + '\n')
            f.write('f' + c + '1 * * r *\n')
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

alphabet = ['0', '1', 'a', 'b', 'c', 'd', 'o', '(', ')', '-']

def create_huffman_encoding_dynamic(alphabet):
    create_move_circuit(alphabet)
    create_copy_circuit(alphabet)
    create_writeLeft_circuit(alphabet)
    create_moveToFront_circuit(alphabet)
    create_find_circuit(alphabet)

    move = ''
    with open ('move_circuit.txt', 'r') as f:
        for line in f.readlines():
            move += line
    copy = ''
    with open ('copy_circuit.txt', 'r') as f:
        for line in f.readlines():
            copy += line                                
    writeLeft = ''
    with open ('writeLeft_circuit.txt', 'r') as f:
        for line in f.readlines():
            writeLeft += line
    moveToFront = ''
    with open ('moveToFront_circuit.txt', 'r') as f:
        for line in f.readlines():
            moveToFront += line
    find = ''
    with open ('find_circuit.txt', 'r') as f:
        for line in f.readlines():
            find += line

    with open("../huffman_encoding_dynamic.txt", "w") as f:
        f.write(move)
        f.write('\n')
        f.write(copy)
        f.write('\n')
        f.write(writeLeft)
        f.write('\n')
        f.write(moveToFront)
        f.write('\n')
        f.write(find)
        f.write('\n')
            

# Make sure to run this in the circuit directory
alphabet = ['0', '1', 'a', 'b', 'c', 'd', 'o', '(', ')', '-']
create_huffman_encoding_dynamic(alphabet)