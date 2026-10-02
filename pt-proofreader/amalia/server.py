import modal

MODEL_NAME = "amalia-llm/AMALIA-9B-0626-DPO"
MODEL_REVISION = "c4614b9b5c7b4fe303fa20902e692fc7dface640"

GPU = "L40S"
N_GPU = 1
MINUTES = 60
VLLM_PORT = 8000
ROUTING_REGION = "eu"

vllm_image = (
    modal.Image.from_registry("nvidia/cuda:12.9.0-devel-ubuntu22.04", add_python="3.12")
    .entrypoint([])
    .uv_pip_install("vllm==0.21.0")
)

hf_cache_vol = modal.Volume.from_name("huggingface-cache", create_if_missing=True)
vllm_cache_vol = modal.Volume.from_name("vllm-cache", create_if_missing=True)

app = modal.App("amalia")


@app.server(
    image=vllm_image,
    gpu=f"{GPU}:{N_GPU}",
    scaledown_window=15 * MINUTES,
    startup_timeout=10 * MINUTES,
    volumes={
        "/root/.cache/huggingface": hf_cache_vol,
        "/root/.cache/vllm": vllm_cache_vol,
    },
    port=VLLM_PORT,
    routing_region=ROUTING_REGION,
    unauthenticated=False,
)
class Server:
    @modal.enter()
    def start(self) -> None:
        import subprocess

        cmd = [
            "vllm",
            "serve",
            MODEL_NAME,
            "--revision",
            MODEL_REVISION,
            "--host",
            "0.0.0.0",
            "--port",
            str(VLLM_PORT),
        ]

        self.process = subprocess.Popen(cmd)

    @modal.exit()
    def stop(self) -> None:
        self.process.terminate()
