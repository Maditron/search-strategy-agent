import asyncio
import logging

from google.protobuf.json_format import MessageToDict, ParseDict
from google.protobuf.struct_pb2 import Value

from a2a.server.agent_execution import AgentExecutor, RequestContext
from a2a.server.events import EventQueue
from a2a.server.tasks import TaskUpdater
from a2a.helpers import new_task_from_user_message, new_text_message
from a2a.types import Part, TaskState
from a2a.utils.errors import UnsupportedOperationError

from search_strategy_agent.agent import SearchStrategyAgent
from search_strategy_agent.models import SearchStrategyInput


logger = logging.getLogger(__name__)


class SearchStrategyAgentExecutor(AgentExecutor):
    def __init__(self):
        self.agent = SearchStrategyAgent()

    async def execute(
        self,
        context: RequestContext,
        event_queue: EventQueue,
    ) -> None:
        task = context.current_task

        if task is None:
            if context.message is None:
                raise ValueError("An A2A message is required.")

            task = new_task_from_user_message(context.message)
            await event_queue.enqueue_event(task)

        updater = TaskUpdater(
            event_queue=event_queue,
            task_id=task.id,
            context_id=task.context_id,
        )

        try:
            if context.message is None:
                raise ValueError("An A2A message is required.")

            data_parts = [
                part
                for part in context.message.parts
                if part.HasField("data")
            ]

            if len(data_parts) != 1:
                raise ValueError(
                    "Exactly one JSON data part is required."
                )

            data_part = data_parts[0]

            if data_part.media_type != "application/json":
                raise ValueError(
                    "Input must use application/json."
                )

            payload = MessageToDict(data_part.data)
            agent_input = SearchStrategyInput.model_validate(payload)

            await updater.update_status(
                state=TaskState.TASK_STATE_WORKING,
                message=new_text_message("Designing search strategy."),
            )

            result = await asyncio.to_thread(
                self.agent.run,
                agent_input,
            )

            output_data = result.model_dump(mode="json")

            await updater.add_artifact(
                parts=[
                    Part(
                        data=ParseDict(output_data, Value()),
                        media_type="application/json",
                    )
                ],
                name="search-strategy",
            )

            await updater.complete()

        except Exception:
            logger.exception(
                "Search Strategy Agent execution failed."
            )

            await updater.update_status(
                state=TaskState.TASK_STATE_FAILED,
                message=new_text_message(
                    "Search strategy generation failed."
                ),
            )

    async def cancel(
        self,
        context: RequestContext,
        event_queue: EventQueue,
    ) -> None:
        raise UnsupportedOperationError()
