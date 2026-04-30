### Component List

- orchestrator
    - this gets called from main and is the main 'orchestrator' of the project.
- configuration adapter
    - this is a bridge to the configuration file so that i can change it if need be. when the orchestrator calls for config, it can recheck the file so that its always updated when the pipeline runs
- hardcover client
    - this provides premade methods to get certain data from hardcover
- library handler
    - this interacts with whatever library or libraries you have set up as your local, and provides a way to get books from opds and such.
- bookparser
    - this talks to the hardcover adapter and the library handler, getting the books list from each. then it diffs the list.
- torrent handler
    - torrents things
- torrent tracker
    - manages trackers
