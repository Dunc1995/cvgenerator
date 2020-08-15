import cvgenerator.workflows as wf
from cvgenerator.forms import menu, choice

def run():
    additions_menu = menu('edit', 'What would you like to create?')
    additions_menu.add_options([
        choice('Generate a work experience template', wf.placeholder),
        choice('Generate an education template', wf.placeholder)
    ])

    main_menu = menu('main', 'What would you like to do?', escapable=False)
    main_menu.add_options([
        choice('Compile my CV', wf.placeholder),
        choice('Add to my CV', additions_menu.show)
    ])
    main_menu.show()
    wf.on_exit()

if __name__ == "__main__":
    run()