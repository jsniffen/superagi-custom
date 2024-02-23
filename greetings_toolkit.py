from abc import ABC
from superagi.tools.base_tool import BaseToolkit, BaseTool
from typing import Type, List
from greetings_tool import GreetingsTool


class GreetingsToolkit(BaseToolkit, ABC):
    name: str = "Test Toolkit"
    description: str = "Test Toolkit"

    def get_tools(self) -> List[BaseTool]:
        return [GreetingsTool()]

    def get_env_keys(self) -> List[str]:
        return ["FROM"]
