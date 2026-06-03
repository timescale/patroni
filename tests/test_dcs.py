from patroni.dcs import Status


def test_status_from_node_parses_upgrade_annotation_string():
    # On Kubernetes, annotation values are JSON strings. Status.from_node must
    # json-decode the `upgrade` annotation back into an Upgrade.
    annotations = {
        "optime": "123",
        "upgrade": '{"initiator":"m1","state":"precheck","source_sysid":"s","source_version":"17",'
                   '"target_sysid":null,"target_version":"18","shutdown_lsn":null,'
                   '"downtime_start":null,"config":{},"progress":[]}',
    }
    status = Status.from_node(annotations)
    assert status.upgrade is not None
    assert status.upgrade.state.value == "precheck"
    assert status.upgrade.target_version == "18"
    assert status.last_lsn == 123
