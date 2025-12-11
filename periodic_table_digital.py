from dataclasses import dataclass
from typing import List, Optional

@dataclass
class DigitalAtom:
    atomic_number: int
    symbol: str
    name: str
    atomic_mass: float
    valence_electrons: int
    oxidation_states: List[int]

    def can_bond_with(self, other: 'DigitalAtom') -> Optional[str]:
        """
        Simplified bonding: if any oxidation state pair sums to zero,
        return 'ionic' when a ±1 is involved, else 'covalent'.
        """
        for ox1 in self.oxidation_states:
            for ox2 in other.oxidation_states:
                if ox1 + ox2 == 0:
                    return "ionic" if (abs(ox1) == 1 or abs(ox2) == 1) else "covalent"
        return None

# Minimal demo dataset (expandable to full periodic table)
PERIODIC_TABLE = {
    "H":  {"atomic_number": 1,  "name": "Hydrogen", "atomic_mass": 1.008,  "valence_electrons": 1, "oxidation_states": [1, -1]},
    "O":  {"atomic_number": 8,  "name": "Oxygen",   "atomic_mass": 15.999, "valence_electrons": 6, "oxidation_states": [-2]},
    "Na": {"atomic_number": 11, "name": "Sodium",   "atomic_mass": 22.990, "valence_electrons": 1, "oxidation_states": [1]},
    "Cl": {"atomic_number": 17, "name": "Chlorine", "atomic_mass": 35.45,  "valence_electrons": 7, "oxidation_states": [-1]},
    "C":  {"atomic_number": 6,  "name": "Carbon",   "atomic_mass": 12.011, "valence_electrons": 4, "oxidation_states": [-4, 4]},
    "S":  {"atomic_number": 16, "name": "Sulfur",   "atomic_mass": 32.06,  "valence_electrons": 6, "oxidation_states": [-2, 4, 6]},
    "Hg": {"atomic_number": 80, "name": "Mercury",  "atomic_mass": 200.59, "valence_electrons": 2, "oxidation_states": [1, 2]},
    "Bi": {"atomic_number": 83, "name": "Bismuth",  "atomic_mass": 208.98, "valence_electrons": 5, "oxidation_states": [3, 5]},
}

# Build atoms
atoms = {sym: DigitalAtom(symbol=sym, **props) for sym, props in PERIODIC_TABLE.items()}

# Example: test bonds
pairs = [("Na","Cl"), ("H","O"), ("C","O"), ("Hg","S"), ("Bi","S")]
for a, b in pairs:
    bond = atoms[a].can_bond_with(atoms[b])
    print(f"{a}-{b}: {bond}")
