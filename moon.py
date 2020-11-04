import dearpygui.core as core
import dearpygui.simple as simple


def login(sender, data):
    pass

with simple.window('Moon Overwatch Leveling Bot'):
    core.add_input_text('Account Email', default_value='smurf@cock.li')
    core.add_input_text('Account Password', default_value='mature_password!')
    core.add_button('Login', callback=login)

core.set_theme('Red')
core.start_dearpygui(primary_window='Moon Overwatch Leveling Bot')
