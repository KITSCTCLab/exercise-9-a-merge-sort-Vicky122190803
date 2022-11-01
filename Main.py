Skip to content
Search or jump to…
Pull requests
Issues
Marketplace
Explore
 
@Vicky122190803 
KITSCTCLab
/
exercise-9-a-merge-sort-Vicky122190803
Public
generated from brightvarghese/22_ODD_DS_Exercise-9.a
Code
Issues
Pull requests
1
Actions
Projects
Wiki
Security
Insights
exercise-9-a-merge-sort-Vicky122190803/Main.py /
@github-classroom
github-classroom Initial commit
Latest commit d99e857 3 minutes ago
 History
 1 contributor
16 lines (13 sloc)  322 Bytes

from typing import List

def merge_sort(data) -> None:
  # Write code here


# Do not change the following code
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
merge_sort(data)
print(data)
Footer
© 2022 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
exercise-9-a-merge-sort-Vicky122190803/Main.py at main · KITSCTCLab/exercise-9-a-merge-sort-Vicky122190803
