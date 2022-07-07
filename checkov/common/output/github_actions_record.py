import typing
from typing import Any

from checkov.common.output.record import Record


class GithubActionsRecord(Record):
    def __init__(self, record: Record, triggers: typing.Set[str], jobs: typing.Dict[str, Any], workflow_name: str):
        super().__init__(record.check_id, record.check_name, record.check_result, record.code_block, record.file_path,
                         record.file_line_range, record.resource, record.evaluations, record.check_class,
                         record.file_abs_path, record.entity_tags, record.caller_file_path,
                         record.caller_file_line_range, bc_check_id=record.bc_check_id,
                         resource_address=record.resource_address,
                         severity=record.severity, bc_category=record.bc_category, benchmarks=record.benchmarks)
        self.triggers = triggers,
        self.jobs = jobs
        self.workflow_name = workflow_name
