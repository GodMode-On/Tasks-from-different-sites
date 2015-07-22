from string import digits

def count_nums(text, position):
    '''
    Returns how many digits in a row in text, starting from pos.
    '''
    
    if not text[position].isdigit():
        return False
    count = 0
    while text[position].isdigit():
        count += 1
        position += 1
        if position == len(text):
            return count
    return count
    
    
def get_rid_of_brackets(molecule):
    '''
    Something like that:
    K4[ON(SO3)2]2 -> K4ONSO3SO3ONSO3SO3
    '''
    brackets = {'(' : ')',
                '[' : ']',
                '{' : '}'}
                
    while any(bracket in molecule for bracket in brackets.keys()):
        for i in range(len(molecule)-1, -1, -1):
            if molecule[i] in brackets.values():
                for j, element in list(enumerate(molecule))[::-1]:
                    if element in brackets.keys():
                        if brackets[element] == molecule[i]:
                            start = molecule[:j]
                            in_brackets = molecule[j+1:i]
                            number_len = count_nums(molecule, i+1)
                            if number_len:
                                times = int(molecule[i+1:i+number_len+1])
                            else:
                                times = 1
                            end = molecule[i+number_len+1:]
                            break
                molecule = start + in_brackets * times + end
                break
    return molecule
    
def molecule_to_atoms(molecule):
    '''
    Something like that:
    H2SO3 -> ['H2', 'S', 'O3']
    '''
    
    molecule_without_brackets = get_rid_of_brackets(molecule)
    molecule_split = ''
    for element in molecule_without_brackets:
        if element.isupper():
            molecule_split += ' ' + element
        else:
            molecule_split += element           
    return molecule_split.lstrip().split()
    
def parse_molecule(molecule):
    '''
    Returns number of atoms of each element contained in the molecule
    '''
    
    atom_list = molecule_to_atoms(molecule)
    
    result = dict()
    for element in atom_list:
        if any(digit in element for digit in digits):
            if element[1].isdigit():
                atom = element[0]
                count = element[1:]
                
            else:
                atom = element[:2]
                count = element[2:]
        else:
                atom = element
                count = 1
        if atom in result.keys():
            result[atom] += int(count)
        else:
            result[atom] = int(count)
