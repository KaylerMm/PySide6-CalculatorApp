import qdarktheme

from variables import (DARKER_PRIMARY_COLOR, DARKEST_PRIMARY_COLOR,
                       PRIMARY_COLOR)

qss = f"""
    PushButton[cssClass="specialButton"] {{
    QPushButton[cssClass="specialButton"] {{
        color: #fff;
        background: {PRIMARY_COLOR};
    }}
    PushButton[cssClass="specialButton"]:hover {{
    QPushButton[cssClass="specialButton"]:hover {{
        color: #fff;
        background: {DARKER_PRIMARY_COLOR};
    }}
    PushButton[cssClass="specialButton"]:pressed {{
    QPushButton[cssClass="specialButton"]:pressed {{
        color: #fff;
        background: {DARKEST_PRIMARY_COLOR};
    }}
"""

def set_theme():
    return qdarktheme.load_stylesheet('dark')