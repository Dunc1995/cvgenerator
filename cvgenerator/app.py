import cvgenerator.workflows as wf
from cvgenerator.forms import menu, choice

def run():
    edit_menu = menu('edit', 'What would you like to create?')
    edit_menu.add_options([
        choice('Insert data entry', wf.insert_data),
        choice('Insert new tag', wf.insert_tag),
        choice('Insert new data type', wf.insert_data_type),
        choice('Edit data type schemas', wf.edit_type_schemas),
        choice('Assign data tags', wf.assign_tags_to_data)
    ])

    main_menu = menu('main', 'What would you like to do?', escapable=False)
    main_menu.add_options([
        choice('Compile my CV', wf.placeholder),
        choice('Edit CV Data', edit_menu.show)
    ])
    main_menu.show()
    wf.on_exit()

if __name__ == "__main__":
    run()