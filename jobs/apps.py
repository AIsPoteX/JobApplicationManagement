from django.apps import AppConfig


class JobsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "jobs"

    def ready(self):
        # 注册信号，处理 PDF 删除/替换时的清理
        import jobs.signals  # noqa: F401
