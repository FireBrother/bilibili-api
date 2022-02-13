"""
bilibili_api.series

合集相关操作。
"""

from .utils.utils import get_api
from .utils.network import request
from .utils.Credential import Credential

API = get_api("series")


async def get_series_archives(mid: int = 0,
                              series_id: int = 1,
                              only_normal: str = "true",
                              sort: str = "desc",
                              ps: int = 30,
                              pn: int = 1,
                              credential: Credential = None,):
    """
    获取用户合集信息。

    Args:
        mid         (int, required)    : 用户uid.
        series_id   (int, required)    : 合集id.
        only_normal (str, optional)    : 未知，Defaults to true.
        sort        (str, optional)    : 排序方式. Defaults to desc
        ps          (int, optional)    : 分页大小. Defaults to 30.
        pn          (int, optional)    : 页码，从 1 开始. Defaults to 1.

    Returns:
        dict.
    """
    if credential is None:
        credential = Credential()
    api = API["series"]["archives"]
    params = {
        "mid": mid,
        "series_id": series_id,
        "only_normal": only_normal,
        "sort": sort,
        "ps": ps,
        "pn": pn
    }
    return await request("GET", url=api["url"], params=params, credential=credential)
