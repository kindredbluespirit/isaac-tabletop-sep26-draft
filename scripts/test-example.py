from isaaclab_arena.assets.asset_registry import AssetRegistry
from isaaclab_arena.environments.arena_env_builder import ArenaEnvBuilder, ArenaEnvBuilderCfg
from isaaclab_arena.environments.isaaclab_arena_environment import IsaacLabArenaEnvironment
from isaaclab_arena.scene.scene import Scene

asset_registry = AssetRegistry()

# Select building blocks
background = asset_registry.get_asset_by_name("kitchen")()
embodiment = asset_registry.get_asset_by_name("franka_ik")()
cracker_box = asset_registry.get_asset_by_name("cracker_box")()
tomato_soup_can = asset_registry.get_asset_by_name("tomato_soup_can")()

# Compose the environment
scene = Scene(assets=[background, cracker_box, tomato_soup_can])
env_cfg = IsaacLabArenaEnvironment(
    name="franka_kitchen_example",
    embodiment=embodiment,
    scene=scene,
)

builder_cfg = ArenaEnvBuilderCfg()
env_builder = ArenaEnvBuilder(env_cfg, builder_cfg)
env = env_builder.make_registered()
env.reset()