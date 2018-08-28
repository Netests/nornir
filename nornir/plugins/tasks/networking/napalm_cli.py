from typing import List

from nornir.core.result import Result
from nornir.core.task import HostTask


def napalm_cli(task: HostTask, commands: List[str]) -> Result:
    """
    Run commands on remote devices using napalm

    Arguments:
        commands: commands to execute

    Returns:
        Result object with the following attributes set:
          * result (``dict``): result of the commands execution
    """
    device = task.host.get_connection("napalm")
    result = device.cli(commands)
    return Result(host=task.host, result=result)
