import pandas as pd
from rdkit.Chem import PandasTools
pp = pd.read_csv('SAMPL.csv', names=['iupac', 'smiles', 'expt', 'calc'])
PandasTools.AddMoleculeColumnToFrame(pp,'smiles','molecule')
PandasTools.WriteSDF(pp, 'solubility_data.sdf', molColName='molecule')
fp=open('sol_lables.yaml','w')
for value in list(pp['expt']):
        fp.write("- value: "+str(value)+" \n")
        fp.write("  num_bonds_in_molecule: 1 \n")
        fp.write("  bond_index: 0 \n")
fp.close()
fp=open('sol_attributes.yaml','w')
for value in list(pp['expt']):
        fp.write("- charge: 0 \n")
#import readline; print('\n'.join([str(readline.get_history_item(i + 1)) for i in range(readline.get_current_history_length())]))