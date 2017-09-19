import ui

def mths_button_touch_up_inside(sender):
    #displays the English version
    view['school_name_label'].text = ('Mother Teresa HS')
    view['team_name_label'].text = ('Titans')

def st_joes_button_touch_up_inside(sender):
    #displays the English version
    view['school_name_label'].text = ('St. Joes HS')
    view['team_name_label'].text = ('Jaguars')

def st_marks_button_touch_up_inside(sender):
    #displays the English version
    view['school_name_label'].text = ('St. Marks HS')
    view['team_name_label'].text = ('Lions')

view = ui.load_view()
view.present('sheet')
