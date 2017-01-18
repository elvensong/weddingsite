;; Pony mode config for the megacorp project
((nil . ;; This applies these settings regardless of major mode

  ((pony-settings (make-pony-project
                   :python "/usr/bin/python"
                   :pythonpath "/home/david/megacorp/libs/projectzero"
                   :settings "local_settings_file"
                   :appsdir "testproject/apps/")
))))
