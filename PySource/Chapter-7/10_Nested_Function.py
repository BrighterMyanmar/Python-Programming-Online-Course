def aa():
    name = "Mg Mg"
    print(f"I am Top Level aa function")
    def bb():
        print(f"I am aa => bb fun, Second Level")
        def cc():
            print(f"I am aa => bb => cc func, Third Level")
            def dd():
                print(f"I am aa => bb => cc => dd fun , Fourth Level {name}")
            dd()
        cc()
    bb()

aa()