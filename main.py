import NRP
import os

classical_dataset = "nrp2.txt"
realistic_dataset = "nrp-e3.txt"

pwd = os.path.abspath(os.path.dirname(__file__))
classical_dataset = os.path.join(pwd, "dataset", "classic-nrp", classical_dataset)
realistic_dataset = os.path.join(pwd, "dataset", "realistic-nrp", realistic_dataset)

# The cost ratio
ratio = 0.5
gen100 = 100
gen500 = 500
gen1000 = 1000

#classical NRP
NRP.nrp_random(classical_dataset, ratio, gen100, True)
NRP.nrp_random(classical_dataset, ratio, gen500, True)
NRP.nrp_random(classical_dataset, ratio, gen1000, True)

NRP.nrp_single(classical_dataset, ratio, gen100, True)
NRP.nrp_single(classical_dataset, ratio, gen500, True)
NRP.nrp_single(classical_dataset, ratio, gen1000, True)

NRP.nrp_multi(classical_dataset, ratio, gen100, True)
NRP.nrp_multi(classical_dataset, ratio, gen500, True)
NRP.nrp_multi(classical_dataset, ratio, gen1000, True)

# Realistic NRP
NRP.nrp_single(realistic_dataset, ratio, gen100, True)
NRP.nrp_single(realistic_dataset, ratio, gen500, True)
NRP.nrp_single(realistic_dataset, ratio, gen1000, True)

NRP.nrp_single(realistic_dataset, ratio, gen100, True)
NRP.nrp_single(realistic_dataset, ratio, gen500, True)
NRP.nrp_single(realistic_dataset, ratio, gen1000, True)

NRP.nrp_multi(realistic_dataset, ratio, gen100, True)
NRP.nrp_multi(realistic_dataset, ratio, gen500, True)
NRP.nrp_multi(realistic_dataset, ratio, gen1000, True)

# Comparisons
# We first compare single and multi solutions
NRP.compare(classical_dataset, ratio, False, 0, True, gen1000, True, gen1000)
# Then we compare all
NRP.compare(classical_dataset, ratio, True, gen1000, True, gen1000, True, gen1000)

# Do same for realistic NRP
NRP.compare(realistic_dataset, ratio, False, 0, True, gen1000, True, gen1000)
NRP.compare(realistic_dataset, ratio, True, gen1000, True, gen1000, True, gen1000)

