import dearpygui.core as core
import dearpygui.simple as simple


def login(sender, data):
    pass

def multiple_accounts(sender, data):
    core.delete_item('Account Email')
    core.delete_item('Account Password')

    core.add_input_text(
            'Accounts File',
            default_value='accs_to_level.txt',
            before='Login')


with simple.window('Moon Overwatch Leveling Bot'):
    core.add_input_text('Account Email', default_value='smurf@cock.li')
    core.add_input_text('Account Password', default_value='mature_password!')
    core.add_checkbox('Multiple Accounts', default_value=False, callback=multiple_accounts)
    core.add_button('Login', callback=login)

core.set_theme('Red')
core.start_dearpygui(primary_window='Moon Overwatch Leveling Bot')
