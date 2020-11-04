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
    core.set_style_item_spacing(15, 15)
    core.set_style_frame_padding(5, 5)
#    core.set_global_font_scale(1.5)
    core.add_additional_font('Roboto-Black.ttf', 14)
#    core.add_additional_font('Yellowtail-Regular.ttf', 16)

    core.add_text('Moon')
    core.add_separator()
    
    core.add_input_text(
            'Account Email',
            default_value='smurf@cock.li',
            width=200)

    core.add_input_text(
            'Account Password',
            default_value='mature_password!',
            width=200)
    
    core.add_checkbox(
            'Multiple Accounts',
            default_value=False,
            callback=multiple_accounts)
    
    core.add_same_line()
    core.add_button('Login', callback=login, width=85)
    core.add_separator()

core.set_theme('Red')
core.start_dearpygui(primary_window='Moon Overwatch Leveling Bot')
