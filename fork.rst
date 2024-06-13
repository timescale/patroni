.. _fork:

Timescale patroni fork
======================


TS_1
-----

- Add ``xlog_cache_ttl`` parameter for the Kubernetes DCS

  Setting it to multiple of ``loop_wait`` prevents frequent pod updates, reducing the load on the API server, at the expense of stale value of the xlog position in the member's metadata.
