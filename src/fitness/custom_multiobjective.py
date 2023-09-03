from fitness.base_ff_classes.base_ff import base_ff


class minimise_nodes(base_ff):
    """
    Fitness function class for minimising the number of nodes in a
    derivation tree.
    """

    def __init__(self):
        # Initialise base fitness function class.
        super().__init__()

    def evaluate(self, ind, **kwargs):
        return ind.nodes


class custom_multiobjective(base_ff):
    """
    Fitness function class for minimising the number of nodes in a
    derivation tree.
    """

    def __init__(self):
        # Initialise base fitness function class.
        super().__init__()

    def evaluate(self, ind, **kwargs):
        if not ind.genome:
            eff_length = None
        elif ind.invalid:
            eff_length = len(ind.genome)
        else:
            eff_length = min(len(ind.genome), ind.used_codons)
        if eff_length < 30:
            return 10
        return 0
