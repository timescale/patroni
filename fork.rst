.. _fork:

Timescale patroni fork
======================

Why we fork?
------------

Certain changes, i.e. restricting the frequency of updates to the pod members, for now carry tradeoffs that are not acceptable
for the upstream, i.e. the replica xlog information obtained from the API is inaccurate. Eventual goal is to refine and contrib those changes there.

TS_1
-----

- Add ``xlog_cache_ttl`` parameter for the Kubernetes DCS

  Setting it to multiple of ``loop_wait`` prevents frequent pod updates, reducing the load on the API server, at the expense of stale value of the xlog position in the member's metadata.

TS_2
----

- add `pg_rewind_log_progress` and `pg_rewind_log_debug` patroni options to include `--progress` and `--debug` in the pg_rewind command line. `pg_rewind_log_progress` is enabled by default.
- restrict `ydiff` to 1.2.x and 1.3x to prevent breaking `patronictl edit-config`. This will be reverted once the fork is rebased to upstream.
