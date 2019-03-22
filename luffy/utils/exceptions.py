from rest_framework.views import exception_handler
from django.db import DatabaseError
from rest_framework.response import Response
from rest_framework import status
# python内置的日志管理器
import logging

# 创建日志对象
logger = logging.Logger("luffy")

def custom_exception_handler(exc,context):
    """自定义异常处理
    exc: 发生异常时的异常对象
    context: 发生异常时的上下文环境
    """
    response = exception_handler(exc,context)

    if response is None:
        # 数据库错误异常捕获
        view = context["view"]
        if isinstance(exc,DatabaseError):
            # 数据库出现异常了,通过日志的方式记录下来
            logger.error('数据库报错了: [%s] %s' % (view, exc))
            return Response("数据库报错了!请联系客服~",status=status.HTTP_507_INSUFFICIENT_STORAGE)
    else:
        return response