class VirtualReaction:
    def __init__(self, atoms: List[DigitalAtom]):
        self.atoms = atoms
        self.bonds = []  # list of (i, j, type)

    def run(self, ruleset):
        # apply ruleset to propose bonds and validate constraints
        pass
