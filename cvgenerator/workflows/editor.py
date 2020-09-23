def show_help():
    text = '''
    --- Summary ---
    Schemas exist to enforce your document's structure. The schemas_hierarchy.yaml in your
    ./cv_bin/config directory defines your document's schema types. The cvgenerator application
    parses this .yaml file to create JSON objects that define metadata for every piece of 
    information you add to your document.
    --- Commands ---
    1. \"Edit default schema names\" allows you to set default names for all of your schemas.
    For example a \'work_experience_section\' will always be called \"Work Experience\".
    2. \"Edit default schema tags\"  allows you to assign default tags to all of your document's
    schemas. For example a Summary section may be optional whereas a Work Experience section is
    mandatory.
    3. \"Refresh schema hierarchy\" will reload the schema_hierarchy.yaml config file and
    repopulate the schemas table in db.json. IT IS WORTH NOTING that this may remove any
    tags that have been previously added to your data schemas; this should only be used if
    you're planning on defining a new document structure.
    '''
    #TODO find a better way to print
    print(text)