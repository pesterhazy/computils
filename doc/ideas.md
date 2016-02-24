Concepts and Ideas
--------------------

Computil commands

- `with-tempdir`: runs the nested command with a tempdir that is guaranteed to
  be cleaned up
- `with-resource`: run a command and make sure that the acquired resource is
  cleaned up
- `limit-time`: interrupt a command if its runtime exceeds a given number of seconds
- `on-s3`: in the following commands, grab input files from S3 and upload output
  files to S3
