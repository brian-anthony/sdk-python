#  Copyright 2022 The CDEvents Authors
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
#  SPDX-License-Identifier: Apache-2.0
"""Events under dev.cdevents.branch."""
from dataclasses import dataclass
from datetime import datetime
from typing import Dict, Optional, Union

from cdevents.cdevent import SPEC_VERSION, CDEvent
from cdevents.context import Context
from cdevents.subject import Subject


@dataclass
class BranchSubject(Subject):
    """Subject for branch-related events."""

    repository: Optional[Dict]
    """A reference to the repository where the branch event happened."""


# region BranchCreatedEvent


@dataclass
class BranchCreatedEvent(CDEvent):
    CDEVENT_TYPE = "dev.cdevents.branch.created." + SPEC_VERSION

    subject: BranchSubject
    """Branch subject."""


def new_branch_created_event(
    context_id: str,
    context_source: str,
    context_timestamp: datetime,
    subject_id: str,
    subject_source: str,
    repository: Optional[Dict],
    custom_data: Union[str, Dict, None],
    custom_data_type: str,
) -> BranchCreatedEvent:
    """Creates a new branch created CDEvent."""

    context = Context(
        type=BranchCreatedEvent.CDEVENT_TYPE,
        version=SPEC_VERSION,
        id=context_id,
        source=context_source,
        timestamp=context_timestamp,
    )

    subject = BranchSubject(id=subject_id, source=subject_source, repository=repository)

    event = BranchCreatedEvent(
        context=context, subject=subject, custom_data=custom_data, custom_data_type=custom_data_type
    )

    return event


# endregion BranchCreatedEvent


# region BranchDeletedEvent


@dataclass
class BranchDeletedEvent(CDEvent):
    CDEVENT_TYPE = "dev.cdevents.branch.deleted." + SPEC_VERSION

    subject: BranchSubject
    """Branch subject."""


def new_branch_deleted_event(
    context_id: str,
    context_source: str,
    context_timestamp: datetime,
    subject_id: str,
    subject_source: str,
    repository: Optional[Dict],
    custom_data: Union[str, Dict, None],
    custom_data_type: str,
) -> BranchDeletedEvent:
    """Creates a new branch deleted CDEvent."""

    context = Context(
        type=BranchDeletedEvent.CDEVENT_TYPE,
        version=SPEC_VERSION,
        id=context_id,
        source=context_source,
        timestamp=context_timestamp,
    )

    subject = BranchSubject(id=subject_id, source=subject_source, repository=repository)

    event = BranchDeletedEvent(
        context=context, subject=subject, custom_data=custom_data, custom_data_type=custom_data_type
    )

    return event


# endregion BranchDeletedEvent
