import pyperclip

restricted = ['%', '@']

def create_move_cicuit(alphabet):
    with open('move_circuit_draft.txt', 'w') as f:
        for c in alphabet:
            f.write('move1 ' + c + ' @ r m' + c + '\n')
        f.write('move1 % _ r move2\n')
        for c in alphabet:
            f.write('\nm' + c + ' $ * r m' + c + '1\n')
            f.write('m' + c + ' * * r *\n\n')
            f.write('m' + c + '1 _ '+ c +' l move \n')
            f.write('m' + c + '1 * * r *\n')
    with open ('move_circuit_draft.txt', 'r') as f:
        s = ''
        for line in f.readlines():
            s += line
        pyperclip.copy(s)

# with open('f1.txt', 'w') as f:
#         for x in alphabet:
#             f.write(';m' + x + '\n')
#             f.write('\n')
        


def create_copy_cicuit(alphabet):
    with open('copy_circuit_draft.txt', 'w') as f:
        for c in alphabet:
            f.write('copy1 ' + c + ' @ l w' + c + '\n')
        f.write('copy1 % _ r copy2\n')
        for c in alphabet:
            f.write('\nw' + c + ' _ ' + c + ' r w' + c + '1\n\n')
            f.write('w' + c + '1 $ * r w' + c + '2\n')
            f.write('w' + c + '1 * * r *\n\n')
            f.write('w' + c + '2 _ '+ c +' l copy \n')
            f.write('w' + c + '2 * * r *\n')
    with open ('copy_circuit_draft.txt', 'r') as f:
        s = ''
        for line in f.readlines():
            s += line
        pyperclip.copy(s)

alphabet = ['0', '1', 'a', 'b', 'c', 'd', 'o', '(', ')']
# create_move_cicuit(alphabet)

alphabet = ['0', '1']
create_copy_cicuit(alphabet)