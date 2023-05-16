"""
text: "fooziman" output => "foozimaN"
"""

def fn_hack_4():

    result = "fooziman"
    result = result[:-1] + "N"
    print(result)
    
    return result