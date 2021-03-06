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
            before='Login',
            width=200)

with simple.window('Moon Overwatch Leveling Bot'):
    core.set_style_item_spacing(15, 15)
    core.set_style_frame_padding(5, 5)
    core.add_additional_font('Roboto-Regular.ttf', 14)

    core.add_image('logo', 'moon.png')
    core.add_separator()
    
    core.add_input_text(
            'Account Email',
            default_value='tigolbitties@battle.net',
            width=200)

    core.add_input_text(
            'Account Password',
            default_value='weShouldBuffBrig!69',
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
