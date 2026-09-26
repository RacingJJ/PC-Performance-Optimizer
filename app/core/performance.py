from dataclasses import dataclass
import psutil


@dataclass
class SystemMetrics:
    cpu: int
    ram: int
    disk: int
    network: str


def get_system_metrics() -> SystemMetrics:
    cpu = int(psutil.cpu_percent(interval=0.2))
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage("/")
    ram = int((memory.used / memory.total) * 100)
    disk_percent = int((disk.used / disk.total) * 100)
    return SystemMetrics(
        cpu=cpu,
        ram=ram,
        disk=disk_percent,
        network="Stable",
    )


def calculate_performance_score(metrics: SystemMetrics) -> int:
    score = 100
    score -= metrics.cpu * 0.35
    score -= metrics.ram * 0.3
    score -= max(0, metrics.disk - 70) * 0.6
    score = max(0, min(100, int(score)))
    return score
