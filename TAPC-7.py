# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 10:38:41 2018

@author: Maria
"""
import re

expectedName = 'Anonymous Ltd.'
sampleText1 = """
Copyright in these documents published on Hitachi Chemical World-Wide Web Server is owned by Hitachi Ltd.
Hitachi Ltd. authorizes you to copy the documents for non-commercial use within your organization only, 
provided that the above copyright notice appears in each and all copies. 
Except as expressly provided above, nothing contained herein shall be construed as conferring any license or 
right under any Hitachi Chemical's copyright, patent, trademark or other intellectual property rights.

This publication may include any inaccuracies or errors. These documents are provided "as is" without warranty of 
any kind, either expressed or implied, including, but not limited to, implied warranties of merchantability, fitness 
for a particular purpose, or non-infringement of any third party's rights of any kind. In no event, Hitachi Ltd. shall be 
liable for any special, indirect or consequential damages whatsoever or any damages, whether in contract, tort or otherwise, 
arising out of or in connection with the use of the documents herein. These documents are subject to change at any time without 
notice.

"""

sampleText2 = """
Copyright in these documents published on Hitachi Chemical World-Wide Web Server is owned by Hitachi Ltd.
Anonymous Ltd. authorizes you to copy the documents for non-commercial use within your organization only, 
provided that the above copyright notice appears in each and all copies. 
Except as expressly provided above, nothing contained herein shall be construed as conferring any license or 
right under any Hitachi Chemical's copyright, patent, trademark or other intellectual property rights.

This publication may include any inaccuracies or errors. These documents are provided "as is" without warranty of 
any kind, either expressed or implied, including, but not limited to, implied warranties of merchantability, fitness 
for a particular purpose, or non-infringement of any third party's rights of any kind. In no event, Anonymous Ltd. shall be 
liable for any special, indirect or consequential damages whatsoever or any damages, whether in contract, tort or otherwise, 
arising out of or in connection with the use of the documents herein. These documents are subject to change at any time without 
notice.

"""

sampleText3 = """
Copyright in these documents published on Hitachi Chemical World-Wide Web Server is owned by Anonymous Ltd.
Anonymous Ltd. authorizes you to copy the documents for non-commercial use within your organization only, 
provided that the above copyright notice appears in each and all copies. 
Except as expressly provided above, nothing contained herein shall be construed as conferring any license or 
right under any Hitachi Chemical's copyright, patent, trademark or other intellectual property rights.

This publication may include any inaccuracies or errors. These documents are provided "as is" without warranty of 
any kind, either expressed or implied, including, but not limited to, implied warranties of merchantability, fitness 
for a particular purpose, or non-infringement of any third party's rights of any kind. In no event, Anonymous Ltd. shall be 
liable for any special, indirect or consequential damages whatsoever or any damages, whether in contract, tort or otherwise, 
arising out of or in connection with the use of the documents herein. These documents are subject to change at any time without 
notice.

"""

def validateCompanyName(content, expectedN):
    '''
    content: string, a text.
    expectedN: string, variable set to 'Anonymous Ltd.'
    
    returns: boolean, False if there are company names different than 
    'Anonymous Ltd.'
    '''
    counter = 0
    pattern = re.compile(r'(\w+) Ltd\.')
    matches = pattern.finditer(content)
    i = 0
    for match in matches:
        temp = match.group(0)
        if temp == expectedN:
            counter += 1
        i += 1
    if counter == i:
#        print('All annonymous, ok')
        return True
    else:
#        print('Sorry, ' + str(counter) + ' out of ' + str(i) + ' matches are validated')
        return False


print(validateCompanyName(sampleText3, expectedName))
