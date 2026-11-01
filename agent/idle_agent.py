"""
유휴 GPU 감지 에이전트 골격.
실제 기동 전에 GPU/경로 확인 필요.
"""
import time
import subprocess
from typing import Optional

try:
    import pynvml
    PYNVML_AVAILABLE = True
except ImportError:
    PYNVML_AVAILABLE = False

class IdleAgent:
    def __init__(self, gpu_index: int = 0, util_threshold: int = 10, vram_threshold_mb: int = 500):
        self.gpu_index = gpu_index
        self.util_threshold = util_threshold
        self.vram_threshold_mb = vram_threshold_mb
        self.rpc_process: Optional[subprocess.Popen] = None

    def is_idle(self) -> bool:
        if not PYNVML_AVAILABLE:
            return False
        pynvml.nvmlInit()
        handle = pynvml.nvmlDeviceGetHandleByIndex(self.gpu_index)
        util = pynvml.nvmlDeviceGetUtilizationRates(handle)
        mem = pynvml.nvmlDeviceGetMemoryInfo(handle)
        pynvml.nvmlShutdown()
        used_mb = mem.used / (1024 * 1024)
        return util.gpu < self.util_threshold and used_mb < self.vram_threshold_mb

    def start_rpc(self, bind_ip: str, port: int = 50052):
        if self.rpc_process and self.rpc_process.poll() is None:
            return
        cmd = ["rpc-server.exe", "-H", bind_ip, "-p", str(port)]
        self.rpc_process = subprocess.Popen(cmd)

    def stop_rpc(self):
        if self.rpc_process and self.rpc_process.poll() is None:
            self.rpc_process.terminate()
            self.rpc_process.wait(timeout=10)
            self.rpc_process = None

    def run(self, bind_ip: str, interval: float = 5.0):
        print("Idle agent started")
        while True:
            if self.is_idle():
                self.start_rpc(bind_ip)
            else:
                self.stop_rpc()
            time.sleep(interval)

if __name__ == "__main__":
    agent = IdleAgent()
    # 실제 IP로 교체
    # agent.run("192.168.1.20")
    print("Skeleton ready. Set bind IP and run.")
