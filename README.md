# RL Base

Single-machine (isolated) Robot Learning Base Template I use for custom experiments. May contain podman containers or a kubernetes cluster though.

It is essentially an extension to LeRobot which primarily contains the three prongs.
1. ground (our root)
2. policies (for custom policy servers, will be served via lerobot's custom PreTrainedPolicy)
3. Robot environment (exposes Isaac Sim, MuJoCo and real world robot environments)

It's a template and not a library/module.

# Teleoperation

First start the environment server, then the leader script.

### MuJoCo

```
uv run --directory worlds/mujoco scripts/start_world.py
```

### Isaac Sim

```
uv run --directory worlds/isaac scripts/start_world.py
```

### Leader

Make sure the so101 leader has been calibrated using [lelab](https://huggingface.co/docs/lerobot/main/lelab) first.
```
ls /dev/ttyACM* # assuming no other ttyACM devices are currently present
uv run scripts/teleop_so101_leader.py --port /dev/ttyACM0 # or whatever device represents the so101 leader
```

# Instructions for AGENTS

AGENTS.md has been symlinked to README.md

When the user asks a question that involves this repository,
start your exploration with the docs/ folder. The documentation
there should be enough in most cases as opposed to screening
the entire repository.

Anything python related should be handled using uv + pyproject.toml

Consider uv add instead of uv pip install when dealing with new packages.

When told to a doc, follow the YYYY-MM-DD_01_n-a-m-e.md syntax.

The Hugo project page lives in site/. To build: hugo --source site --destination public.
The Python project uses uv with hatchling, src layout (src/project-name/). Scripts live in scripts/.

Whenever you implement a plan, sometimes when I tell you, create a doc with all the details for future reference.

Do not commit anything on your own.