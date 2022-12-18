import numpy as np
import itertools
import copy


class Rock:
    def __init__(self, body, x=2, z=None):
        """x, z are the coordinates of the rocks lower left corner"""
        self.body = body
        self.x = x
        self.z = z
        
    @property
    def shape(self):
        return self.body.shape

    def embed(self, i_body):
        """Embed a layer of the rock body in air"""
        layer = np.zeros(7, dtype=int)
        layer[self.x:self.x + self.shape[1]] = self.body[i_body]
        return layer

    def view(self):
        body = self.body
        body = np.array(body, dtype=str)
        body[body == '1'] = '#'
        body[body == '0'] = '.'
        s = ''
        for row in body:
            s += ''.join(row) + '\n'
        print(s)
        


class Tetris:
    def __init__(self, fname):
        with open(fname) as f:
            jets_text = f.read().strip()

        self.jets_cycle = itertools.cycle([1 if j == '>' else -1 for j in jets_text])
            
        self.rock_bodies = [
            np.array([[1, 1, 1, 1]]),
            np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]]),
            np.array([[1, 1, 1], [0, 0, 1], [0, 0, 1]]),
            np.array([1, 1, 1, 1])[:, None],
            np.array([[1, 1], [1, 1]]),
        ]
        self.rock_bodies_cycle = itertools.cycle(self.rock_bodies)
        self.pile = [np.ones(7, dtype=int)]
        self.height = 0

    def view(self):
        pile = self.pile.copy()
        pile.reverse()
        pile = np.array(pile, dtype=str)
        pile[pile == '1'] = '#'
        pile[pile == '0'] = '.'
        s = ''
        for row in pile:
            s += ''.join(row) + '\n'
        print(s)
            
    def push(self, rock, jet):
        pile = self.pile
        pile_z = len(self.pile) - 1
        end = rock.x + rock.shape[1] - 1
        if rock.x + jet < 0:
            return
        if end + jet > 6:
            return
        if rock.z > pile_z: 
            rock.x += jet
            return
        else:
            rock.x += jet
            for i, z in enumerate(range(rock.z, rock.z + rock.shape[0])):
                if z <= pile_z:
                    layer_body = rock.embed(i)
                    if np.any(layer_body & pile[z]):
                        rock.x -= jet
                        return
        
    def move_down(self, rock):
        pile = self.pile
        pile_z = len(pile) - 1
        if rock.z > pile_z + 1:
            rock.z -= 1
            return True
        else:
            for i, z in enumerate(range(rock.z, rock.z + rock.shape[0])):
                if z <= pile_z + 1:
                    layer_rock = rock.embed(i)
                    layer_below = pile[z - 1]
                    if np.any(layer_rock & layer_below):
                        self.absorb(rock)
                        return False
            
            rock.z -= 1
            return True

    def absorb(self, rock):
        pile = self.pile
        pile_z = len(self.pile) - 1
        pile_new = []
        for i, z in enumerate(range(rock.z, rock.z + rock.shape[0])):
            layer_new = rock.embed(i)
            if z <= pile_z:
                pile[z] += layer_new
            else:
                pile_new.append(layer_new)
        if len(pile_new) > 0:
            pile.extend(pile_new)

    def run(self, num_rocks):
        self.height = 0
        for i, body in enumerate(itertools.islice(self.rock_bodies_cycle, num_rocks)):
            rock = Rock(body, x=2, z=len(self.pile) + 3)
            self.push(rock, next(self.jets_cycle))
            while self.move_down(rock):
                self.push(rock, next(self.jets_cycle))

            # renormalize 
            if np.all(self.pile[-1]):
                self.height += len(self.pile) - 1
                self.pile = [self.pile[-1]]
                
        self.height += len(self.pile) - 1


if __name__ == '__main__':

    # part I
    # tetris = Tetris('./input.txt')
    # tetris.run(500000)
    # print(tetris.height)

    # part II
    tetris = Tetris('./input.txt')
    # check for periodic repetitions of patterns in the pile,
    # here I've searched for rows with all 1s.

    # initial index (index = num_rocks -1) and height
    # periodicity is estalbished after (init + 1) rocks have fallen
    # the pile is then h_init units high
    init = 1870
    h_init = 2950

    # period and height change over period
    period = 1715 # = 1585 + 130
    h_period = 2690 # = 2475 + 215

    target = 1000000000000
    target_red = target - init
    quotient = target_red // period
    remainder = target_red % period

    h_predicted = h_init + quotient*h_period

    # calc height for remainer
    tetris.run(init + period + remainder)
    h_remainder = tetris.height - h_init - h_period
    h_predicted += h_remainder
    print(h_predicted)
