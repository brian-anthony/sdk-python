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
"""Events under dev.cdevents.artifact."""
from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, Union

from cdevents.cdevent import SPEC_VERSION, CDEvent
from cdevents.context import Context
from cdevents.subject import Subject


@dataclass
class BuildFinishedSubjectContent:
    """Content for build subjects when a build is finished."""

    artifact_id: str
    """PURL-format ID of artifact produced by the build."""


@dataclass
class BuildSubject(Subject):
    """Subject for build-related events."""

    type: str = field(default="build", init=False)

    content: Union[Dict, BuildFinishedSubjectContent] = field(default_factory=dict, init=False)


@dataclass
class BuildFinishedSubject(BuildSubject):
    """Subject for artifact-related messages."""

    content: BuildFinishedSubjectContent
    """Content for build finished."""


# region BuildQueuedEvent


@dataclass
class BuildQueuedEvent(CDEvent):
    """Build queued event."""

    CDEVENT_TYPE = "dev.cdevents.build.queued." + SPEC_VERSION

    subject: BuildSubject
    """Build subject."""


def new_build_queued_event(
    context_id: str,
    context_source: str,
    context_timestamp: datetime,
    subject_id: str,
    subject_source: str,
    custom_data: Union[str, Dict, None],
    custom_data_content_type: str,
) -> BuildQueuedEvent:
    """Creates a new build queued CDEvent."""
    context = Context(
        type=BuildQueuedEvent.CDEVENT_TYPE,
        version=SPEC_VERSION,
        id=context_id,
        source=context_source,
        timestamp=context_timestamp,
    )

    subject = BuildSubject(id=subject_id, source=subject_source)

    event = BuildQueuedEvent(
        context=context,
        subject=subject,
        custom_data=custom_data,
        custom_data_content_type=custom_data_content_type,
    )

    return event


# endregion BuildQueuedEvent

# region BuildStartedEvent


@dataclass
class BuildStartedEvent(CDEvent):
    """Build started event."""

    CDEVENT_TYPE = "dev.cdevents.build.started." + SPEC_VERSION

    subject: BuildSubject
    """Build subject."""


def new_build_started_event(
    context_id: str,
    context_source: str,
    context_timestamp: datetime,
    subject_id: str,
    subject_source: str,
    custom_data: Union[str, Dict, None],
    custom_data_content_type: str,
) -> BuildStartedEvent:
    """Creates a new build started CDEvent."""
    context = Context(
        type=BuildStartedEvent.CDEVENT_TYPE,
        version=SPEC_VERSION,
        id=context_id,
        source=context_source,
        timestamp=context_timestamp,
    )

    subject = BuildSubject(id=subject_id, source=subject_source)

    event = BuildStartedEvent(
        context=context,
        subject=subject,
        custom_data=custom_data,
        custom_data_content_type=custom_data_content_type,
    )

    return event


# endregion BuildStartedEvent

# region BuildFinishedEvent


@dataclass
class BuildFinishedEvent(CDEvent):
    """Build finished event."""

    CDEVENT_TYPE = "dev.cdevents.build.finished." + SPEC_VERSION

    subject: BuildSubject
    """Build subject."""


def new_build_finished_event(
    context_id: str,
    context_source: str,
    context_timestamp: datetime,
    subject_id: str,
    subject_source: str,
    artifact_id: str,
    custom_data: Union[str, Dict, None],
    custom_data_content_type: str,
) -> BuildFinishedEvent:
    """Creates a new build finished CDEvent."""
    context = Context(
        type=BuildFinishedEvent.CDEVENT_TYPE,
        version=SPEC_VERSION,
        id=context_id,
        source=context_source,
        timestamp=context_timestamp,
    )

    content = BuildFinishedSubjectContent(artifact_id=artifact_id)
    subject = BuildFinishedSubject(id=subject_id, source=subject_source, content=content)

    event = BuildFinishedEvent(
        context=context,
        subject=subject,
        custom_data=custom_data,
        custom_data_content_type=custom_data_content_type,
    )

    return event


# endregion BuildFinishedEvent
