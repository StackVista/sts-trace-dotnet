
```toml
concurrent = 1
check_interval = 0

[session_server]
  session_timeout = 1800

[[runners]]
  name = "MSEDGEWIN10 - Experimental windows runner"
  url = "https://gitlab.com/"
  token = "BLABLA"
  executor = "shell"
  builds_dir = "c:/workspaces/builds"
  cache_dir = "c:/workspaces/caches"
  environment = [""]
  shell = "cmd"
  [runners.custom_build_dir]
  [runners.cache]
    [runners.cache.s3]
    [runners.cache.gcs]
```
