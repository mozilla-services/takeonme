---
name: Add a new service or resource
about: Request and review steps to add a new service or resource
title: ''
labels: ''
assignees: ''

---


## Adding a new service

Recommended Steps:

1. [set up `takeonme` for development](https://github.com/mozilla-services/takeonme/#developing)

1. Run `cp -r example_service takeonme/` to recursively copy the
   example resource into the package namespace.

1. Run `mv takeonme/{example_service,service_name}`

1. Replace `example_*` with the service or resource name in
   `takeonme/service_name/commands.py`

1. Find or implement a client library for the service's API. Prefer
   first party and Python libraries

1. Run `poetry add` to add the client libary to `takeonme` dependencies

1. Add `list_.add_command(takeonme.service_name.commands.list_)` to
   `takeonme/cli.py`

## Adding a new resource

Requirements:

- [ ] this resource can be hijacked (i.e. it's on
      https://github.com/EdOverflow/can-i-take-over-xyz, a similar
      list, or reference an accepted bug)

- [ ] an API exists to enumerate the resource


Add a list subcommand to `takeonme/service_name/commands.py` that:

- [ ] includes a link to the API endpoint in the docstring or the
      docstring of a client method it uses to fetch the resource

- [ ] writes to the configured output file (accessible from
      `ctx.obj["output"]`). Prefer a format other tools can consume
      directly.

- [ ] implements the flag `--json` and writes complete API output in
      JSON format (i.e. `takeonme list service_name resource --json`)

- [ ] reads JSON output from stdin and write the plaintext output to
      stdout (i.e. `takeonme list --input=- service_name resource
      <(takeonme list service_name resource --json)` without making
      API calls
