import gymnasium
import numpy as np
from gymnasium.wrappers.vector import JaxToNumpy  # , JaxToTorch

import crazyflow  # noqa: F401, register gymnasium envs
from crazyflow.utils import enable_cache


def main():
    enable_cache()
    SEED = 42
    envs = gymnasium.make_vec("DroneReachPos-v0", num_envs=20, freq=50, time_horizon_in_seconds=2)

    # This wrapper makes it possible to interact with the environment using numpy arrays, if desired. JaxToTorch is available as well.
    envs = JaxToNumpy(envs)

    # Dummy action for going up (in attitude control)
    action = np.zeros((20, 4), dtype=np.float32)
    action[..., 0] = 0.4

    # Environments provide reset parameters that can be used to set the initial state of the environment.
    obs, info = envs.reset(
        seed=SEED,
        options={
            "pos_min": np.array([-1.0, 1.0, 1.0]),
            "pos_max": np.array([-1.0, 1.0, 1.0]),
            "vel_min": 0.0,
            "vel_max": 0.0,
            "goal_pos_min": np.array([-1.0, 1.0, 1.0]),
            "goal_pos_max": np.array([-1.0, 1.0, 1.0]),
        },
    )

    # Step through the environment
    for _ in range(100):
        observation, reward, terminated, truncated, info = envs.step(action)
        envs.render()

    envs.close()


if __name__ == "__main__":
    main()
