

print('Checking if installed packages import correctly....')
import numpy; 
import scipy; 
import skimage; 
import Bio; 
import matplotlib; 
import pandas; 
import tifffile; 
import trackpy;
import seaborn;
print('All packages imported correctly.')

try: 
	import torch; 
	import cellpose; 
	print('PyTorch has GPU enabled?')
	print(torch.cuda.is_available())
except:
	print('torch and cellpose skipped for now')

print('Check that biopython isnt blank:')
from Bio import SeqIO
try:
    SeqIO.parse
    print('Biopython is not blank.')
except:
    print('Biopython is blank, not installed correctly.')



